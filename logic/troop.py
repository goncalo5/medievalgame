import constants


# Infantry, Cavalry, Artillery
class Unit(object):  # or Troop
    def __init__(self, index, name, time, costs, weapon, shield, armor, speed, cargo_capacity):
        self.index = index
        self.name = name
        self.time = time  # time2build
        self.costs = costs
        self.attack = self.weapon = weapon
        self.shield = shield
        self.armor = armor
        self.speed = speed
        self.cargo_capacity = cargo_capacity
        self.n = 0  # number of TROOPS


class Infantry(Unit):
    def __init__(self, soldier, index, name, time, costs, weapon, shield, armor, speed, cargo_capacity):
        super(Infantry, self).__init__(index, name, time, costs, weapon, shield, armor, speed, cargo_capacity)
        self.soldier = soldier


class Cavalry(Unit):
    def __init__(self, soldier, worse, index, name, time, costs, weapon, shield, armor, speed, cargo_capacity):
        super(Cavalry, self).__init__(index, name, time, costs, weapon, shield, armor, speed, cargo_capacity)
        self.soldier = soldier
        self.worse = worse
        self.speed = self.worse.speed


class Artillery(Unit):
    def __init__(self, soldiers, machine, index, name, time, costs, weapon, shield, armor, speed, cargo_capacity):
        super(Artillery, self).__init__(index, name, time, costs, weapon, shield, armor, speed, cargo_capacity)
        self.soldiers = soldiers  # {spear_fighter: 5, ... obj_soldier: n_soldier}
        self.machine = machine
        self.calculate_speed()

    def calculate_speed(self):
        speed_slowest_soldier = 999
        for soldier in self.soldiers:
            if soldier.speed < speed_slowest_soldier:
                speed_slowest_soldier = soldier.speed
        self.speed = min(speed_slowest_soldier, self.machine.speed)


# Person, Horse
class LivingBeing(object):
    def __init__(self):
        pass


class Person(LivingBeing):
    def __init__(self):
        super(Person, self).__init__()


class Soldier(Person):
    def __init__(self):
        super(Soldier, self).__init__()


class Horse(LivingBeing):
    def __init__(self):
        super(Horse, self).__init__()


class Machine(object):
    def __init__(self, name):
        pass


# Weapons, shield, armor
class MilitaryObject(object):
    def __init__(self):
        pass


class Weapon(MilitaryObject):
    def __init__(self, name, power):
        super(Weapon, self).__init__()
        self.name = name
        self.power = power


class Shield(MilitaryObject):
    def __init__(self, name):
        super(Shield, self).__init__()
        self.name = name
        self.shield = constants.SHIELD[self.name]


class Armor(MilitaryObject):
    def __init__(self, name):
        super(Armor, self).__init__()
        self.name = name
        self.shield = constants.ARMOR[self.name]

