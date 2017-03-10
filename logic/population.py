

class Population(object):
    def __init__(self, village, name, total, rate):
        self.village = village
        self.name = name
        self.total = total
        self.rate = rate
        self.happiness = None
        self.calculate_happiness()
        self.calculate_per_s()

    def calculate_happiness(self):
        self.happiness = 10
        for resource in self.village.resources:
            if resource.name.lower() == 'food':
                if resource.total <= 0:
                    self.happiness *= -1

    def calculate_per_s(self):
        self.per_s = self.total * self.happiness * self.rate