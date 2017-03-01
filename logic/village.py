import threading
import constants
from resources import Resource
from buildings import Building, Mine, Storage, Factory


class Village(object):
    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.empty = True
        self.total_fields = constants.WORLD['village']['fields']
        self.fields_left = self.total_fields
        self.fields_occupied = 0
        # Resources
        # create resources's objects
        self.wood = self.clay = self.iron = None
        resources = constants.RESOURCES
        for resource in resources:
            obj = self
            name = resource
            value = Resource(**resources[resource])
            setattr(obj, name, value)
        del resources
        self.resources = {'wood': self.wood, 'clay': self.clay, 'iron': self.iron}
        self.n_resources = len(self.resources)

        # Buildings
        self.forest = self.storage = self.main_building = None
        # create buildings's objects
        buildings = constants.BUILDINGS_UPPER
        for building in buildings:
            obj = self
            name = building['name']
            if building['type'] == 'mine':
                resource = getattr(self, building['resource'])
                value = Mine(village=self, resource_obj=resource, **building)
                setattr(obj, name, value)
            elif building['type'] == 'storage':
                resource = getattr(self, building['resource'])
                value = Storage(village=self, resource_obj=resource, **building)
                setattr(obj, name, value)
            elif building['type'] == 'factory':
                value = Factory(village=self, **building)
                setattr(obj, name, value)
            else:
                value = Building(**building)
                setattr(obj, name, value)
        del buildings
        self.mines = [self.forest]
        self.storages = [self.storage]
        self.factories = [self.main_building]
        self.buildings = self.mines + self.storages + self.factories

        self.run = False
        self.is_evolving = False  # just 1 building at the same time
        # start updating resources
        if not self.run and not self.empty:
            self.run = True
            self.updating_total()

    def updating_total(self):
        for r in self.resources:
            resource = self.resources[r]
            resource.total += resource.per_s
        if self.run:
            self.storage.check_storage()
            t = threading.Timer(interval=1, function=self.updating_total)
            t.start()

    def evolve_building(self, building):
        if self.check_if_can_evolve(building):
            self.take_resources2evolve(building)
            self.loop_evolve(building)  # time to built

    def check_if_can_evolve(self, building):
        if not self.is_evolving:
            if self.wood >= building.cost and not building.is_evolving:
                return True
        else:
            pass

    def take_resources2evolve(self, building):
        self.wood.total -= building.cost
        building.evolving = True

    def up1level(self, building):
        building.level += 1
        building.calculate_cost()
        self.update_per_s(building)  # for mines
        self.update_storage_capacity(building)  # for storages
        self.update_times(building)  # for factories

    # for mines
    def update_per_s(self, building):
        if building in self.mines:
            for mine in self.mines:
                mine.update_per_s()

    # for storage
    def update_storage_capacity(self, building):
        if building in self.storages:
            building.update_storage_capacity()

    # for factories
    def update_times(self, building):
        if building in self.factories:
            self.update_all_times()
        else:
            self.update_time(building)

    def update_time(self, building):
        time = 1
        building.calculate_time2build()
        time *= building.time
        for f in self.factories:
            f.calculate_factor()
            time *= f.factor
        building.time = time

    def update_all_times(self):
        for b in self.buildings:
            self.update_time(b)
            b.left = b.time

    def loop_evolve(self, building):
        self.is_evolving = building.is_evolving = True
        if building.evolving:
            building.left -= 1
            if building.left <= 0:
                building.left = building.time
                self.is_evolving = building.is_evolving = False
                self.up1level(building)
                building.left = building.time
                return
            t = threading.Timer(interval=1, function=self.loop_evolve, kwargs={'building': building})
            t.start()

    def save(self):
        self.run = False

    def occupy1field(self):
        self.field_left -= 1
        self.fields_ocupided += 1

    def leave1field(self):
        self.field_left += 1
        self.fields_ocupided -= 1
