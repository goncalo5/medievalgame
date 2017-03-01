import time
import database
import constants


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
