import constants
from logic.buildings.buildings import Building


class Market(Building):
    def __init__(self, world, village, index, name, kind, cost, rate_cost, time, rate_time):
        super(Market, self).__init__(village, index, name, kind, cost, rate_cost, time, rate_time)
        self.world = world
        self.village = village
        self.offers = []

    def new_offer(self, resource_wanted, resource_offer):  # resource = {'name': 'food', 'total': '1000'}
        if self.village not in self.world.trader.offers:
            self.world.trader.offers[self.village] = []
        self.world.trader.offers[self.village].append(Offer(self.village, resource_wanted, resource_offer))

    def delete_offer(self, offer_i):
        self.world.trader.offers[self.village].pop(offer_i)
        self.offers.pop(offer_i)


class Offer(object):
    def __init__(self, village, resource_wanted, resource_offer):
        self.village = village
        self.resource_wanted = resource_wanted
        self.resource_offer = resource_offer
        self.ratio = None

    def calculate_ratio(self):
        self.ratio = self.resource_wanted['total'] / self.resource_offer['total']
