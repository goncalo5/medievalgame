# population and resources
POPULATION = {'name': 'population', 'total': 10, 'rate': 0.001}
FOOD = {'index': 0, 'name': 'food', 'total': 500, 'per_s': 1, 'rate_per_s': 1.5}
WOOD = {'index': 1, 'name': 'wood', 'total': 500, 'per_s': 1, 'rate_per_s': 1.5}
STONE = {'index': 2, 'name': 'stone', 'total': 500, 'per_s': 1, 'rate_per_s': 1.5}
IRON = {'index': 3, 'name': 'iron', 'total': 500, 'per_s': 1, 'rate_per_s': 1.5}
GOLD = {'index': 4, 'name': 'gold', 'total': 500, 'per_s': 1, 'rate_per_s': 1.5}
RESOURCES = [FOOD, WOOD, STONE, IRON, GOLD]

# buildings
MAIN_BUILDING = {'index': 1, 'name': 'main_building', 'kind': 'factory', 'time': 3, 'rate_time': 1.5,
                 'cost': [0, 60, 100, 50, 0], 'rate_cost': [0, 2, 2, 2, 0], 'factor': 2, 'rate_factor': 2}
FOREST = {'index': 2, 'name': 'forest', 'kind': 'mine', 'time': 3, 'rate_time': 1.5,
          'cost': [0, 20, 0, 10, 0], 'rate_cost': [0, 2, 2, 2, 0], 'resource': 'wood'}
QUARRY = {'index': 3, 'name': 'quarry', 'kind': 'mine', 'time': 3, 'rate_time': 1.5,
            'cost': [0, 10, 10, 10, 0], 'rate_cost': [0, 2, 2, 2, 0], 'resource': 'stone'}
MINE = {'index': 4, 'name': 'mine', 'kind': 'mine', 'time': 3, 'rate_time': 1.5,
             'cost': [0, 10, 10, 10, 0], 'rate_cost': [0, 2, 2, 2, 0], 'resource': 'iron'}
STORAGE = {'index': 5, 'name': 'storage', 'kind': 'storage', 'time': 3, 'rate_time': 1.5,
           'cost': [0, 100, 150, 70, 0], 'rate_cost': [0, 2, 2, 2, 0], 'capacity': 1500, 'rate_capacity': 1.5, 'resource': 'wood'}
HIDING_PLACE = {'index': 6, 'name': 'hiding_place', 'kind': 'None', 'time': 3, 'rate_time': 1.5,
                'cost': [0, 10, 10, 10, 0], 'rate_cost': [0, 2, 2, 2, 0]}
MARKET = {'index': 7, 'name': 'market', 'kind': 'None', 'time': 3, 'rate_time': 1.5,
          'cost': [0, 10, 10, 10, 0], 'rate_cost': [0, 2, 2, 2, 0]}
FARM = {'index': 8, 'name': 'farm', 'kind': 'None', 'time': 3, 'rate_time': 1.5,
        'cost': [0, 10, 10, 10, 0], 'rate_cost': [0, 2, 2, 2, 0]}
ACADEMY = {'index': 9, 'name': 'academy', 'kind': 'None', 'time': 3, 'rate_time': 1.5,
           'cost': [0, 10, 10, 10, 0], 'rate_cost': [0, 2, 2, 2, 0]}
RALLY_POINT = {'index': 10, 'name': 'rally_point', 'kind': 'None', 'time': 3, 'rate_time': 1.5,
               'cost': [0, 10, 10, 10, 0], 'rate_cost': [0, 2, 2, 2, 0]}
STATUE = {'index': 11, 'name': 'statue', 'kind': 'None', 'time': 3, 'rate_time': 1.5,
          'cost': [0, 10, 10, 10, 0], 'rate_cost': [0, 2, 2, 2, 0]}
BARRACK = {'index': 12, 'name': 'barracks', 'kind': 'None', 'time': 3, 'rate_time': 1.5,
           'cost': [0, 10, 10, 10, 0], 'rate_cost': [0, 2, 2, 2, 0]}
STABLE = {'index': 13, 'name': 'stable', 'kind': 'None', 'time': 3, 'rate_time': 1.5,
          'cost': [0, 10, 10, 10, 0], 'rate_cost': [0, 2, 2, 2, 0]}
