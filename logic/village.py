import threading
import constants
from resources import Resource, Population
from buildings import Building, Mine, Storage, Factory


class Village(object):
    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.run = False
        self.is_evolving = False  # just 1 building at the same time
        self.total_fields = constants.WORLD['village']['fields']
        self.fields_left = self.total_fields
        self.fields_occupied = 0
        # Null
        self.food = self.wood = self.stone = self.iron = self.gold = None
        self.forest = self.storage = self.main_building = None

    def create_resources_objects(self):
        self.resources = []
        self.resources_dict = {}
        resources = constants.RESOURCES
        for resource in resources:
            obj = self
            name = resource['name']
            value = Resource(**resource)
            setattr(obj, name, value)
            self.resources.append(getattr(obj, name))
            self.resources_dict[name] = getattr(obj, name)
        self.n_resources = len(self.resources)

    def create_population_object(self):
        self.population = Population(village=self, **constants.POPULATION)

    def create_buildings_objects(self):
        self.factories = []
        self.mines = []
        self.storages = []
        self.buildings = []
        self.buildings_dict = {}
        buildings = constants.BUILDINGS
        for building in buildings:
            obj = self
            name = building['name']
            if building['kind'] == 'mine':
                resource = getattr(self, building['resource'])
                value = Mine(village=self, resource_obj=resource, **building)
                setattr(obj, name, value)
                self.mines.append(getattr(obj, name))
            elif building['kind'] == 'storage':
                resource = getattr(self, building['resource'])
                value = Storage(village=self, resource_obj=resource, **building)
                setattr(obj, name, value)
                self.storages.append(getattr(obj, name))
            elif building['kind'] == 'factory':
                value = Factory(village=self, **building)
                setattr(obj, name, value)
                self.factories.append(getattr(obj, name))
            else:
                value = Building(village=self, **building)
                setattr(obj, name, value)
            self.buildings.append(getattr(obj, name))
            self.buildings_dict[name] = getattr(obj, name)

    def updating_total(self):
        self.population.total += self.population.per_s
        for resource in self.resources:
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
            for i, resource in enumerate(self.resources):
                if resource.total < building.cost[i]:
                    return False
            return True

    def take_resources2evolve(self, building):
        for i, resource in enumerate(self.resources):
            resource.total -= building.cost[i]
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
