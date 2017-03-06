import constants
from buildings import Building


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


# to control all market's offers and do his own offers
class Trader(object):
    def __init__(self):
        self.ratios = constants.TRADER['ratios']
        self.profit = constants.TRADER['profit']
        self.offers = {}

    # his own offers
    # resource = {'name': 'food', 'total': '1000'}
    def calculate_ratio(self, resource_send, resource_receive):
        return self.profit * \
               self.ratios[resource_send['name']] / \
               self.ratios[resource_receive['name']]

    def calculate_receive(self, resource_receive, resource_send):
        ratio = self.calculate_ratio(resource_receive, resource_send)
        return resource_send / ratio


class Offer(object):
    def __init__(self, village, resource_wanted, resource_offer):
        self.village = village
        self.resource_wanted = resource_wanted
        self.resource_offer = resource_offer
        self.ratio = None

    def calculate_ratio(self):
        self.ratio = self.resource_wanted['total'] / self.resource_offer['total']