WORKSHOP = {'index': 14, 'name': 'workshop', 'kind': 'None', 'time': 3, 'rate_time': 1.5,
            'cost': [0, 10, 10, 10, 0], 'rate_cost': [0, 2, 2, 2, 0]}
SMITHY = {'index': 15, 'name': 'smithy', 'kind': 'None', 'time': 3, 'rate_time': 1.5,
          'cost': [0, 10, 10, 10, 0], 'rate_cost': [0, 2, 2, 2, 0]}
WATCHTOWER = {'index': 16, 'name': 'watchtower', 'kind': 'None', 'time': 3, 'rate_time': 1.5,
              'cost': [0, 10, 10, 10, 0], 'rate_cost': [0, 2, 2, 2, 0]}
WALL = {'index': 17, 'name': 'wall', 'kind': 'None', 'time': 3, 'rate_time': 1.5,
        'cost': [0, 10, 10, 10, 0], 'rate_cost': [0, 2, 2, 2, 0]}
BUILDINGS = [MAIN_BUILDING, FARM, FOREST,QUARRY, MINE, STORAGE, HIDING_PLACE, MARKET,
             ACADEMY, RALLY_POINT, STATUE, BARRACK, STABLE, WORKSHOP, SMITHY, WATCHTOWER, WALL]

WORLD = {'fields': 100, 'village': {'fields': 100}}

# Trader
TRADER = {'ratios': {'food': 1,'wood': 1,'stone': 2, 'iron': 10, 'gold': 100},
          'profit': 0.1}

WEAPONS = {'spear': 10, 'sword': 25, 'axe': 40}
SHIELD = {'simple': 10}
ARMOR = {'simple': 10}

SPEAR_FIGHTER = {'index': 2, 'name': 'spear_fighter', 'time': 3, 'cost': [50, 30, 10],
                 'weapon': 'spear', 'shield': 'simple', 'armor': 'simple', 'speed': 18, 'cargo_capacity': 25}
SWORDSMAN = {'index': 2, 'name': 'swordsman', 'time': 3, 'cost': [50, 30, 10],
             'weapon': 'spear', 'shield': 'simple', 'armor': 'simple', 'speed': 18, 'cargo_capacity': 25}
AXEMAN = {'index': 2, 'name': 'axeman', 'time': 3, 'cost': [50, 30, 10],
          'weapon': 'spear', 'shield': 'simple', 'armor': 'simple', 'speed': 18, 'cargo_capacity': 25}
LIGHT_CAVALRY = {'index': 2, 'name': 'light_cavalry', 'time': 3, 'cost': [50, 30, 10],
                 'weapon': 'spear', 'shield': 'simple', 'armor': 'simple', 'speed': 18, 'cargo_capacity': 25}
HEAVY_CAVALRY = {'index': 2, 'name': 'heavy_cavalry', 'time': 3, 'cost': [50, 30, 10],
                 'weapon': 'spear', 'shield': 'simple', 'armor': 'simple', 'speed': 18, 'cargo_capacity': 25}
RAM = {'index': 2, 'name': 'ram', 'time': 3, 'cost': [50, 30, 10],
       'weapon': 'spear', 'shield': 'simple', 'armor': 'simple', 'speed': 18, 'cargo_capacity': 25}
CATAPULT = {'index': 2, 'name': 'catapult', 'time': 3, 'cost': [50, 30, 10],
            'weapon': 'spear', 'shield': 'simple', 'armor': 'simple', 'speed': 18, 'cargo_capacity': 25}
SCOUT = {'index': 2, 'name': 'scout', 'time': 3, 'cost': [50, 30, 10],
         'weapon': 'spear', 'shield': 'simple', 'armor': 'simple', 'speed': 18, 'cargo_capacity': 25}
NOBLE = {'index': 2, 'name': 'noble', 'time': 3, 'cost': [50, 30, 10],
         'weapon': 'spear', 'shield': 'simple', 'armor': 'simple', 'speed': 18, 'cargo_capacity': 25}
TROOPS = [SPEAR_FIGHTER, SWORDSMAN, AXEMAN, LIGHT_CAVALRY, HEAVY_CAVALRY, RAM, CATAPULT, SCOUT, NOBLE]

N_ROUNDS = 1
DISTANCES = {'ORTHOGONAL': 1, 'DIAGONAL': 1.4}

# Presentation
SCREEN = '600x650'
MENU = ['overview', 'buildings', 'market', 'military',
        'rally_point', 'world', 'tribe']
