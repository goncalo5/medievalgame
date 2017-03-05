import constants
from player import Player
from village import Village


class World(object):
    def __init__(self):
        self.n_continents = 9
        self.continents = []

        self.players = []

        for i in xrange(self.n_continents):
            self.continent = Continent({'continent': i})
            self.continents.append(self.continent)

    def create_player(self, name):
        planet = self.find_a_planet()
        self.players.append(Player(name, planet))

    def find_a_planet(self):
        for c in self.continents:
            for z in c.zones:
                for v in z.villages:
                    if not v.run:
                        return v

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
