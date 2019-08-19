# kivy modules:
from kivy.app import App
from kivy.core.window import Window
    # uix:
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
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


class TimberCampDescriptionMenu(DescriptionMenu):
    def __init__(self, **kwargs):
        self.app = App.get_running_app()
        self.building = self.app.timber_camp
        super().__init__(**kwargs)


class ClayPitDescriptionMenu(DescriptionMenu):
    def __init__(self, **kwargs):
        self.app = App.get_running_app()
        self.building = self.app.clay_pit
        super().__init__(**kwargs)


class IronMineDescriptionMenu(DescriptionMenu):
    def __init__(self, **kwargs):
        self.app = App.get_running_app()
        self.building = self.app.iron_mine
        super().__init__(**kwargs)


class FarmDescriptionMenu(DescriptionMenu):
    def __init__(self, **kwargs):
        self.app = App.get_running_app()
        self.building = self.app.farm
        super().__init__(**kwargs)


class RallyPointDescriptionMenu(DescriptionMenu):
    def __init__(self, **kwargs):
        self.app = App.get_running_app()
        self.building = self.app.rally_point
        super().__init__(**kwargs)


# Resources Menus:
class ResourceMenu(Menu):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.menus = RESOURCES.get("MENUS")
        self.header_size_hint_x = self.menus.get("HEADER")
        self.content_size_hint_x = self.menus.get("CONTENT")

        # header:
        header = [
            ["Production", self.header_size_hint_x[0]],
            ["Units per sec", self.header_size_hint_x[1]],
            ["Units per sec at level %s" % (self.building.level + 1), self.header_size_hint_x[2]]
        ]
        self.create_header(header, self, BLACK)

        row = BoxLayout(orientation="horizontal")
        label = Image(source=self.resource.icon, size_hint_x=self.content_size_hint_x[0])
        row.add_widget(label)
        label = DarkLabel(text="Base production", size_hint_x=self.content_size_hint_x[1])
        row.add_widget(label)
        self.per_s_label = DarkLabel(text="%s" % self.resource.per_s, size_hint_x=self.content_size_hint_x[2])
        row.add_widget(self.per_s_label)
        self.resource.per_s * self.app.resources_ratio
        next_level = self.resource.per_s * self.app.resources_ratio
        next_level = round(next_level, 2)
        self.next_level_label = DarkLabel(text="%s" % (next_level),
                          size_hint_x=self.content_size_hint_x[3])
        self.resource.bind(per_s=self.update_labels)
        row.add_widget(self.next_level_label)
        self.add_widget(row)
    
    def update_labels(self, *args):
        self.per_s_label.text = "%s" % round(self.resource.per_s, 2)
        self.next_level_label.text = "%s" % round(self.resource.calc_next_level(), 2)


class TimberCampMenu(ResourceMenu):
    def __init__(self, **kwargs):
        self.app = App.get_running_app()
        self.building = self.app.timber_camp
        self.resource = self.app.wood
        super().__init__(**kwargs)


class ClayPitMenu(ResourceMenu):
    def __init__(self, **kwargs):
        self.app = App.get_running_app()
        self.building = self.app.clay_pit
        self.resource = self.app.clay
        super().__init__(**kwargs)


class IronMineMenu(ResourceMenu):
    def __init__(self, **kwargs):
        self.app = App.get_running_app()
        self.building = self.app.iron_mine
        self.resource = self.app.iron
        super().__init__(**kwargs)


class AvailableUnavailableMenu(Menu):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.app = App.get_running_app()
        self.all_available_rows = {}
        self.all_unavailable_rows = {}


# Buildings Menus:
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
        for unit in self.app.units:
            if unit.name not in self.app.barracks.units:
                continue
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
        label = Label(text="%s" % unit.name, size_hint_x=0.15, font_size=24)
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
        self.all_labels[unit] = Label(text="0/0", size_hint_x=0.15, font_size=24)
        row.add_widget(self.all_labels[unit])

        # Recruit:
        self.all_inputs[unit] = TextInput(size_hint_x=0.1)
        label = Label(text="(%s)" % "", size_hint_x=0.05, font_size=24)
        row.add_widget(self.all_inputs[unit])
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
        app = App.get_running_app()
        for unit, unit_input in self.all_inputs.items():
            n = unit_input.text
            if not n:
                continue
            n = int(n)
            # check if can recruit:
            if app.wood.current >= unit.requirements.get("WOOD") * n and\
                    app.clay.current >= unit.requirements.get("CLAY") * n and\
                    app.iron.current >= unit.requirements.get("IRON") * n:
                app.wood.current -= unit.requirements.get("WOOD") * n
                app.clay.current -= unit.requirements.get("CLAY") * n
                app.iron.current -= unit.requirements.get("IRON") * n
                unit.n += n
                self.all_labels.get(unit).text = "%s/%s" % (unit.n, unit.n)
                self.app.population["units"] += n
                self.app.population["total"] += n


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
        building.bind(wood_str=label.setter("text"))
        row.add_widget(img)
        row.add_widget(label)
        img = Image(source=self.app.clay.icon, size_hint_x=size_hint_x[2]/2)
        label = DarkLabel(text=str(int((building.clay))), size_hint_x=size_hint_x[2]/2, font_size=24)
        building.bind(clay_str=label.setter("text"))
        row.add_widget(img)
        row.add_widget(label)
        img = Image(source=self.app.iron.icon, size_hint_x=size_hint_x[3]/2)
        label = DarkLabel(text=str(int((building.clay))), size_hint_x=size_hint_x[3]/2, font_size=24)
        building.bind(iron_str=label.setter("text"))
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


