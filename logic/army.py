from campaign import Campaign


class VillageForces(object):  # village's army + military building (watch-tower ...)
    def __init__(self, village, num_of_units):
        self.attack = 0
        self.shield = 0
        self.structure = 0
        # null attributes
        self.damage = self.rate_destroyed = None
        self.village = village
        self.army = {}  # {spear_fighter: 5, ... obj_soldier: n_soldier}
        # num_of_units = {'light_fighter': 1...}
        for unit in self.village.units:
            num = num_of_units[unit.name]
            unit.n -= num
            self.army[unit] = num

        for unit in self.army:
            self.attack += unit.attack * unit.n
            self.shield += unit.shield * unit.n
            self.structure += unit.structure * unit.n


class Army(VillageForces):
    def __init__(self, village, num_of_units):
        super(Army, self).__init__(village, num_of_units)
        self.speed = 0

    def calc_speed(self):
        for unit in self.village.units:
            if unit.speed > self.speed:
                self.speed = unit.speed


