import constants
from buildings import Building
from army import Army
from troop import Unit
from campaign import Campaign


# Where the soldiers are trained
class Barracks(Building):
    def __init__(self, village, units, index, name, kind, cost, rate_cost, time, rate_time):
        super(Barracks, self).__init__(village, index, name, kind, cost, rate_cost, time, rate_time)

    def training_soldiers(self, soldier, number=1):
        try:
            self.soldiers[soldier].n += number
        except AttributeError:
            self.soldiers[soldier].n = number

    def to_fire_soldiers(self, soldier, number=1):
        self.soldiers[soldier].n -= number


# where the army is created and organized
class RallyPoint(Building):
    def __init__(self, world, village, index, name, kind, cost, rate_cost, time, rate_time):
        super(RallyPoint, self).__init__(village, index, name, kind, cost, rate_cost, time, rate_time)
        self.world = world
        self.village = village


    def create_army(self, num_of_units):
        # num_of_units = {'light_fighter': 1...}
        self.army = Army(village=self.village, num_of_units=num_of_units)

    def delete_army(self):
        self.army = {}

    def start_campaign(self, coordinates_target_village):
        Campaign(world=self.world, army=self.army, village=self.village,
                 target_village=self.world.coordinates2village(coordinates_target_village))

    def back2village(self):
        pass