class ScavengingPanel(Menu):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = App.get_running_app()
        label = Label(text=self.app.rally_point.scavenging.get("DESCRIPTION"), size_hint_y=0.25, font_size=22)
        self.add_widget(label)

        # units:
        units_icons = BoxLayout(orientation="horizontal", size_hint_y=0.08)
        self.add_widget(units_icons)
        self.units_inputs = BoxLayout(orientation="horizontal", size_hint_y=0.08)
        self.add_widget(self.units_inputs)
        units_n_labes = BoxLayout(orientation="horizontal", size_hint_y=0.08)
        self.add_widget(units_n_labes)
        for unit in self.app.units:
            if unit.name not in self.app.rally_point.scavenging.get("POSSIBLE_UNITS"):
                continue
            icon = Image(source=unit.icon)
            units_icons.add_widget(icon)
            unit_input = TextInput(text="", id=unit.name)
            unit_input.bind(text=self.unit_input_change)
            self.units_inputs.add_widget(unit_input)
            unit_n_label = Label(text=str(unit.n))
            unit.bind(n_str=unit_n_label.setter("text"))
            units_n_labes.add_widget(unit_n_label)

        # types:
        box1 = GridLayout(cols=2)
        self.add_widget(box1)
        self.images = {}
        self.collectible_resources = {}
        self.gain_label = {}
        for _type in self.app.rally_point.scavenging.get("ALL"):
            scavenging_type = self.app.rally_point.scavenging.get("ALL").get(_type)
            box2 = BoxLayout(orientation="vertical")
            box1.add_widget(box2)
            # image:
            self.images[_type] = Image(source=scavenging_type.get("icon_gray"))
            box2.add_widget(self.images[_type])
            label = Label(text=_type)
            box2.add_widget(label)
            # collectible_resources:
            self.collectible_resources[_type] = BoxLayout(orientation="vertical")
            box2.add_widget(self.collectible_resources[_type])
            image = Image(source=self.app.rally_point.scavenging.get("LOCK_ICON"))
            self.collectible_resources[_type].add_widget(image)
            button = Button(text="Unlock", id=_type)
            button.bind(on_press=self.unlock)
            box2.add_widget(button)

    
    def unit_input_change(self, *args):
        for _type in self.app.rally_point.scavenging.get("ALL"):
            capacity_per_resource = self.calc_capacity_per_resource(_type)
            self.update_resources_labels(_type, capacity_per_resource)

    def calc_capacity_per_resource(self, _type):
        scavenging_type = self.app.rally_point.scavenging.get("ALL").get(_type)

        total_capacity = 0
        for unit_input in self.units_inputs.children:
            unit = getattr(self.app, unit_input.id)
            try:
                total_capacity += int(unit_input.text) * unit.capacity
            except ValueError:
                continue
        capacity_with_factor = total_capacity * scavenging_type.get("loot_factor")
        capacity_per_resource = capacity_with_factor / 3
        return capacity_per_resource
        
    def update_resources_labels(self, _type, capacity_per_resource):
        try:
            for resource_label in self.gain_label[_type].values():
                resource_label.text = "%s" % round(capacity_per_resource)
        except KeyError:
            pass

    def unlock(self, *args):
        button = args[0]
        _type = button.id
        scavenging_type = self.app.rally_point.scavenging.get("ALL").get(_type)

        capacity_per_resource = self.calc_capacity_per_resource(_type)

        # check if can buy:
        if button.text.lower() == "unlock":
            if self.app.wood.current >= scavenging_type.get("wood") and\
                    self.app.clay.current >= scavenging_type.get("clay") and\
                    self.app.iron.current >= scavenging_type.get("iron"):
                # update resources:
                self.app.wood.current -= scavenging_type.get("wood")
                self.app.clay.current -= scavenging_type.get("clay")
                self.app.iron.current -= scavenging_type.get("iron")
                # update image:
                self.images[_type].source = scavenging_type.get("icon")
                # update collectible_resources:
                self.collectible_resources[_type].clear_widgets()
                self.gain_label[_type] = {}
                for resource in [self.app.wood, self.app.clay, self.app.iron]:
                    box = BoxLayout(orientation="horizontal")
                    self.collectible_resources[_type].add_widget(box) 
                    icon = Image(source=resource.icon)
                    box.add_widget(icon)
                    self.gain_label[_type][resource] = Label(text="%s" % round(capacity_per_resource))
                    box.add_widget(self.gain_label[_type][resource])

                button.text = "Start"

        elif button.text.lower() == "start":
            # check if you have the units:
            
            for unit_input in self.units_inputs.children:
                unit = getattr(self.app, unit_input.id)
                if unit.name not in self.app.rally_point.scavenging.get("POSSIBLE_UNITS"):
                    continue
                if not unit_input.text:
                    continue
                if unit.n < int(unit_input.text):
                    return
            # update resources:
            for resource in [self.app.wood, self.app.clay, self.app.iron]:
                resource.current += capacity_per_resource
            
            
