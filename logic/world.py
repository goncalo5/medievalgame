import constants
from player import Player
from village import Village


class World(object):
    def __init__(self):
        self.n_galaxies = 9
        self.galaxies = []

        self.players = []

        for i in xrange(self.n_galaxies):
            self.galaxy = Galaxy({'galaxy': i})
            self.galaxies.append(self.galaxy)

    def create_player(self, name):
        planet = self.find_a_planet()
        self.players.append(Player(name, planet))

    def find_a_planet(self):
        for g in self.galaxies:
            for ps in g.planetary_systems:
                for p in ps.villages:
                    if p.empty:
                        return p

    def coordinates2planet(self, coordinates):
        for g in self.galaxies:
            for ps in g.planetary_systems:
                for p in ps.villages:
                    if p.coordinates == coordinates:
                        return p


class Galaxy(object):
    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.n_planetary_system = 9
        self.planetary_systems = []
        for i in xrange(self.n_planetary_system):
            coord = self.coordinates
            coord['planetary_systems'] = i
            self.planetary_systems.append(PlanetarySystem(coord))


class PlanetarySystem(object):
    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.n_villages = 5
        self.villages = []
        for i in xrange(self.n_villages):
            coord = self.coordinates
            coord['village'] = i
            self.villages.append(Village(coord))
