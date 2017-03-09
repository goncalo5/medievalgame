import threading
import constants


class Campaign(object):
    def __init__(self, world, village, army, target_village):
        self.world = world
        self.army = army
        self.village = village
        self.target_village = target_village
        self.distance = 0.
        self.calc_distance()
        self.left = self.distance / self.army.speed

    def travel_loop(self):
        if self.left > 0:
            self.left -= 1
            t = threading.Timer(interval=1, function=self.travel_loop)
            t.start()


    def calc_distance(self):
        self.distance = self.world.find_distance_between2villages(
            self.village.coordinates, self.target_village.coordinates)