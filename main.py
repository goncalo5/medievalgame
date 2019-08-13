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
        self.menus = self.settings.get("MENUS")

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
        self.all_available_rows = {}
        self.all_unavailable_rows = {}

    def create_header(self, header, box, color=(1, 1, 1, 1)):
        row = BoxLayout(orientation="horizontal", size_hint_y=None)

        for name, hint_x in header:
            label = Label(text=name, size_hint_x=hint_x)
            label.color = color
            row.add_widget(label)
        if box == "return":
            return row
        box.add_widget(row)


class AllUnitsRecruit(AvailableUnavailableMenu):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.all_inputs = {}
        self.all_labels = {}

        # Availables:
        self.available_box = BoxLayout(orientation="vertical")
        for building_name in BUILDINGS:
            building = getattr(self.app, building_name.lower())
            building.bind(level=self.update_units_availables)

        header = [
            ["Unit", 0.25],
            ["Requirements", 0.5],
            ["In the\nvillage/total", 0.15],
            ["Recruit", 0.15]
        ]
        self.create_header(header, self.available_box)
        self.create_all_availables(self.app.barracks, self.available_box)
        self.create_button()

        # Unavailables:
        self.unavailable_box = BoxLayout(orientation="vertical")
        header = [
            ["Not yet available", 0.30],
            ["Requirements", 0.70]
        ]
        self.create_header(header, self.unavailable_box)
        self.create_all_not_availables(self.unavailable_box)

    def update_units_availables(self, *args):
        building = args[0]
        if "units" not in dir(building):
            return
        for unit_name in building.units:
            unit = getattr(self.app, unit_name)
            if self.check_if_is_available(unit):
                if unit not in self.all_available_rows:
                    self.add_1_available_row(unit, self.available_box)
                if unit in self.all_unavailable_rows:
                    row = self.all_unavailable_rows.pop(unit)
                    self.unavailable_box.remove_widget(row)

    def create_button(self):
        self.button = Button(text="Recruit", size_hint_y=0.2, size_hint_x=0.15, pos_hint={"x": 0.85})
        self.button.bind(on_press=self.check)
        self.add_widget(self.button)
    
    def create_all_availables(self, building, box):
        for unit_name in building.units:
            unit = getattr(self.app, unit_name)
            if self.check_if_is_available(unit):
                self.add_1_available_row(unit, box)
        self.add_widget(box)

    def create_all_not_availables(self, box):
        for unit_name in self.app.barracks.units:
            unit = getattr(self.app, unit_name)
            if not self.check_if_is_available(unit):
                self.add_1_not_available_row(unit, box)
        self.add_widget(box)

    def add_1_available_row(self, unit, box):
        row = BoxLayout(orientation="horizontal", size_hint_y=0.2)
        self.all_available_rows[unit] = row

        # Unit:
        img = Image(source=unit.icon, size_hint_x=0.05)
        label = Label(text="Spear Fighter", size_hint_x=0.15, font_size=24)
        row.add_widget(img)
        row.add_widget(label)

        # Requirements:
        img = Image(source=self.app.wood.icon, size_hint_x=0.05)
        label = Label(text=str(unit.requirements.get("WOOD")), size_hint_x=0.05, font_size=24)
        row.add_widget(img)
        row.add_widget(label)
        img = Image(source=self.app.clay.icon, size_hint_x=0.05)
        label = Label(text=str(unit.requirements.get("CLAY")), size_hint_x=0.05, font_size=24)
        row.add_widget(img)
        row.add_widget(label)
        img = Image(source=self.app.iron.icon, size_hint_x=0.05)
        label = Label(text=str(unit.requirements.get("IRON")), size_hint_x=0.05, font_size=24)
        row.add_widget(img)
        row.add_widget(label)

        # In the\nvillage/total:
        self.all_labels[unit.name] = Label(text="0/0", size_hint_x=0.15, font_size=24)
        row.add_widget(self.all_labels[unit.name])

        # Recruit:
        self.all_inputs[unit.name] = TextInput(size_hint_x=0.1)
        label = Label(text="(%s)" % "", size_hint_x=0.05, font_size=24)
        row.add_widget(self.all_inputs[unit.name])
        row.add_widget(label)
        box.add_widget(row)

    def add_1_not_available_row(self, unit, box):
        row = BoxLayout(orientation="horizontal", size_hint_y=0.2)
        self.all_unavailable_rows[unit] = row

        img = Image(source=unit.icon, size_hint_x=0.05)
        row.add_widget(img)
        label = Label(text=unit.name, size_hint_x=0.2, font_size=24)
        row.add_widget(label)
        for building_req, level_req in unit.requirements.get("UNLOCK"):
            label = Label(text="%s (Level %s)" % (building_req, level_req),
                            size_hint_x=0.25, font_size=24, color=(0.5, 0.5, 0.5, 1))
            row.add_widget(label)
        label = Label(size_hint_x=0.45)
        row.add_widget(label)
        box.add_widget(row)

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


