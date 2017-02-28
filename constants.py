# resources
RESOURCES = {'wood': {'total': 500, 'per_s': 1, 'rate_per_s': 1.5},
             'clay': {'total': 500, 'per_s': 1, 'rate_per_s': 1.5},
             'iron': {'total': 500, 'per_s': 1, 'rate_per_s': 1.5}}

# buildings
BUILDINGS = \
    {'main_building': {'cost': 10, 'rate_cost': 2, 'time': 3, 'rate_time': 1.5,
                               'type': 'factory', 'factor': 2, 'rate_factor': 2},
             'forest': {'cost': 10, 'rate_cost': 1.5, 'time': 3, 'rate_time': 1.5,
                        'type': 'mine'},
             'clay_pit': {'cost': 10, 'rate_cost': 1.5, 'time': 3, 'rate_time': 1.5,
                          'type': 'mine'},
             'iron_mine': {'cost': 10, 'rate_cost': 1.5, 'time': 3, 'rate_time': 1.5,
                           'type': 'mine'},
             'storage': {'cost': 10, 'rate_cost': 2, 'time': 3, 'rate_time': 1.5,
                               'type': 'storage', 'capacity': 1500, 'rate_capacity': 1.5},
             'hiding_place': {'cost': 10, 'rate_cost': 2, 'time': 3, 'rate_time': 1.5,
                         'type': 'storage', 'capacity': 1500, 'rate_capacity': 1.5},
             'market': {'cost': 10, 'rate_cost': 2, 'time': 3, 'rate_time': 1.5,
                               'type': 'storage', 'capacity': 1500, 'rate_capacity': 1.5},
             'farm': {'cost': 10, 'rate_cost': 2, 'time': 3, 'rate_time': 1.5,
                               'type': 'storage', 'capacity': 1500, 'rate_capacity': 1.5},
             'academy': {'cost': 10, 'rate_cost': 2, 'time': 3, 'rate_time': 1.5,
                               'type': 'storage', 'capacity': 1500, 'rate_capacity': 1.5},
             'rally_point': {'cost': 10, 'rate_cost': 2, 'time': 3, 'rate_time': 1.5,
                               'type': 'storage', 'capacity': 1500, 'rate_capacity': 1.5},
             'statue': {'cost': 10, 'rate_cost': 2, 'time': 3, 'rate_time': 1.5,
                               'type': 'storage', 'capacity': 1500, 'rate_capacity': 1.5},
             'barracks': {'cost': 10, 'rate_cost': 2, 'time': 3, 'rate_time': 1.5,
                               'type': 'storage', 'capacity': 1500, 'rate_capacity': 1.5},
             'stable': {'cost': 10, 'rate_cost': 2, 'time': 3, 'rate_time': 1.5,
                               'type': 'storage', 'capacity': 1500, 'rate_capacity': 1.5},
             'workshop': {'cost': 10, 'rate_cost': 2, 'time': 3, 'rate_time': 1.5,
                               'type': 'storage', 'capacity': 1500, 'rate_capacity': 1.5},
             'smithy': {'cost': 10, 'rate_cost': 2, 'time': 3, 'rate_time': 1.5,
                               'type': 'storage', 'capacity': 1500, 'rate_capacity': 1.5},
             'watchtower': {'cost': 10, 'rate_cost': 2, 'time': 3, 'rate_time': 1.5,
                               'type': 'storage', 'capacity': 1500, 'rate_capacity': 1.5},
             'wall': {'cost': 10, 'rate_cost': 2, 'time': 3, 'rate_time': 1.5,
                               'type': 'storage', 'capacity': 1500, 'rate_capacity': 1.5}
             }

WORLD = {'fields': 100, 'village': {'fields': 100}}

WEAPONS = {'spear': 10, 'sword': 25, 'axe': 40}
SHIELD = {'simple': 10}
ARMOR = {'simple': 10}

TROOPS = \
            {'spear_fighter': {'name': 'spear_fighter', 'cost': {'wood': 50, 'clay': 30, 'iron': 10},
                              'weapons': 'spear', 'shield': 'simple', 'armor': 'simple',
                              'speed': 18, 'cargo_capacity': 25},
            'swordsman': {'name': 'swordsman', 'cost': {'wood': 50, 'clay': 30, 'iron': 10},
                          'weapons': 'spear', 'shield': 'simple', 'armor': 'simple',
                          'speed': 18, 'cargo_capacity': 25},
            'axeman': {'name': 'axeman', 'cost': {'wood': 50, 'clay': 30, 'iron': 10},
                              'weapons': 'spear', 'shield': 'simple', 'armor': 'simple',
                              'speed': 18, 'cargo_capacity': 25},
            'light_cavalry': {'name': 'light_cavalry', 'cost': {'wood': 50, 'clay': 30, 'iron': 10},
                              'weapons': 'spear', 'shield': 'simple', 'armor': 'simple',
                              'speed': 18, 'cargo_capacity': 25},
            'heavy_cavalry': {'name': 'heavy_cavalry', 'cost': {'wood': 50, 'clay': 30, 'iron': 10},
                              'weapons': 'spear', 'shield': 'simple', 'armor': 'simple',
                              'speed': 18, 'cargo_capacity': 25},
            'ram':  {'name': 'ram', 'cost': {'wood': 50, 'clay': 30, 'iron': 10},
                              'weapons': 'spear', 'shield': 'simple', 'armor': 'simple',
                              'speed': 18, 'cargo_capacity': 25},
            'catapult': {'name': 'catapult', 'cost': {'wood': 50, 'clay': 30, 'iron': 10},
                              'weapons': 'spear', 'shield': 'simple', 'armor': 'simple',
                              'speed': 18, 'cargo_capacity': 25},
            'scout':  {'name': 'scout', 'cost': {'wood': 50, 'clay': 30, 'iron': 10},
                              'weapons': 'spear', 'shield': 'simple', 'armor': 'simple',
                              'speed': 18, 'cargo_capacity': 25},
            'noble':  {'name': 'noble', 'cost': {'wood': 50, 'clay': 30, 'iron': 10},
                              'weapons': 'spear', 'shield': 'simple', 'armor': 'simple',
                              'speed': 18, 'cargo_capacity': 25}
            }

N_ROUNDS = 1
DISTANCES = {'ORTHOGONAL': 1, 'DIAGONAL': 1.4}

# Presentation
MENU = ['overview', 'buildings', 'market', 'military',
        'rally_point', 'world', 'tribe']
