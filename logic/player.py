class Player(object):
    def __init__(self, name, village):
        self.name = name
        self.points = 0
        village.run = True
        village.create_resources_objects()
        village.create_population_object()
        village.create_buildings_objects()
        village.updating_total()
        self.villages = [village]
