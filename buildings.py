# kivy modules:
from kivy.app import App
from kivy import properties as kp
    # uix:
from kivy.uix.widget import Widget
# self modules:
from settings import *

class Building(Widget):
    # settings = kp.DictProperty()
    level = kp.NumericProperty(0)
    wood0 = kp.NumericProperty()
    clay0 = kp.NumericProperty()
    iron0 = kp.NumericProperty()
    wood = kp.NumericProperty()
    clay = kp.NumericProperty()
    iron = kp.NumericProperty()
    time = kp.NumericProperty()
    population0 = kp.NumericProperty()
    population_ratio = kp.NumericProperty()
    population_for_next_level = kp.NumericProperty()
    population = kp.NumericProperty()
    def __init__(self):
        self.name = self.settings.get("NAME")
        self.icon = self.settings.get("ICON")
        self.level = self.settings.get("LEVEL")
        self.max_level = self.settings.get("MAX_LEVEL")
        self.wood0 = self.settings.get("REQUIREMENTS").get("WOOD")
        self.clay0 = self.settings.get("REQUIREMENTS").get("CLAY")
        self.iron0 = self.settings.get("REQUIREMENTS").get("IRON")
        self.time0 = self.settings.get("REQUIREMENTS").get("TIME")
        self.time_ratio = self.settings.get("REQUIREMENTS").get("TIME")
        self.ratio = self.settings.get("REQUIREMENTS").get("RATIO")
        self.population0 = self.settings.get("POPULATION").get("BASE")
        self.population_ratio = self.settings.get("POPULATION").get("RATIO")
        self.unlock = self.settings.get("REQUIREMENTS").get("UNLOCK", [])
        self.menus = self.settings.get("MENUS")
        self.description = self.settings.get("DESCRIPTION", "")

        self.time_left = self.time
        self.update_cost_for_current_level()
        self.update_population_for_current_level()
        self.update_time_for_current_level()
    
    def __repr__(self):
        return self.name

    def update_cost_for_current_level(self):
        self.wood = self.wood0 * self.ratio ** self.level
        self.clay = self.clay0 * self.ratio ** self.level
        self.iron = self.iron0 * self.ratio ** self.level

    def update_population_for_current_level(self):
        if self.level == 0:
            self.population = 0
            self.population_for_next_level = self.population0
        else:
            self.population = int(self.population0 * self.population_ratio ** self.level)
            next_level = int(self.population0 * self.population_ratio ** (self.level + 1))
            self.population_for_next_level = next_level - self.population

    def update_time_for_current_level(self):
        try:
            app = App.get_running_app()
            headquarters_ratio = app.headquarters.time_reduce ** app.headquarters.level
        except AttributeError:

            headquarters_ratio = BUILDINGS.get("HEADQUARTERS").get("TIME_REDUCE")
            headquarters_level = BUILDINGS.get("HEADQUARTERS").get("LEVEL")
            headquarters_ratio = headquarters_ratio ** headquarters_level
        self.time = self.time0 * self.time_ratio ** self.level * headquarters_ratio


class Headquarters(Building):
    def __init__(self):
        self.settings = BUILDINGS.get("HEADQUARTERS")
        super().__init__()
        self.time_reduce = self.settings.get("TIME_REDUCE")


class RallyPoint(Building):
    def __init__(self):
        self.settings = BUILDINGS.get("RALLY_POINT")
        super().__init__()


class Statue(Building):
    def __init__(self):
        self.settings = BUILDINGS.get("STATUE")
        super().__init__()


class TimberCamp(Building):
    def __init__(self):
        self.settings = BUILDINGS.get("TIMBER_CAMP")
        super().__init__()


class ClayPit(Building):
    def __init__(self):
        self.settings = BUILDINGS.get("CLAY_PIT")
        super().__init__()


class IronMine(Building):
    def __init__(self):
        self.settings = BUILDINGS.get("IRON_MINE")
        super().__init__()
        self.resource_name = "iron"


class Farm(Building):
    def __init__(self):
        self.settings = BUILDINGS.get("FARM")
        super().__init__()
        self.population_ratio = self.settings.get("POPULATION_RATIO")


class Warehouse(Building):
    def __init__(self):
        self.settings = BUILDINGS.get("WAREHOUSE")
        super().__init__()
        self.capacity0 = self.settings.get("CAPACITY_INIT")
        self.capacity_ratio = self.settings.get("CAPACITY_RATIO")


class HidingPlace(Building):
    def __init__(self):
        self.settings = BUILDINGS.get("HIDING_PLACE")
        super().__init__()
        self.capacity0 = self.settings.get("CAPACITY_INIT")
        self.capacity_ratio = self.settings.get("CAPACITY_RATIO")


class Barracks(Building):
    def __init__(self):
        self.settings = BUILDINGS.get("BARRACKS")
        super().__init__()
        self.speed_factor0 = self.settings.get("SPEED_FACTOR_INIT")
        self.speed_factor_ratio = self.settings.get("SPEED_FACTOR_RATIO")
        self.unlock = self.settings.get("UNLOCK")
        self.units = self.settings.get("UNITS")


class Stable(Building):
    def __init__(self):
        self.settings = BUILDINGS.get("STABLE")
        super().__init__()
        self.speed_factor0 = self.settings.get("SPEED_FACTOR_INIT")
        self.speed_factor_ratio = self.settings.get("SPEED_FACTOR_RATIO")
        self.unlock = self.settings.get("UNLOCK")


class Workshop(Building):
    def __init__(self):
        self.settings = BUILDINGS.get("WORKSHOP")
        super().__init__()
        self.speed_factor0 = self.settings.get("SPEED_FACTOR_INIT")
        self.speed_factor_ratio = self.settings.get("SPEED_FACTOR_RATIO")
        self.unlock = self.settings.get("UNLOCK")


class Academy(Building):
    def __init__(self):
        self.settings = BUILDINGS.get("ACADEMY")
        super().__init__()
        self.unlock = self.settings.get("UNLOCK")


class Smithy(Building):
    def __init__(self):
        self.settings = BUILDINGS.get("SMITHY")
        super().__init__()
        self.speed_factor0 = self.settings.get("SPEED_FACTOR_INIT")
        self.speed_factor_ratio = self.settings.get("SPEED_FACTOR_RATIO")
        self.unlock = self.settings.get("UNLOCK")


class Market(Building):
    def __init__(self):
        self.settings = BUILDINGS.get("MARKET")
        super().__init__()
        self.unlock = self.settings.get("UNLOCK")


class Wall(Building):
    def __init__(self):
        self.settings = BUILDINGS.get("WALL")
        super().__init__()
        self.speed_factor0 = self.settings.get("SPEED_FACTOR_INIT")
        self.speed_factor_ratio = self.settings.get("SPEED_FACTOR_RATIO")
        self.unlock = self.settings.get("UNLOCK")