class AllBuildingsUpgrade(AvailableUnavailableMenu):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.new()
    
    def new(self):
        # self.size_hint_y = 0.95
        self.buildings_upgrading = [None] * 2
        self.building_labels = {}
        self.building_buttons = {}

        # scrool:
        self.recycleview = RecycleView()
        self.box_scroll =\
            BoxLayout(orientation="vertical", size_hint_y=None)
        self.box_scroll.\
            bind(minimum_height=self.box_scroll.setter('height'))
        self.create_time_menu()
        self.create_available_box()
        self.create_unavailable_box()
        self.recycleview.add_widget(self.box_scroll)
        self.add_widget(self.recycleview)
    
    def update(self, *args):
        self.buildings_upgrading[0].text = str(self.app.current_upgrading)
        if self.app.time_left > 0:
            self.add_box_time()
            self.buildings_upgrading[1].text = "%s" % int(self.app.time_left)
        else:
            self.buildings_upgrading[1].text = ""
            self.remove_box_time()
        for building in self.all_available_rows:
            self.building_labels[building.name].text = "%s\n(Level %s)" % (building.name, building.level)
            self.building_buttons[building.name].text = str(int(building.level + 1))

        # update availables:
        for building_name in BUILDINGS:
            building = getattr(self.app, building_name.lower())
            if not building.unlock:
                continue
            for building_to_check_name, building_to_check_level in building.unlock:
                building_to_check = getattr(self.app, building_to_check_name.lower())
                if building_to_check.level < building_to_check_level:
                    break
            else:  # no breaks:
                if building in self.all_unavailable_rows:
                    self.unavailable_box.remove_widget(self.all_unavailable_rows[building])
                if building not in self.all_available_rows:
                    self.add_1_available_row(building)
        

    def upgrade(self, *args):
        right_button = args[0]
        for building_name, button in self.building_buttons.items():
            if button is right_button:
                building = getattr(self.app, building_name.lower())
                self.app.upgrade_building(building)


    ##############################################################
    # time menu:
    def create_time_menu(self):
        self.box_time = BoxLayout(orientation="vertical", size_hint_y=None)
        self.box_time.bind(minimum_height=self.box_time.setter('height'))

        # header:
        size_hint_x = self.app.headquarters.menus.get("TIME")
        header = [
            ["Construction", size_hint_x[0]],
            ["Duration", size_hint_x[1]],
            ["Completation", size_hint_x[2]],
            ["Cancellation", size_hint_x[3]]
        ]
        self.header_time = self.create_header(header, "return", BLACK)

        # 1 row
        self.row_time = BoxLayout(orientation="horizontal", size_hint_y=None, height=100)
            # building name
        building_name = DarkLabel(text="%s" % self.app.current_upgrading, size_hint=(size_hint_x[0], None))
        self.buildings_upgrading[0] = building_name
        self.app.bind(current_upgrading=self.update)
        self.app.bind(time_left=self.update)
        self.row_time.add_widget(building_name)
            # time left:
        time_label = DarkLabel(text="", size_hint=(size_hint_x[1], None))
        self.buildings_upgrading[1] = time_label
        self.row_time.add_widget(time_label)
            # datetime when will be finish:
        label = DarkLabel(text=self.app.time_eta, size_hint=(size_hint_x[2], None))
        self.app.bind(time_eta=label.setter("text"))
        self.row_time.add_widget(label)
            # cancel button:
        cancel_button = Button(text="Cancel", pos_hint={'center_x': 0.5, 'center_y': 0.5},
                               size_hint=(size_hint_x[3], 0.5))
        cancel_button.bind(on_press=self.app.cancel_upgrading)
        self.row_time.add_widget(cancel_button)

        # add to scroll:
        self.box_scroll.add_widget(self.box_time)

    def add_box_time(self):
        try:
            self.box_time.add_widget(self.header_time)
            self.box_time.add_widget(self.row_time)
        except:
            pass

    def remove_box_time(self):
        self.box_time.remove_widget(self.header_time)
        self.box_time.remove_widget(self.row_time)

    ##############################################################
    # AVAILABLE:
    def create_available_box(self):
        self.available_box = BoxLayout(orientation="vertical", size_hint_y=None)
        self.available_box.bind(minimum_height=self.available_box.setter('height'))
        size_hint_x = self.app.headquarters.menus.get("AVAILABLES")
        header = [
            ["Buildings", size_hint_x[0]],
            ["Wood", size_hint_x[1]],
            ["Clay", size_hint_x[2]],
            ["Iron", size_hint_x[3]],
            ["Time", size_hint_x[4]],
            ["Pop", size_hint_x[5]],
            ["Construct", size_hint_x[6]]
        ]
        self.create_header(header, self.available_box, BLACK)
        possibles = BUILDINGS
        self.create_all_availables(possibles)
        self.box_scroll.add_widget(self.available_box)

    def create_all_availables(self, possibles):
        for name in possibles:
            building = getattr(self.app, name.lower())
            if self.check_if_is_available(building):
                self.add_1_available_row(building)

    def add_1_available_row(self, building):
        row = BoxLayout(orientation="horizontal", size_hint_y=None, height=100)
        self.all_available_rows[building] = row

        size_hint_x = self.app.headquarters.menus.get("AVAILABLES")
        # Building:
        img = Image(source=building.icon, size_hint_x=size_hint_x[0] / 4)
        building_label = DarkLabel(text="%s\n(Level %s)" % (building.name, building.level), 
                                   size_hint_x=size_hint_x[0] * 3/4, font_size=24)
        self.building_labels[building.name] = building_label
        building.bind(level=self.update)
        row.add_widget(img)
        row.add_widget(building_label)

        # Requirements:
        img = Image(source=self.app.wood.icon, size_hint_x=size_hint_x[1]/2)
        label = DarkLabel(text=str(int((building.wood))), size_hint_x=size_hint_x[1]/2, font_size=24)
        row.add_widget(img)
        row.add_widget(label)
        img = Image(source=self.app.clay.icon, size_hint_x=size_hint_x[2]/2)
        label = DarkLabel(text=str(int((building.clay))), size_hint_x=size_hint_x[2]/2, font_size=24)
        row.add_widget(img)
        row.add_widget(label)
        img = Image(source=self.app.iron.icon, size_hint_x=size_hint_x[3]/2)
        label = DarkLabel(text=str(int((building.clay))), size_hint_x=size_hint_x[3]/2, font_size=24)
        row.add_widget(img)
        row.add_widget(label)
        img = Image(source=RESOURCES.get("ICON").get("TIME"), size_hint_x=size_hint_x[4]/2)
        label = DarkLabel(text=str(int((building.time))), size_hint_x=size_hint_x[4]/2, font_size=24)
        row.add_widget(img)
        row.add_widget(label)
        img = Image(source=RESOURCES.get("ICON").get("POPULATION"), size_hint_x=size_hint_x[5]/2)
        label = DarkLabel(text=str(int((building.population_for_next_level))), size_hint_x=size_hint_x[5]/2, font_size=24)
        row.add_widget(img)
        row.add_widget(label)

        # button:
        button = Button(text="lv %s" % (building.level + 1), size_hint=(size_hint_x[6], 0.6),
                        pos_hint={"center_x": 0.5, "center_y": 0.5})
        self.building_buttons[building.name] = button
        button.bind(on_press=self.upgrade)
        row.add_widget(button)

        self.available_box.add_widget(row)


    ##############################################################
    # UNAVAILABLE:
    def create_unavailable_box(self):
        self.unavailable_box = BoxLayout(orientation="vertical", size_hint_y=None)
        self.unavailable_box.bind(minimum_height=self.unavailable_box.setter('height'))
        size_hint_x = self.app.headquarters.menus.get("UNAVAILABLES")
        header = [
            ["Not yet available", size_hint_x[0]],
            ["Requirements", size_hint_x[1]]
        ]
        self.create_header(header, self.unavailable_box, BLACK)
        self.create_all_not_availables()
        # self.add_widget(self.unavailable_box)
        self.box_scroll.add_widget(self.unavailable_box)

    def create_all_not_availables(self):
        for building_name in BUILDINGS:
            building = getattr(self.app, building_name.lower())
            if not self.check_if_is_available(building):
                self.add_1_not_available_row(building)

    def add_1_not_available_row(self, building):
        row = BoxLayout(orientation="horizontal", size_hint_y=None, height=100)
        if building in self.all_unavailable_rows:
            return
        self.all_unavailable_rows[building] = row
        size_hint_x = self.app.headquarters.menus.get("UNAVAILABLES")

        img = Image(source=building.icon, size_hint_x=None, width=Window.width * size_hint_x[0] / 4)
        row.add_widget(img)
        label = DarkLabel(text=building.name, size_hint_x=None, width=Window.width * size_hint_x[0] * 3/4, font_size=24)
        row.add_widget(label)
        for building_req, level_req in building.unlock:
            label = Label(text="%s (Level %s)" % (building_req, level_req),
                            size_hint_x=None, width=Window.width * size_hint_x[1] / 3, font_size=24, color=(0.5, 0.5, 0.5, 1))
            row.add_widget(label)
        self.unavailable_box.add_widget(row)
    ##############################################################

    def check_if_is_available(self, building):
        unlock = building.unlock
        if not unlock:
            return True
        for building_name, level_to_unlock in unlock:
            building = getattr(self.app, building_name.lower())
            if building.level < level_to_unlock:
                return False
        return True


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
    time_eta = kp.ObjectProperty("")
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
        self.current_population = 0
        for building in self.buildings:
            self.current_population += building.population

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
            self.max_population *= self.farm.population_ratio
        if self.current_upgrading.name == "warehouse":
            self.max_capacity = self.warehouse.capacity0 * self.warehouse.capacity_ratio**(self.warehouse.level - 1)
        # update:
        self.current_upgrading = ""
        self.is_upgrading = False
    
    def cancel_upgrading(self, *args):
        if self.is_upgrading:
            self.cancel = True


    def update_resources(self, dt):
        for resource in self.resources:
            resource.current += resource.per_s * dt
            resource.current = min(resource.current, self.max_capacity)


if __name__ == "__main__":
    GameApp().run()
