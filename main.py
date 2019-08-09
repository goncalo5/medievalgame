# kivy modules:
from kivy.app import App
from kivy import properties as kp
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.event import EventDispatcher
    # uix:
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, NoTransition
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
        print("update_population_for_current_level", self.name)
        print(self.population0, self.population_ratio, self.level)
        if self.level == 0:
            self.population = 0
            self.population_for_next_level = self.population0
        else:
            self.population = int(self.population0 * self.population_ratio ** self.level)
            next_level = int(self.population0 * self.population_ratio ** (self.level + 1))
            self.population_for_next_level = next_level - self.population
        print(self.population, self.population_for_next_level)

    def update_time_for_current_level(self):
        print("update_time_for_current_level", self.name)
        try:
            app = App.get_running_app()
            headquarters_ratio = app.headquarters.time_reduce ** app.headquarters.level
        except AttributeError:
            print("AttributeError")
            headquarters_ratio = BUILDINGS.get("HEADQUARTERS").get("TIME_REDUCE")
            headquarters_level = BUILDINGS.get("HEADQUARTERS").get("LEVEL")
            headquarters_ratio = headquarters_ratio ** headquarters_level
        print("time", self.time, self.time0, self.time_ratio, self.level, headquarters_ratio)
        self.time = self.time0 * self.time_ratio ** self.level * headquarters_ratio
        print("time", self.time)


class Headquarters(Building):
    def __init__(self):
        self.settings = BUILDINGS.get("HEADQUARTERS")
        super().__init__()
        self.time_reduce = self.settings.get("TIME_REDUCE")


class RallyPoint(Building):
    def __init__(self):
        self.settings = BUILDINGS.get("RALLYPOINT")
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


class Resource(Widget):
    current = kp.NumericProperty(0)
    def __init__(self, _type, **kwargs):
        super().__init__(**kwargs)
        self.current = RESOURCES.get("INIT").get(_type)
        self.per_s = RESOURCES.get("PRODUCTION").get(_type)
        self.icon = RESOURCES.get("ICON").get(_type)


class Unit(EventDispatcher):
    n = kp.NumericProperty(0)
    def __init__(self, name):
        super().__init__()
        print(name)
        self.settings = UNITS.get(name)
        self.name = name.lower()
        self.icon = self.settings.get("ICON")
        self._type = self.settings.get("TYPE", "general")
        self.requirements = self.settings.get("REQUIREMENTS")
        self.atk = self.settings.get("ATK")
        self.defence = self.settings.get("DEFENCE")
        self.speed = self.settings.get("SPEED")
        self.capacity = self.settings.get("CAPACITY")
        self.special_abilities = self.settings.get("SPECIAL_ABILITIES")


class Game(ScreenManager):
    overview = kp.ObjectProperty(None)
    main = kp.ObjectProperty(None)

    def on_touch_move(self, touch):
        # print("on_touch_move",  touch)
        app = App.get_running_app()

        app.offset += touch.dy
        # print(app.offset)
        app.offset = max(app.offset, 0)


