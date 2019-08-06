# external modules:
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager
from kivy import properties as kp
from kivy.core.window import Window
# mine modules:
from settings import *


class Building(Widget):
    # settings = kp.DictProperty()
    level = kp.NumericProperty(0)
    # wood = kp.NumericProperty(self.settings.get("REQUIREMENTS").get("WOOD"))
    # clay = kp.NumericProperty(self.settings.get("REQUIREMENTS").get("CLAY"))
    # iron = kp.NumericProperty(self.settings.get("REQUIREMENTS").get("IRON"))
    # time = kp.NumericProperty(self.settings.get("REQUIREMENTS").get("TIME"))
    # population = kp.NumericProperty(self.settings.get("REQUIREMENTS").get("POPULATION"))
    def __init__(self):
        self.level = self.settings.get("LEVEL")
        self.wood = self.settings.get("REQUIREMENTS").get("WOOD")
        self.clay = self.settings.get("REQUIREMENTS").get("CLAY")
        self.iron = self.settings.get("REQUIREMENTS").get("IRON")
        self.time = self.settings.get("REQUIREMENTS").get("TIME")
        self.population = self.settings.get("REQUIREMENTS").get("POPULATION")


class Headquarters(Building):
    def __init__(self):
        self.settings = BUILDINGS.get("HEADQUARTERS")
        super().__init__()


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
        self.settings = BUILDINGS.get("TIMBER_CAMP")
        super().__init__()


class IronMine(Building):
    def __init__(self):
        self.settings = BUILDINGS.get("TIMBER_CAMP")
        super().__init__()


class Game(ScreenManager):
    overview = kp.ObjectProperty(None)
    main = kp.ObjectProperty(None)


class GameApp(App):
    width = kp.NumericProperty(Window.width)
    # resources:
    wood = kp.NumericProperty(RESOURCES.get("WOOD"))
    clay = kp.NumericProperty(RESOURCES.get("CLAY"))
    iron = kp.NumericProperty(RESOURCES.get("IRON"))
    # buildings:
    headquarters = kp.ObjectProperty(Headquarters())
    rally_point = kp.ObjectProperty(RallyPoint())
    statue = kp.ObjectProperty(Statue())
    timber_camp = kp.ObjectProperty(TimberCamp())
    clay_pit = kp.ObjectProperty(ClayPit())
    iron_mine = kp.ObjectProperty(IronMine())

    def build(self):
        print(Window.width)
        self.game = Game()
        return self.game

    def upgrade_building(self, building):
        # check if can upgrade:
        if self.wood > building.wood and self.clay > building.clay and self.iron > building.iron:
            building.level += 1
            self.wood -= building.wood
            self.clay -= building.clay
            self.iron -= building.iron


if __name__ == "__main__":
    GameApp().run()
