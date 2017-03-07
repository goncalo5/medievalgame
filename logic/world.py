import constants
from player import Player
from village import Village
from market import Trader


class World(object):
    def __init__(self):
        self.n_continents = 9
        self.continents = []

        self.players = []

        self.trader = Trader()

        for i in xrange(self.n_continents):
            self.continent = Continent({'continent': i})
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

    def coordinates2planet(self, coordinates):
        for c in self.continents:
            for z in c.zones:
                for v in z.villages:
                    if v.coordinates == coordinates:
                        return v


class Continent(object):
    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.n_zone = 9
        self.zones = []
        for i in xrange(self.n_zone):
            coord = self.coordinates
            coord['zones'] = i
            self.zones.append(Zone(coord))


class Zone(object):
    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.n_villages = 5
        self.villages = []
        for i in xrange(self.n_villages):
            coord = self.coordinates
            coord['village'] = i
            self.villages.append(Village(coord))
