# python modules:
import datetime
import time
from collections import defaultdict
# kivy modules:
from kivy.app import App
from kivy.clock import Clock
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
    wood_str = kp.StringProperty()
    clay_str = kp.StringProperty()
    iron_str = kp.StringProperty()
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

        self.bind(wood=self.update_str, clay=self.update_str, iron=self.update_str)
    
    def __repr__(self):
        return self.name

    def update_str(self, *args):
        self.wood_str = str(int(self.wood))
        self.clay_str = str(int(self.clay))
        self.iron_str = str(int(self.iron))

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
    attacker = kp.DictProperty(defaultdict(int))
    defender = kp.DictProperty(defaultdict(int))
    units_kills_atk = kp.DictProperty(defaultdict(int))
    units_kills_def = kp.DictProperty(defaultdict(int))
    def __init__(self):
        self.settings = BUILDINGS.get("RALLY_POINT")
        super().__init__()
        self.scavenging = self.settings.get("SCAVENGING")
    
    def calc_simulator(self, *args):
        print("simulator", args)
        attacker_inputs = args[0]
        attacker_inputs = list(reversed(attacker_inputs.children[:-1]))
        defender_inputs = args[1]
        defender_inputs = list(reversed(defender_inputs.children[:-1]))
        app = args[2]

        # attacker = defaultdict(int)
        attacker_power_per_type = defaultdict(int)
        total_defender_power_per_type = defaultdict(lambda: app.wall.basic_defense)
        defender_power_per_type = defaultdict(int)
        total_population_per_type = defaultdict(int)
        total_population_per_type_def = defaultdict(int)
        perc_population_per_type = defaultdict(int)
        _types = ["general", "cavalry", "archer"]

        # get input units:
        for i, unit in enumerate(app.units):
            try:
                self.attacker[unit] = int(attacker_inputs[i].text)
            except ValueError:
                self.attacker[unit] = 0
            try:
                self.defender[unit] = int(defender_inputs[i].text)
            except ValueError:
                self.defender[unit] = 0

        print("attacker", self.attacker)
        print("defender", self.defender)

        # calc total power done for all units per type:
        for i, unit in enumerate(app.units):
            attacker_power_per_type[unit._type] += self.attacker[unit] * unit.atk
            for _type in _types:
                total_defender_power_per_type[_type] += self.defender[unit] * unit.defence.get(_type.upper())
        print("attacker_power_per_type", attacker_power_per_type)
        print("total_defender_power_per_type", total_defender_power_per_type)

        # calc total_population_per_type:
        for i, unit in enumerate(app.units):
            total_population_per_type[unit._type] += self.attacker[unit] * unit.population
            total_population_per_type_def[unit._type] += self.defender[unit] * unit.population
        print("total_population_per_type", total_population_per_type)
        print("total_population_per_type_def", total_population_per_type_def)
        
        # calc perc_population_per_type:
        total_all_types_population = sum(total_population_per_type.values())
        try:
            for _type in _types:
                perc_population_per_type[_type] += total_population_per_type[_type] / total_all_types_population
        except ZeroDivisionError:
            return
        print("perc_population_per_type", perc_population_per_type)

        # calc defender power after aply perc_population_per_type:
        for _type in _types:
            defender_power_per_type[_type] = total_defender_power_per_type[_type] * perc_population_per_type[_type]
        print("defender_power_per_type", defender_power_per_type)

        # calc total_killed_units_per_type by type:
        total_killed_units_per_type = defaultdict(int)
        total_killed_units_per_type_def = defaultdict(int)
        for _type in _types:
            print(_type)
            if attacker_power_per_type[_type] == 0:
                continue
            if total_population_per_type[_type] == 0:
                continue
            x = attacker_power_per_type[_type] / defender_power_per_type[_type]
            x_defender = defender_power_per_type[_type] / attacker_power_per_type[_type]
            print("x", x)
            print("x_defender", x_defender)
            ratio = 1 / x**0.5
            ratio_defender = 1 / x_defender**0.5
            print("ratio", ratio)
            print("ratio_defender", ratio_defender)
            damage_done_by_def = ratio * defender_power_per_type[_type]
            damage_done_by_atk = ratio_defender * attacker_power_per_type[_type]
            print("damage_done_by_def", damage_done_by_def)
            print("damage_done_by_atk", damage_done_by_atk)
            total_killed_units_per_type[_type] =\
                damage_done_by_def / attacker_power_per_type[_type] * total_population_per_type[_type]
            total_killed_units_per_type_def[_type] =\
                damage_done_by_atk / defender_power_per_type[_type] * total_population_per_type[_type]
        print("total_killed_units_per_type", total_killed_units_per_type)
        print("total_killed_units_per_type_def", total_killed_units_per_type_def)

        # calc units_kills: split the type % for all units
        for i, unit in enumerate(app.units):
            # attacker:
            try:
                ratio_units = (self.attacker[unit] * unit.population) / total_population_per_type[unit._type]
                print("ratio_units", ratio_units)
                self.units_kills_atk[unit] = total_killed_units_per_type[unit._type] * ratio_units / unit.population
                self.units_kills_atk[unit] = min(round(self.units_kills_atk[unit]), self.attacker[unit])
            except ZeroDivisionError:
                continue
            # defender:
            try:
                ratio_units_def = (self.defender[unit] * unit.population) / total_population_per_type_def[unit._type]
                print("ratio_units_def", ratio_units_def)
                self.units_kills_def[unit] = total_killed_units_per_type_def[unit._type] * ratio_units_def / unit.population
                self.units_kills_def[unit] = min(round(self.units_kills_def[unit]), self.defender[unit])
            except ZeroDivisionError:
                continue
        print("self.units_kills_atk", self.units_kills_atk)
        print("self.units_kills_def", self.units_kills_def)




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
        self.image = self.settings.get("IMAGE")


class Warehouse(Building):
    max_capacity = kp.NumericProperty()
    time_to_full = kp.DictProperty({
        "wood": "",
        "clay": "",
        "iron": ""
    })
    time_when_its_full = kp.DictProperty({
        "wood": "",
        "clay": "",
        "iron": ""
    })
    def __init__(self):
        self.settings = BUILDINGS.get("WAREHOUSE")
        super().__init__()
        self.capacity0 = self.settings.get("CAPACITY_INIT")
        self.capacity_ratio = self.settings.get("CAPACITY_RATIO")
        self.max_capacity = self.calc_capacity(self.level)
        self.bind(level=self.on_level)
        Clock.schedule_interval(self.calc_when_is_full, .1)
    
    def calc_capacity(self, level):
        return self.capacity0 * self.capacity_ratio**(level - 1)
    
    def on_level(self, *args):
        self.max_capacity = self.calc_capacity(self.level)

    def calc_when_is_full(self, *args):
        self.app = App.get_running_app()
        for resource in self.app.resources:
            resource_until_full = self.max_capacity - resource.current
            resource_until_full = max(resource_until_full, 0)
            seconds_to_full = resource_until_full / resource.per_s
            self.time_to_full[resource._type] = str(datetime.timedelta(seconds=int(seconds_to_full)))
            self.time_when_its_full[resource._type] =\
                datetime.datetime.fromtimestamp(time.time() + seconds_to_full).strftime('%H:%M:%S')


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
        self.basic_defense = self.settings.get("BASIC_DEFENSE")

