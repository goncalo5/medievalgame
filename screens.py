# kivy modules:
from kivy.app import App
from kivy.core.window import Window
    # uix:
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview import RecycleView
# self modules:
from settings import *


class DarkLabel(Label):
    pass


# Screens:
class Menu(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
    
    def create_header(self, header, box, color=(1, 1, 1, 1)):
        row = BoxLayout(orientation="horizontal", size_hint_y=None)

        for name, hint_x in header:
            label = Label(text=name, size_hint_x=hint_x)
            label.color = color
            row.add_widget(label)
        if box == "return":
            return row
        box.add_widget(row)
    
    # Descriptions Menus:
class DescriptionMenu(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "horizontal"
        self.size_hint_y = 0.3
        image = Image(size_hint_x=0.15, source=self.building.icon)
        self.add_widget(image)
        box = BoxLayout(orientation="vertical")
        self.level_label = DarkLabel(text="%s (Level %s)" % (self.building.name, self.building.level))
        self.building.bind(level=self.update_text)
        box.add_widget(self.level_label)
        label = DarkLabel(font_size=25,
            text=self.building.description)
        box.add_widget(label)

        self.add_widget(box)
    
    def update_text(self, *args):
        self.level_label.text = "%s (Level %s)" % (self.building.name, self.building.level)


class HeadquartersDescriptionMenu(DescriptionMenu):
    def __init__(self, **kwargs):
        self.app = App.get_running_app()
        self.building = self.app.headquarters
        super().__init__(**kwargs)


class BarracksDescriptionMenu(DescriptionMenu):
    def __init__(self, **kwargs):
        self.app = App.get_running_app()
        self.building = self.app.barracks
        super().__init__(**kwargs)


class IronMineDescriptionMenu(DescriptionMenu):
    def __init__(self, **kwargs):
        self.app = App.get_running_app()
        self.building = self.app.iron_mine
        super().__init__(**kwargs)


    # Resources Menus:
class ResourceMenu(Menu):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print(56, RESOURCES.get("MENUS"))

        self.menus = RESOURCES.get("MENUS")
        self.header_size_hint_x = self.menus.get("HEADER")
        self.content_size_hint_x = self.menus.get("CONTENT")

        # header:
        header = [
            ["Production", self.header_size_hint_x[0]],
            ["Units per hour", self.header_size_hint_x[1]],
            ["Units per hour at level %s" % (self.building.level + 1), self.header_size_hint_x[2]]
        ]
        self.create_header(header, self, BLACK)

class IronMineMenu(ResourceMenu):
    def __init__(self, **kwargs):
        self.app = App.get_running_app()
        self.building = self.app.iron_mine
        self.resource = self.app.iron
        print(55)
        super().__init__(**kwargs)

        print(57)
        row = BoxLayout(orientation="horizontal")
        print(58)
        label = Image(source=self.resource.icon, size_hint_x=self.content_size_hint_x[0])
        row.add_widget(label)
        label = DarkLabel(text="Base production", size_hint_x=self.content_size_hint_x[1])
        row.add_widget(label)
        label = DarkLabel(text="Base production", size_hint_x=self.content_size_hint_x[2])
        row.add_widget(label)
        label = DarkLabel(text="Base production", size_hint_x=self.content_size_hint_x[3])
        row.add_widget(label)
        self.add_widget(row)


class AvailableUnavailableMenu(Menu):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.app = App.get_running_app()
        self.all_available_rows = {}
        self.all_unavailable_rows = {}



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