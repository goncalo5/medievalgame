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
# self modules:
from settings import *

class DarkLabel(Label):
    pass


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
        self.unlock = self.requirements.get("UNLOCK")
        self.atk = self.settings.get("ATK")
        self.defence = self.settings.get("DEFENCE")
        self.speed = self.settings.get("SPEED")
        self.capacity = self.settings.get("CAPACITY")
        self.special_abilities = self.settings.get("SPECIAL_ABILITIES")
    
    def recruit(self, n):
        n = int(n)
        app = App.get_running_app()
        # check if can recruit:
        if app.wood.current >= self.requirements.get("WOOD") * n:
            app.wood.current -= self.requirements.get("WOOD") * n
            self.n += n

# Screens:
class AvailableUnavailableMenu(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"

        self.app = App.get_running_app()
        self.all_inputs = {}
        self.all_labels = {}

    
    def create_header(self, header, color=(1, 1, 1, 1)):
        box = BoxLayout(orientation="horizontal", size_hint_y=0.2)

        for name, hint_x in header:
            label = Label(text=name, size_hint_x=hint_x)
            label.color = color
            box.add_widget(label)
        self.add_widget(box)
    
    def create_button(self):
        self.button = Button(text="Recruit", size_hint_y=0.2, size_hint_x=0.15, pos_hint={"x": 0.85})
        self.button.bind(on_press=self.check)
        self.add_widget(self.button)
    
    def create_all_availables(self, building):
        for unit_name in building.units:
            unit = getattr(self.app, unit_name)
            if self.check_if_is_available(unit):
                self.add_1_available_row(unit, self.app)

    def create_all_not_availables(self):
        for unit_name in self.app.barracks.units:
            unit = getattr(self.app, unit_name)
            if not self.check_if_is_available(unit):
                self.add_1_not_available_row(unit)

    def add_1_available_row(self, unit, app):
        box = BoxLayout(orientation="horizontal", size_hint_y=0.2)

        # Unit:
        img = Image(source=unit.icon, size_hint_x=0.05)
        label = Label(text="Spear Fighter", size_hint_x=0.15, font_size=24)
        box.add_widget(img)
        box.add_widget(label)

        # Requirements:
        img = Image(source=app.wood.icon, size_hint_x=0.05)
        label = Label(text=str(unit.requirements.get("WOOD")), size_hint_x=0.05, font_size=24)
        box.add_widget(img)
        box.add_widget(label)
        img = Image(source=app.clay.icon, size_hint_x=0.05)
        label = Label(text=str(unit.requirements.get("CLAY")), size_hint_x=0.05, font_size=24)
        box.add_widget(img)
        box.add_widget(label)
        img = Image(source=app.iron.icon, size_hint_x=0.05)
        label = Label(text=str(unit.requirements.get("IRON")), size_hint_x=0.05, font_size=24)
        box.add_widget(img)
        box.add_widget(label)

        # In the\nvillage/total:
        self.all_labels[unit.name] = Label(text="0/0", size_hint_x=0.15, font_size=24)
        box.add_widget(self.all_labels[unit.name])

        # Recruit:
        self.all_inputs[unit.name] = TextInput(size_hint_x=0.1)
        label = Label(text="(%s)" % "", size_hint_x=0.05, font_size=24)
        box.add_widget(self.all_inputs[unit.name])
        box.add_widget(label)
        self.add_widget(box)

    def add_1_not_available_row(self, unit):
        # print("add_1_not_available_row", unit.name)
        box = BoxLayout(orientation="horizontal", size_hint_y=0.2)
        img = Image(source=unit.icon, size_hint_x=0.05)
        box.add_widget(img)
        label = Label(text=unit.name, size_hint_x=0.2, font_size=24)
        box.add_widget(label)
        for building_req, level_req in unit.requirements.get("UNLOCK"):
            label = Label(text="%s (Level %s)" % (building_req, level_req),
                          size_hint_x=0.25, font_size=24, color=(0.5, 0.5, 0.5, 1))
            box.add_widget(label)
        label = Label(size_hint_x=0.45)
        box.add_widget(label)
        self.add_widget(box)

    def check_if_is_available(self, unit):
        unlock = unit.requirements.get("UNLOCK")
        if not unlock:
            return True
        for building_name, level_to_unlock in unlock:
            building = getattr(self.app, building_name)
            if building.level < level_to_unlock:
                return False
        return True

    def check(self, *args):
        print("check", self.all_labels)
        if not self.all_inputs:
            return
        n = self.all_inputs.get("spear_fighter").text
        n = int(n)
        app = App.get_running_app()
        # check if can recruit:
        if app.wood.current >= app.spear_fighter.requirements.get("WOOD") * n:
            app.wood.current -= app.spear_fighter.requirements.get("WOOD") * n
            app.spear_fighter.n += n
            self.all_labels.get("spear_fighter").text = "%s/%s" % (app.spear_fighter.n, app.spear_fighter.n)


class AllUnitsRecruit(AvailableUnavailableMenu):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        header = [
            ["Unit", 0.25],
            ["Requirements", 0.5],
            ["In the\nvillage/total", 0.15],
            ["Recruit", 0.15]
        ]
        self.create_header(header)
        self.create_all_availables(self.app.barracks)
        self.create_button()
        header = [
            ["Not yet available", 0.30],
            ["Requirements", 0.70]
        ]
        self.create_header(header)
        self.create_all_not_availables()


class AllBuildingsUpgrade(AvailableUnavailableMenu):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.building_labels = {}
        
        header = [
            ["Construction", 0.25],
            ["Duration", 0.25],
            ["Completation", 0.25],
            ["Cancellation", 0.25]
        ]
        self.create_header(header, BLACK)
        header = [
            ["Buildings", 0.30],
            ["Wood", 0.15],
            ["Clay", 0.15],
            ["Iron", 0.15],
            ["Time", 0.15],
            ["Pop", 0.15],
            ["Construct", 0.15]
        ]
        self.create_header(header, BLACK)
        possibles = BUILDINGS
        self.create_all_availables(possibles)
        # building = self.app.headquarters
        # self.add_1_available_row(building, self.app)
        header = [
            ["Not yet available", 0.30],
            ["Requirements", 0.70]
        ]
        self.create_header(header, BLACK)
        self.create_all_not_availables()
        # self.create_button()

    def add_1_available_row(self, building, app):
        box = BoxLayout(orientation="horizontal", size_hint_y=0.2)

        # Building:
        img = Image(source=building.icon, size_hint_x=0.05)
        building_label = DarkLabel(text="%s\n(Level %s)" % (building.name, building.level), size_hint_x=0.15, font_size=24)
        self.building_labels[building.name] = building_label
        building.bind(level=self.update_labels)
        box.add_widget(img)
        box.add_widget(building_label)

        # Requirements:
        img = Image(source=app.wood.icon, size_hint_x=0.05)
        label = DarkLabel(text=str(int((building.wood))), size_hint_x=0.05, font_size=24)
        box.add_widget(img)
        box.add_widget(label)
        img = Image(source=app.clay.icon, size_hint_x=0.05)
        label = DarkLabel(text=str(int((building.clay))), size_hint_x=0.05, font_size=24)
        box.add_widget(img)
        box.add_widget(label)
        img = Image(source=app.iron.icon, size_hint_x=0.05)
        label = DarkLabel(text=str(int((building.clay))), size_hint_x=0.05, font_size=24)
        box.add_widget(img)
        box.add_widget(label)
        img = Image(source=RESOURCES.get("ICON").get("TIME"), size_hint_x=0.05)
        label = DarkLabel(text=str(int((building.time))), size_hint_x=0.05, font_size=24)
        box.add_widget(img)
        box.add_widget(label)
        img = Image(source=RESOURCES.get("ICON").get("POPULATION"), size_hint_x=0.05)
        label = DarkLabel(text=str(int((building.population_for_next_level))), size_hint_x=0.05, font_size=24)
        box.add_widget(img)
        box.add_widget(label)

        # button:
        button = Button(text="lv %s" % (app.headquarters.level + 1), size_hint_x=0.05)
        app.upgrade_building(app.headquarters)
        button.bind(on_press=self.upgrade)
        box.add_widget(button)

        self.add_widget(box)
    
    def update_labels(self, *args):
        for building_name, label in self.building_labels.items():
            building = getattr(self.app, building_name)
            label.text = "%s\n(Level %s)" % (building.name, building.level)

    def upgrade(self, *args):
        print("upgrade", self.app.headquarters.level)
        self.app.upgrade_building(self.app.headquarters)

    def add_1_not_available_row(self, building):
        box = BoxLayout(orientation="horizontal", size_hint_y=0.2)
        img = Image(source=building.icon, size_hint_x=0.05)
        box.add_widget(img)
        label = DarkLabel(text=building.name, size_hint_x=0.2, font_size=24)
        box.add_widget(label)
        for building_req, level_req in building.unlock:
            label = Label(text="%s (Level %s)" % (building_req, level_req),
                            size_hint_x=0.25, font_size=24, color=(0.5, 0.5, 0.5, 1))
            box.add_widget(label)
        self.add_widget(box)

    def create_all_availables(self, possibles):
        for name in possibles:
            obj = getattr(self.app, name.lower())
            if self.check_if_is_available(obj):
                self.add_1_available_row(obj, self.app)
    
    def create_all_not_availables(self):
        print("create_all_not_availables", self.app.buildings)
        for building_name in BUILDINGS:
            building = getattr(self.app, building_name.lower())
            if not self.check_if_is_available(building):
                self.add_1_not_available_row(building)

    def check_if_is_available(self, building):
        print("check_if_is_available")
        unlock = building.unlock
        if not unlock:
            return True
        print("unlock", unlock)
        for building_name, level_to_unlock in unlock:
            print("building_name", building_name)
            building = getattr(self.app, building_name.lower())
            if building.level < level_to_unlock:
                return False
        return True


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
    buildings = kp.ListProperty()
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
