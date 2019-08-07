# external modules:
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager
from kivy import properties as kp
from kivy.core.window import Window
from kivy.clock import Clock
# mine modules:
from settings import *


class Building(Widget):
    # settings = kp.DictProperty()
    level = kp.NumericProperty(0)
    wood = kp.NumericProperty()
    clay = kp.NumericProperty()
    iron = kp.NumericProperty()
    time = kp.NumericProperty()
    population = kp.NumericProperty()
    def __init__(self):
        self.name = self.settings.get("NAME")
        self.level = self.settings.get("LEVEL")
        self.max_level = self.settings.get("MAX_LEVEL")
        self.wood = self.settings.get("REQUIREMENTS").get("WOOD")
        self.clay = self.settings.get("REQUIREMENTS").get("CLAY")
        self.iron = self.settings.get("REQUIREMENTS").get("IRON")
        self.time = self.settings.get("REQUIREMENTS").get("TIME")
        self.population = self.settings.get("REQUIREMENTS").get("POPULATION")
        self.ratio = self.settings.get("REQUIREMENTS").get("RATIO")
        self.time_left = self.time
    
    def __repr__(self):
        return self.name


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


class Game(ScreenManager):
    overview = kp.ObjectProperty(None)
    main = kp.ObjectProperty(None)


class Resource(Widget):
    current = kp.NumericProperty(0)
    def __init__(self, _type, **kwargs):
        super().__init__(**kwargs)
        self.current = RESOURCES.get("INIT").get(_type)
        self.per_s = RESOURCES.get("PRODUCTION").get(_type)


class GameApp(App):
    width = kp.NumericProperty(Window.width)
    # resources:
    wood = kp.ObjectProperty(Resource("WOOD"))
    clay = kp.ObjectProperty(Resource("CLAY"))
    iron = kp.ObjectProperty(Resource("IRON"))
    resources_ratio = kp.NumericProperty(RESOURCES.get("RATIO"))
    # buildings:
    headquarters = kp.ObjectProperty(Headquarters())
    rally_point = kp.ObjectProperty(RallyPoint())
    statue = kp.ObjectProperty(Statue())
    timber_camp = kp.ObjectProperty(TimberCamp())
    clay_pit = kp.ObjectProperty(ClayPit())
    iron_mine = kp.ObjectProperty(IronMine())
    # to upgrade buildings:
    current_upgrading = kp.ObjectProperty("")
    time_left = kp.NumericProperty()
    cancel = kp.BooleanProperty(False)
    is_upgrading = kp.BooleanProperty(False)

    def build(self):
        print(Window.width)
        self.game = Game()
        self.resources = [self.wood, self.clay, self.iron]
        self.buildings =\
            [self.headquarters, self.rally_point, self.statue,
            self.timber_camp, self.clay_pit, self.iron_mine]
        Clock.schedule_interval(self.update_resources, .1)
        return self.game

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
            return False
        self.time_left -= dt
        if self.time_left <= 0:
            self.update_building_finish()
            print("finish")
            return False
    
    def update_building_finish(self):
        # update requirements:
        self.current_upgrading.wood *= self.current_upgrading.ratio
        self.current_upgrading.clay *= self.current_upgrading.ratio
        self.current_upgrading.iron *= self.current_upgrading.ratio
        self.current_upgrading.time *= self.current_upgrading.ratio
        self.current_upgrading.population *= self.current_upgrading.ratio
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
        # update:
        self.current_upgrading.level += 1
        self.current_upgrading = ""
        self.is_upgrading = False
    
    def cancel_upgrading(self):
        if self.is_upgrading:
            self.cancel = True


    def update_resources(self, dt):
        for resource in self.resources:
            resource.current += resource.per_s * dt


if __name__ == "__main__":
    GameApp().run()
