# resources
WOOD = {'index': 1, 'name': 'wood', 'total': 500, 'per_s': 1, 'rate_per_s': 1.5}
CLAY = {'index': 2, 'name': 'clay', 'total': 500, 'per_s': 1, 'rate_per_s': 1.5}
IRON = {'index': 3, 'name': 'iron', 'total': 500, 'per_s': 1, 'rate_per_s': 1.5}
RESOURCES = {'wood': WOOD, 'clay': CLAY, 'iron': IRON}

# buildings
MAIN_BUILDING = {'index': 1, 'name': 'main_building', 'type': 'factory',
                 'cost': {'wood': 10, 'clay': 10, 'iron': 10}, 'rate_cost': {'wood': 2, 'clay': 2, 'iron': 2},
                 'time': 3, 'rate_time': 1.5, 'factor': 2, 'rate_factor': 2}
FOREST = {'index': 2, 'name': 'forest', 'type': 'mine', 'time': 3, 'rate_time': 1.5, 'resource': 'wood',
          'cost': {'wood': 10, 'clay': 10, 'iron': 10}, 'rate_cost': {'wood': 2, 'clay': 2, 'iron': 2}}
CLAY_PIT = {'index': 3, 'name':  'clay_pit', 'cost': {'wood': 10, 'clay': 10, 'iron': 10}, 'rate_cost': {'wood': 2, 'clay': 2, 'iron': 2}, 'time': 3, 'rate_time': 1.5, 'type': 'mine', 'resource': 'clay'}
IRON_MINE = {'index': 4, 'name': 'iron_mine', 'cost': {'wood': 10, 'clay': 10, 'iron': 10}, 'rate_cost': {'wood': 2, 'clay': 2, 'iron': 2}, 'time': 3, 'rate_time': 1.5, 'type': 'mine', 'resource': 'iron'}
STORAGE = {'index': 5, 'name': 'storage', 'cost': {'wood': 10, 'clay': 10, 'iron': 10}, 'rate_cost': {'wood': 2, 'clay': 2, 'iron': 2}, 'time': 3, 'rate_time': 1.5,
           'type': 'storage', 'capacity': 1500, 'rate_capacity': 1.5, 'resource': 'wood'}
HIDING_PLACE = {'index': 6, 'name': 'hiding_place', 'cost': {'wood': 10, 'clay': 10, 'iron': 10}, 'rate_cost': {'wood': 2, 'clay': 2, 'iron': 2}, 'time': 3, 'rate_time': 1.5, 'type': 'None'}
MARKET = {'index': 7, 'name': 'market', 'cost': {'wood': 10, 'clay': 10, 'iron': 10}, 'rate_cost': {'wood': 2, 'clay': 2, 'iron': 2}, 'time': 3, 'rate_time': 1.5, 'type': 'None'}
FARM = {'index': 8, 'name': 'farm', 'cost': {'wood': 10, 'clay': 10, 'iron': 10}, 'rate_cost': {'wood': 2, 'clay': 2, 'iron': 2}, 'time': 3, 'rate_time': 1.5, 'type': 'None'}
ACADEMY = {'index': 9, 'name': 'academy', 'cost': {'wood': 10, 'clay': 10, 'iron': 10}, 'rate_cost': {'wood': 2, 'clay': 2, 'iron': 2}, 'time': 3, 'rate_time': 1.5, 'type': 'None'}
RALLY_POINT = {'index': 10, 'name': 'rally_point', 'cost': {'wood': 10, 'clay': 10, 'iron': 10}, 'rate_cost': {'wood': 2, 'clay': 2, 'iron': 2}, 'time': 3, 'rate_time': 1.5, 'type': 'None'}
STATUE = {'index': 11, 'name': 'statue', 'cost': {'wood': 10, 'clay': 10, 'iron': 10}, 'rate_cost': {'wood': 2, 'clay': 2, 'iron': 2}, 'time': 3, 'rate_time': 1.5, 'type': 'None'}
BARRACK = {'index': 12, 'name': 'barracks', 'cost': {'wood': 10, 'clay': 10, 'iron': 10}, 'rate_cost': {'wood': 2, 'clay': 2, 'iron': 2}, 'time': 3, 'rate_time': 1.5, 'type': 'None'}
STABLE = {'index': 13, 'name': 'stable', 'cost': {'wood': 10, 'clay': 10, 'iron': 10}, 'rate_cost': {'wood': 2, 'clay': 2, 'iron': 2}, 'time': 3, 'rate_time': 1.5, 'type': 'None'}
WORKSHOP = {'index': 14, 'name': 'workshop', 'cost': {'wood': 10, 'clay': 10, 'iron': 10}, 'rate_cost': {'wood': 2, 'clay': 2, 'iron': 2}, 'time': 3, 'rate_time': 1.5, 'type': 'None'}
SMITHY = {'index': 15, 'name': 'smithy', 'cost': {'wood': 10, 'clay': 10, 'iron': 10}, 'rate_cost': {'wood': 2, 'clay': 2, 'iron': 2}, 'time': 3, 'rate_time': 1.5, 'type': 'None'}
WATCHTOWER = {'index': 16, 'name': 'watchtower', 'cost': {'wood': 10, 'clay': 10, 'iron': 10}, 'rate_cost': {'wood': 2, 'clay': 2, 'iron': 2}, 'time': 3, 'rate_time': 1.5, 'type': 'None'}
WALL = {'index': 17, 'name': 'wall', 'cost': {'wood': 10, 'clay': 10, 'iron': 10}, 'rate_cost': {'wood': 2, 'clay': 2, 'iron': 2}, 'time': 3, 'rate_time': 1.5, 'type': 'None'}
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
