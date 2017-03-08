import constants
from buildings import Building
from army import Army
from troop import Unit


# Where the soldiers are trained
class Barracks(Building):
    def __init__(self, village, index, name, kind, cost, rate_cost, time, rate_time):
        super(Barracks, self).__init__(village, index, name, kind, cost, rate_cost, time, rate_time)
        self.soldiers = {}  # {spear_fighter: 5, ... obj_soldier: n_soldier}
        for i, soldier in enumerate(constants.TROOPS):
            new_soldier = Unit(**soldier)
            self.soldiers[new_soldier] = 0  # there are no soldiers at first


    def training_soldiers(self, soldier, number=1):
        try:
            self.soldiers[soldier].n += number
        except AttributeError:
            self.soldiers[soldier].n = number

    def to_fire_soldiers(self, soldier, number=1):
        self.soldiers[soldier].n -= number


# where the army is created and organized
class RallyPoint(Building):
    def __init__(self, village, index, name, kind, cost, rate_cost, time, rate_time):
        super(RallyPoint, self).__init__(village, index, name, kind, cost, rate_cost, time, rate_time)
        self.village = village


    def create_army(self, num_of_units):
        # num_of_units = {'light_fighter': 1...}
        self.army = Army(village=self.village, num_of_units=num_of_units)

    def delete_army(self):
        self.army = {}

    def start_flight(self, coordinates_target_planet):
        target_planet = self.universe.coordinates2planet(coordinates_target_planet)
        Campaign(fleet=self, planet=self.planet, target_planet=target_planet)

    def flight_back(self):
        pass