# python modules:
import datetime
import time
# kivy modules:
from kivy.app import App
from kivy import properties as kp
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.event import EventDispatcher
    # uix:
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, NoTransition, Screen
from kivy.uix.recycleview import RecycleView
# self modules:
from settings import *
import screens
from buildings import *

class Resource(Widget):
    current = kp.NumericProperty(0)
    per_s = kp.NumericProperty(0)
    _type = kp.StringProperty()
    def __init__(self, _type, **kwargs):
        super().__init__(**kwargs)
        self._type = _type.lower()
        self.current = RESOURCES.get("INIT").get(_type)
        self.per_s = RESOURCES.get("PRODUCTION").get(_type)
        self.icon = RESOURCES.get("ICON").get(_type)
        self.ratio = RESOURCES.get("RATIO")
    
    def calc_next_level(self):
        return self.per_s * self.ratio


class Unit(EventDispatcher):
    n = kp.NumericProperty(0)
    n_str = kp.StringProperty("0")
    icon = kp.StringProperty()
    def __init__(self, **kwargs):
        super().__init__()
        self.name = kwargs.get("name").upper()
        self.settings = UNITS.get(self.name)
        self.name = self.name.lower()
        self.icon = self.settings.get("ICON")
        self._type = self.settings.get("TYPE", "general")
        self.requirements = self.settings.get("REQUIREMENTS")
        self.population = self.requirements.get("POPULATION")
        self.unlock = self.requirements.get("UNLOCK")
        self.atk = self.settings.get("ATK")
        self.defence = self.settings.get("DEFENCE")
        self.speed = self.settings.get("SPEED")
        self.capacity = self.settings.get("CAPACITY")
        self.special_abilities = self.settings.get("SPECIAL_ABILITIES")
    
    def on_n(self, *args):
        self.n_str = str(self.n)

    def recruit(self, n):
        n = int(n)
        app = App.get_running_app()
        # check if can recruit:
        if app.wood.current >= self.requirements.get("WOOD") * n:
            app.wood.current -= self.requirements.get("WOOD") * n
            self.n += n


class Paladin(Unit):
    level = kp.NumericProperty()
    def __init__(self):
        super().__init__(name="PALADIN")


class Game(ScreenManager):
    overview = kp.ObjectProperty(None)
    main = kp.ObjectProperty(None)

    # def on_touch_move(self, touch):
    #     app = App.get_running_app()

    #     app.offset += touch.dy
    #     app.offset = max(app.offset, 0)


class GameApp(App):
    width = kp.NumericProperty(Window.width)
    height = kp.NumericProperty(Window.height)
    # offset = kp.NumericProperty()
    # resources:
    wood = kp.ObjectProperty(Resource("WOOD"))
    clay = kp.ObjectProperty(Resource("CLAY"))
    iron = kp.ObjectProperty(Resource("IRON"))
    population_icon = kp.StringProperty(RESOURCES.get("ICON").get("POPULATION"))
    resources_ratio = kp.NumericProperty(RESOURCES.get("RATIO"))
    population = kp.DictProperty({
        "max": BUILDINGS.get("FARM").get("POPULATION_INIT"),
        "buildings": 0,
        "units": 0,
        "total": 0,
    })
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
    time_eta = kp.ObjectProperty("")
    cancel = kp.BooleanProperty(False)
    is_upgrading = kp.BooleanProperty(False)
    # Units:
    spear_fighter = kp.ObjectProperty(Unit(name="SPEAR_FIGHTER"))
    swordsman = kp.ObjectProperty(Unit(name="SWORDSMAN"))
    axeman = kp.ObjectProperty(Unit(name="AXEMAN"))
    archer = kp.ObjectProperty(Unit(name="ARCHER"))
    scout = kp.ObjectProperty(Unit(name="SCOUT"))
    light_cavalry = kp.ObjectProperty(Unit(name="LIGHT_CAVALRY"))
    mounted_archer = kp.ObjectProperty(Unit(name="MOUNTED_ARCHER"))
    heavy_cavalry = kp.ObjectProperty(Unit(name="HEAVY_CAVALRY"))
    ram = kp.ObjectProperty(Unit(name="RAM"))
    catapult = kp.ObjectProperty(Unit(name="CATAPULT"))
    paladin = kp.ObjectProperty(Paladin())
    noble = kp.ObjectProperty(Unit(name="NOBLE"))
    militia = kp.ObjectProperty(Unit(name="MILITIA"))

    def build_config(self, *args):
        self.units = [
            self.spear_fighter, self.swordsman, self.axeman, self.archer, 
            self.scout, self.light_cavalry, self.mounted_archer, self.heavy_cavalry, 
            self.ram, self.catapult, self.paladin, self.noble, self.militia
        ]
        self.buildings = [
            self.headquarters, self.rally_point, self.statue,
            self.timber_camp, self.clay_pit, self.iron_mine,
            self.farm, self.warehouse, self.hiding_place, self.barracks, self.stable, self.workshop,
            self.academy, self.smithy, self.market, self.wall
        ]

    def build(self):
        self.game = Game(transition=NoTransition())
        self.resources = [self.wood, self.clay, self.iron]
        self.calc_current_population()
        Clock.schedule_interval(self.update_resources, .1)
        return self.game

    def calc_current_population(self):
        for building in self.buildings:
            self.population["buildings"] += building.population
        for unit in self.units:
            self.population["units"] += unit.n * unit.population

        self.population["total"] = self.population["buildings"] + self.population["units"]

    def upgrade_building(self, building):
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
        self.time_eta = datetime.datetime.fromtimestamp(time.time() + self.time_left).strftime('%H:%M:%S')
        # update resources:
        self.wood.current -= self.current_upgrading.wood
        self.clay.current -= self.current_upgrading.clay
        self.iron.current -= self.current_upgrading.iron
        self.is_upgrading = True
        Clock.schedule_interval(self.update_building, .1)
    
    def update_building(self, dt):
        if self.cancel:
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
            self.population["max"] *= self.farm.population_ratio

        self.current_upgrading = ""
        self.is_upgrading = False
    
    def cancel_upgrading(self, *args):
        if self.is_upgrading:
            self.cancel = True

    def update_resources(self, dt):
        for resource in self.resources:
            resource.current += resource.per_s * dt
            resource.current = min(resource.current, self.warehouse.max_capacity)


if __name__ == "__main__":
    GameApp().run()
