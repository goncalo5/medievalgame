import database
import constants


class Building(object):
    def __init__(self, village, index, name, type, cost, rate_cost, time, rate_time):
        self.village = village
        # initiate variables
        self.index = index
        self.name = name
        self.type = type
        # get constants

        class Cost:
            def __init__(self, resources):
                for r in resources:
                    obj = self
                    name = r
                    value = cost[r]
                    setattr(self, name, value)
        self.cost_lv0 = Cost(cost)
        for r in self.village.resources:
            obj = self.cost_lv0
            name = r
            value = cost[r]
            print obj, name, value
            setattr(obj, name, value)
        self.cost_lv0 = cost
        self.rate_cost = rate_cost
        self.time_lv0 = time
        self.rate_time = rate_time
        # Null variables
        self.level = None
        self.cost  = None
        self.time = None
        self.metal = None

        # initial methods
        self.see_level_in_db()
        self.see_wood_in_db()

        self.calculate_cost()
        self.calculate_time2build()

        #
        self.is_evolving = False
        self.left = self.time

    # Data Base
    # GET
    def see_level_in_db(self):
        self.level = 0

    def see_wood_in_db(self):
        pass

    # calculators
    def calculate_cost(self):
        for r in self.village.resources:

        self.cost['wood'] = self.cost_lv0 * self.rate_cost**self.level

    def calculate_time2build(self):
        self.time = self.time_lv0 * self.rate_time**self.level


class Mine(Building):
    def __init__(self, village, index, name, type, cost, rate_cost, time, rate_time, resource_obj, resource):
        super(Mine, self).__init__(village, index, name, type, cost, rate_cost, time, rate_time)
        self.resource = resource_obj

    def update_per_s(self):
        self.resource.per_s = self.resource.per_s0 * self.resource.rate_per_s ** self.level


class Factory(Building):
    def __init__(self, village, index, name, type, cost, rate_cost, time, rate_time, factor, rate_factor):
        super(Factory, self).__init__(village, index, name, type, cost, rate_cost, time, rate_time)
        self.factor0 = factor
        self.rate_factor = rate_factor
        self.factor = None

    def calculate_factor(self):
        # level - 1, because it's a inverso
        self.factor = 1. / (self.factor0 * self.rate_factor ** (self.level - 1))


class Storage(Building):
    def __init__(self, village, index, name, type, cost, rate_cost, time, rate_time, capacity, rate_capacity, resource_obj, resource):
        super(Storage, self).__init__(village, index, name, type, cost, rate_cost, time, rate_time)
        self.name = name
        self.resource = resource_obj
        self.capacity = self.capacity0 = capacity
        self.rate_capacity = rate_capacity

    def is_full(self):
        return self.resource.total > self.capacity

    def update_storage_capacity(self):
        self.capacity = self.capacity0 * self.rate_capacity ** self.level

    def check_storage(self):
        if self.is_full():
            self.resource.total = self.capacity
