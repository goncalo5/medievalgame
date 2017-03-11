import constants


class Building(object):
    def __init__(self, village, index, name, kind, cost, rate_cost, time, rate_time):
        # initiate objects
        self.village = village
        # initiate variables
        self.index = index
        self.name = name
        self.kind = kind
        # Null variables
        self.level = None
        self.cost_lv0 = list(cost)  # make a copy, for change the assign
        self.cost = cost
        self.rate_cost = rate_cost
        self.time = None

        # get constants
        self.time_lv0 = time
        self.rate_time = rate_time

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
        self.cost = []
        for i, resource in enumerate(self.village.resources):
            cost_lv0 = self.cost_lv0[i]
            rate_cost = self.rate_cost[i]
            self.cost.append(cost_lv0 * rate_cost**self.level)

    def calculate_time2build(self):
        self.time = self.time_lv0 * self.rate_time**self.level


class Mine(Building):
    def __init__(self, village, index, name, kind, cost, rate_cost, time, rate_time, resource_obj, resource):
        super(Mine, self).__init__(village, index, name, kind, cost, rate_cost, time, rate_time)
        self.resource = resource_obj

    def update_per_s(self):
        self.resource.per_s = self.resource.per_s0 * self.resource.rate_per_s ** self.level


class Factory(Building):
    def __init__(self, village, index, name, kind, cost, rate_cost, time, rate_time, factor, rate_factor):
        super(Factory, self).__init__(village, index, name, kind, cost, rate_cost, time, rate_time)
        self.factor0 = factor
        self.rate_factor = rate_factor
        self.factor = None

    def calculate_factor(self):
        # level - 1, because it's a inverso
        self.factor = 1. / (self.factor0 * self.rate_factor ** (self.level - 1))


class Storage(Building):
    def __init__(self, village, index, name, kind, cost, rate_cost, time, rate_time, capacity, rate_capacity, resource_obj, resource):
        super(Storage, self).__init__(village, index, name, kind, cost, rate_cost, time, rate_time)
        self.name = name
        self.resource = resource_obj
        self.capacity = self.capacity0 = capacity
        self.rate_capacity = rate_capacity

    def is_full(self, resource):
        return resource.total > self.capacity

    def update_storage_capacity(self):
        self.capacity = self.capacity0 * self.rate_capacity ** self.level

    def check_storage(self):
        for resource in self.village.resources:
            if self.is_full(resource):
                self.resource.total = self.capacity
