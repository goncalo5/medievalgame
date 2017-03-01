# resources
WOOD = {'index': 1, 'name': 'wood', 'total': 500, 'per_s': 1, 'rate_per_s': 1.5}
CLAY = {'index': 2, 'name': 'clay', 'total': 500, 'per_s': 1, 'rate_per_s': 1.5}
IRON = {'index': 3, 'name': 'iron', 'total': 500, 'per_s': 1, 'rate_per_s': 1.5}
RESOURCES = {'wood': WOOD, 'clay': CLAY,'iron': IRON}

# buildings
MAIN_BUILDING = {'index': 1, 'name': 'main_building', 'cost': 10, 'rate_cost': 2, 'time': 3, 'rate_time': 1.5,
                 'type': 'factory', 'factor': 2, 'rate_factor': 2}
FOREST = {'index': 2, 'name': 'forest', 'type': 'mine', 'cost': 10, 'rate_cost': 1.5, 'time': 3, 'rate_time': 1.5, 'resource': 'wood'}
CLAY_PIT = {'index': 3, 'name':  'clay_pit', 'cost': 10, 'rate_cost': 1.5, 'time': 3, 'rate_time': 1.5, 'type': 'mine', 'resource': 'clay'}
IRON_MINE = {'index': 4, 'name': 'iron_mine', 'cost': 10, 'rate_cost': 1.5, 'time': 3, 'rate_time': 1.5, 'type': 'mine', 'resource': 'iron'}
STORAGE = {'index': 5, 'name': 'storage', 'cost': 10, 'rate_cost': 2, 'time': 3, 'rate_time': 1.5,
           'type': 'storage', 'capacity': 1500, 'rate_capacity': 1.5, 'resource': 'wood'}
HIDING_PLACE = {'index': 6, 'name': 'hiding_place', 'cost': 10, 'rate_cost': 2, 'time': 3, 'rate_time': 1.5,
                'type': 'None'}
MARKET = {'index': 7, 'name': 'market', 'cost': 10, 'rate_cost': 2, 'time': 3, 'rate_time': 1.5,
          'type': 'None'}
FARM = {'index': 8, 'name': 'farm', 'cost': 10, 'rate_cost': 2, 'time': 3, 'rate_time': 1.5,
        'type': 'None'}
ACADEMY = {'index': 9, 'name': 'academy', 'cost': 10, 'rate_cost': 2, 'time': 3, 'rate_time': 1.5,
           'type': 'None'}
RALLY_POINT = {'index': 10, 'name': 'rally_point', 'cost': 10, 'rate_cost': 2, 'time': 3, 'rate_time': 1.5,
                               'type': 'None'}
STATUE = {'index': 11, 'name': 'statue', 'cost': 10, 'rate_cost': 2, 'time': 3, 'rate_time': 1.5,
                               'type': 'None'}
BARRACK = {'index': 12, 'name': 'barracks', 'cost': 10, 'rate_cost': 2, 'time': 3, 'rate_time': 1.5,
                               'type': 'None'}
STABLE = {'index': 13, 'name': 'stable', 'cost': 10, 'rate_cost': 2, 'time': 3, 'rate_time': 1.5,
                               'type': 'None'}
WORKSHOP = {'index': 14, 'name': 'workshop', 'cost': 10, 'rate_cost': 2, 'time': 3, 'rate_time': 1.5,
                               'type': 'None'}
SMITHY = {'index': 15, 'name': 'smithy', 'cost': 10, 'rate_cost': 2, 'time': 3, 'rate_time': 1.5,
                               'type': 'None'}
WATCHTOWER = {'index': 16, 'name': 'watchtower', 'cost': 10, 'rate_cost': 2, 'time': 3, 'rate_time': 1.5,
                               'type': 'None'}
WALL = {'index': 17, 'name': 'wall', 'cost': 10, 'rate_cost': 2, 'time': 3, 'rate_time': 1.5,
                               'type': 'None'}
BUILDINGS_UPPER = [MAIN_BUILDING, FARM,
              FOREST, CLAY_PIT, IRON_MINE, STORAGE, HIDING_PLACE, MARKET,
              ACADEMY, RALLY_POINT, STATUE, BARRACK, STABLE, WORKSHOP,
              SMITHY, WATCHTOWER, WALL]
BUILDINGS = ['main_building', 'farm',
             'forest', 'clay_pit', 'iron_mine', 'storage', 'hiding_place', 'market'
             'academy', 'rally_point', 'statue', 'barrack', 'stable', 'market'
             'smithy', 'watchtower', 'wall']

WORLD = {'fields': 100, 'village': {'fields': 100}}

WEAPONS = {'spear': 10, 'sword': 25, 'axe': 40}
SHIELD = {'simple': 10}
ARMOR = {'simple': 10}

TROOPS = \
            {'spear_fighter': {'index': 2, 'name': 'spear_fighter', 'cost': {'wood': 50, 'clay': 30, 'iron': 10},
                              'weapons': 'spear', 'shield': 'simple', 'armor': 'simple',
                              'speed': 18, 'cargo_capacity': 25},
            'swordsman': {'index': 2, 'name': 'swordsman', 'cost': {'wood': 50, 'clay': 30, 'iron': 10},
                          'weapons': 'spear', 'shield': 'simple', 'armor': 'simple',
                          'speed': 18, 'cargo_capacity': 25},
            'axeman': {'index': 2, 'name': 'axeman', 'cost': {'wood': 50, 'clay': 30, 'iron': 10},
                              'weapons': 'spear', 'shield': 'simple', 'armor': 'simple',
                              'speed': 18, 'cargo_capacity': 25},
            'light_cavalry': {'index': 2, 'name': 'light_cavalry', 'cost': {'wood': 50, 'clay': 30, 'iron': 10},
                              'weapons': 'spear', 'shield': 'simple', 'armor': 'simple',
                              'speed': 18, 'cargo_capacity': 25},
            'heavy_cavalry': {'index': 2, 'name': 'heavy_cavalry', 'cost': {'wood': 50, 'clay': 30, 'iron': 10},
                              'weapons': 'spear', 'shield': 'simple', 'armor': 'simple',
                              'speed': 18, 'cargo_capacity': 25},
            'ram':  {'index': 2, 'name': 'ram', 'cost': {'wood': 50, 'clay': 30, 'iron': 10},
                              'weapons': 'spear', 'shield': 'simple', 'armor': 'simple',
                              'speed': 18, 'cargo_capacity': 25},
            'catapult': {'index': 2, 'name': 'catapult', 'cost': {'wood': 50, 'clay': 30, 'iron': 10},
                              'weapons': 'spear', 'shield': 'simple', 'armor': 'simple',
                              'speed': 18, 'cargo_capacity': 25},
            'scout':  {'index': 2, 'name': 'scout', 'cost': {'wood': 50, 'clay': 30, 'iron': 10},
                              'weapons': 'spear', 'shield': 'simple', 'armor': 'simple',
                              'speed': 18, 'cargo_capacity': 25},
            'noble':  {'index': 2, 'name': 'noble', 'cost': {'wood': 50, 'clay': 30, 'iron': 10},
                              'weapons': 'spear', 'shield': 'simple', 'armor': 'simple',
                              'speed': 18, 'cargo_capacity': 25}
            }

N_ROUNDS = 1
DISTANCES = {'ORTHOGONAL': 1, 'DIAGONAL': 1.4}

# Presentation
MENU = ['overview', 'buildings', 'market', 'military',
        'rally_point', 'world', 'tribe']
