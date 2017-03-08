import math
import constants
from player import Player
from village import Village
from market import Trader


class World(object):
    def __init__(self):
        self.n_continents = constants.WORLD['n_continents']
        self.length = int(math.sqrt(self.n_continents))
        self.continents = []

        self.players = []

        self.trader = Trader()

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
