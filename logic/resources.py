import time
import database
import constants


class Population(object):
    def __init__(self, village, name, total, rate):
        print 'Population'
        self.village = village
        self.name = name
        self.total = total
        self.rate = rate
        self.happiness = None
        self.calculate_happiness()
        self.per_s = self.total * self.happiness * self.rate

    def calculate_happiness(self):
        for resource in self.village.resources:
            if resource.name == 'food':
                if resource.total > 0:
                    self.happiness = 10
                else:
                    self.happiness = -10
        print 'not found food in resources'


class Resource(object):
    def __init__(self, index, name, total, per_s, rate_per_s):
        self.index = index
        self.name = name
        self.total = total
        self.per_s0 = self.per_s = per_s
        self.rate_per_s = rate_per_s

        # Null variables

        # initial methods

    # Data Base
    # GET
    def see_total_in_db(self):
        pass

    # PUT
    def save_total_in_db(self):
        pass

    def updating_total_in_db(self):
        self.save_total_in_db()
        time.sleep(10)
        self.updating_total_in_db()