class GameApp(App):
    width = kp.NumericProperty(Window.width)
    height = kp.NumericProperty(Window.height)
    offset = kp.NumericProperty()
    # resources:
    wood = kp.ObjectProperty(Resource("WOOD"))
    clay = kp.ObjectProperty(Resource("CLAY"))
    iron = kp.ObjectProperty(Resource("IRON"))
    resources_ratio = kp.NumericProperty(RESOURCES.get("RATIO"))
    current_population = kp.NumericProperty(0)
    max_population = kp.NumericProperty(0)
    max_capacity = kp.NumericProperty()
    # buildings:
    headquarters = kp.ObjectProperty(Headquarters())
    rally_point = kp.ObjectProperty(RallyPoint())
    statue = kp.ObjectProperty(Statue())
    timber_camp = kp.ObjectProperty(TimberCamp())
    clay_pit = kp.ObjectProperty(ClayPit())
    iron_mine = kp.ObjectProperty(IronMine())
    farm = kp.ObjectProperty(Farm())
    warehouse = kp.ObjectProperty(Warehouse())
    hiding_place = kp.ObjectProperty(HidingPlace())
    barracks = kp.ObjectProperty(Barracks())
    stable = kp.ObjectProperty(Stable())
    workshop = kp.ObjectProperty(Workshop())
    academy = kp.ObjectProperty(Academy())
    smithy = kp.ObjectProperty(Smithy())
    market = kp.ObjectProperty(Market())
    wall = kp.ObjectProperty(Wall())
    # to upgrade buildings:
    current_upgrading = kp.ObjectProperty("")
    time_left = kp.NumericProperty()
    cancel = kp.BooleanProperty(False)
    is_upgrading = kp.BooleanProperty(False)
    # Units:
    spear_fighter = kp.ObjectProperty(Unit("SPEAR_FIGHTER"))
    swordsman = kp.ObjectProperty(Unit("SWORDSMAN"))
    axeman = kp.ObjectProperty(Unit("AXEMAN"))
    archer = kp.ObjectProperty(Unit("ARCHER"))
    scout = kp.ObjectProperty(Unit("SCOUT"))
    light_cavalry = kp.ObjectProperty(Unit("LIGHT_CAVALRY"))
    mounted_archer = kp.ObjectProperty(Unit("MOUNTED_ARCHER"))
    heavy_cavalry = kp.ObjectProperty(Unit("HEAVY_CAVALRY"))
    ram = kp.ObjectProperty(Unit("RAM"))
    catapult = kp.ObjectProperty(Unit("CATAPULT"))
    paladin = kp.ObjectProperty(Unit("PALADIN"))
    noble = kp.ObjectProperty(Unit("NOBLE"))
    militia = kp.ObjectProperty(Unit("MILITIA"))

    def build(self):
        print(Window.width)
        self.game = Game(transition=NoTransition())
        self.resources = [self.wood, self.clay, self.iron]
        self.buildings =\
            [self.headquarters, self.rally_point, self.statue,
            self.timber_camp, self.clay_pit, self.iron_mine]
        self.max_population = BUILDINGS.get("FARM").get("POPULATION_INIT")
        self.max_capacity = BUILDINGS.get("WAREHOUSE").get("CAPACITY_INIT")
        self.units = [
            self.spear_fighter, self.swordsman, self.axeman, self.archer, 
            self.scout, self.light_cavalry, self.mounted_archer, self.heavy_cavalry, 
            self.ram, self.catapult, self.paladin, self.noble, self.militia
        ]
        self.calc_current_population()
        Clock.schedule_interval(self.update_resources, .1)
        return self.game
    
    def calc_current_population(self):
        print()
        print("calc_current_population")
        self.current_population = 0
        for building in self.buildings:
            print(building.name, building.population)
            self.current_population += building.population

    def upgrade_building(self, building):
        print("upgrade_building")
        if self.is_upgrading:
            return
        # check if can upgrade:
        check_resources =\
            self.wood.current > building.wood and \
            self.clay.current > building.clay and self.iron.current > building.iron
        check_max_level = building.level < building.max_level
        if not (check_resources and check_max_level):
            return
        self.current_upgrading = building
        self.time_left = building.time
        # update resources:
        self.wood.current -= self.current_upgrading.wood
        self.clay.current -= self.current_upgrading.clay
        self.iron.current -= self.current_upgrading.iron
        self.is_upgrading = True
        Clock.schedule_interval(self.update_building, .1)
    
    def update_building(self, dt):
        print("update_building", self.current_upgrading)
        if self.cancel:
            print("cancel")
            # undo update resources:
            self.wood.current += self.current_upgrading.wood
            self.clay.current += self.current_upgrading.clay
            self.iron.current += self.current_upgrading.iron
            self.current_upgrading = ""
            self.time_left = 0
            self.cancel = False
            self.is_upgrading = False
            return False
        self.time_left -= dt
        if self.time_left <= 0:
            self.update_building_finish()
            print("finish")
            return False
    
    def update_building_finish(self):
        # update requirements:
        self.current_upgrading.level += 1
        self.current_upgrading.update_cost_for_current_level()
        self.current_upgrading.update_population_for_current_level()
        self.calc_current_population()
        self.current_upgrading.time *= self.current_upgrading.ratio
        # update buildings:
        if self.current_upgrading.name == "headquarters":
            for build in self.buildings:
                build.time *= self.current_upgrading.time_reduce
        if self.current_upgrading.name == "timber_camp":
            self.wood.per_s *= self.resources_ratio
        if self.current_upgrading.name == "clay_pit":
            self.clay.per_s *= self.resources_ratio
        if self.current_upgrading.name == "iron_mine":
            self.iron.per_s *= self.resources_ratio
        if self.current_upgrading.name == "farm":
            self.max_population *= self.farm.population_ratio
        if self.current_upgrading.name == "warehouse":
            self.max_capacity = self.warehouse.capacity0 * self.warehouse.capacity_ratio**(self.warehouse.level - 1)
        # update:
        self.current_upgrading = ""
        self.is_upgrading = False
    
    def cancel_upgrading(self):
        if self.is_upgrading:
            self.cancel = True


    def update_resources(self, dt):
        for resource in self.resources:
            resource.current += resource.per_s * dt
            resource.current = min(resource.current, self.max_capacity)


if __name__ == "__main__":
    GameApp().run()
