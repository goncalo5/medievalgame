class Player(object):
    def __init__(self, name, village):
        self.name = name
        self.points = 0
        village.run = True
        village.empty = False
        village.updating_total()
        self.planets = [village]
