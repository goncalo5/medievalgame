import math
import constants
from player import Player
from village import Village


class World(object):
    def __init__(self):
        self.n_continents = constants.WORLD['n_continents']
        self.length = int(math.sqrt(self.n_continents))
        self.continents = []

        self.players = []

        self.trader = Trader()

        self.create_zones()

    def create_zones(self):
        for i in xrange(self.length):
            for j in xrange(self.length):
                coord = str(i) + str(j)
                self.continent = Continent(coordinates={'continent': coord})
                self.continents.append(self.continent)

    def create_player(self, name):
        village = self.find_a_village()
        self.players.append(Player(name, village))

    def find_a_village(self):
        for continent in self.continents:
            for zone in continent.zones:
                for village in zone.villages:
                    if not village.run:
                        return village

    def coordinates2village(self, coordinates):
        for continent in self.continents:
            for zone in continent.zones:
                for village in zone.villages:
                    if village.coordinates == coordinates:
                        return village

    def find_distance_between2villages(self, coordinates1, coordinates2):
        # coordinates = {'continent': '10', 'zone': '01', 'village': '11'}
        coordinates1 = changes_coordinates_format(coordinates1)
        coordinates2 = changes_coordinates_format(coordinates2)
        # coordinates =  (101, 011)
        x = abs(coordinates1[1] % self.length - coordinates2[1] % self.length)
        y = abs(coordinates1[0] % self.length - coordinates2[0] % self.length)
        distance = int(math.sqrt(x**2 + y**2))  # Pythagorean theorem
        return distance


def changes_coordinates_format(coordinate):
    # coordinates = {'continent': '10', 'zone': '01', 'village': '11'} => (101, 011)
    return coordinate['continent'][0] + coordinate['zone'][0] + coordinate['village'][0],\
           coordinate['continent'][1] + coordinate['zone'][1] + coordinate['village'][1]


class Continent(object):
    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.n_zone = constants.WORLD['n_zones4continent']
        self.zones = []
        for i in xrange(self.n_zone):
            coord = self.coordinates
            coord['zones'] = i
            self.zones.append(Zone(coordinates=coord))


class Zone(object):
    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.n_villages = constants.WORLD['n_villages4zone']
        self.villages = []
        for i in xrange(self.n_villages):
            coord = self.coordinates
            coord['village'] = i
            self.villages.append(Village(coordinates=coord))


# to control all market's offers and do his own offers
class Trader(object):
    def __init__(self):
        self.ratios = constants.TRADER['ratios']
        self.profit = constants.TRADER['profit']
        self.offers = {}

    # his own offers
    # resource_send, resource_receive = 'wood', 'food'
    def calculate_ratio(self, resource_send, resource_receive):
        return (1 + self.profit) * self.ratios[resource_send] / self.ratios[resource_receive]

    # resource = 1000
    def calculate_receive(self, resource_send, ratio=None):
        if ratio == None:
            ratio = self.calculate_ratio(resource_send, resource_send)
        return float(resource_send) / ratio
