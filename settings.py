RESOURCES = {
    "INIT": {
        "WOOD": 50000,
        "CLAY": 50000,
        "IRON": 40000,
    },
    "PRODUCTION": {
        "WOOD": .8,
        "CLAY": .8,
        "IRON": .8,
    },
    "RATIO": 1.5
}

BUILDINGS = {
    "HEADQUARTERS": {
        "NAME": "headquarters",
        "LEVEL": 0,
        "MAX_LEVEL": 30,
        "REQUIREMENTS": {
            "WOOD": 90,
            "CLAY": 80,
            "IRON": 70,
            "TIME": 1,
            "RATIO": 1.26,
        },
        "POPULATION": {
            "BASE": 5,
            "RATIO": 1.155
        },
        "TIME_REDUCE": 1/1.05
    },
    "RALLYPOINT": {
        "NAME": "rally_point",
        "LEVEL": 1,
        "MAX_LEVEL": 1,
        "REQUIREMENTS": {
            "WOOD": 0,
            "CLAY": 0,
            "IRON": 0,
            "TIME": 0,
            "RATIO": 1.26,
        },
        "POPULATION": {
            "BASE": 5,
            "RATIO": 1.155
        },
    },
    "STATUE": {
        "NAME": "statue",
        "LEVEL": 0,
        "MAX_LEVEL": 1,
        "REQUIREMENTS": {
            "WOOD": 220,
            "CLAY": 220,
            "IRON": 220,
            "TIME": 7,
            "RATIO": 1.26,
        },
        "POPULATION": {
            "BASE": 5,
            "RATIO": 1.155
        },
    },
    "TIMBER_CAMP": {
        "NAME": "timber_camp",
        "LEVEL": 0,
        "MAX_LEVEL": 30,
        "REQUIREMENTS": {
            "WOOD": 50,
            "CLAY": 60,
            "IRON": 40,
            "TIME": 6,
            "RATIO": 1.26,
        },
        "POPULATION": {
            "BASE": 5,
            "RATIO": 1.155
        },
        "PRODUCTION": {
            "BASE": 30,
            "RATIO": 1.16
        },
    },
    "CLAY_PIT": {
        "NAME": "clay_pit",
        "LEVEL": 0,
        "MAX_LEVEL": 30,
        "REQUIREMENTS": {
            "WOOD": 65,
            "CLAY": 50,
            "IRON": 40,
            "TIME": 6,
            "RATIO": 1.26,
        },
        "POPULATION": {
            "BASE": 5,
            "RATIO": 1.155
        },
        "PRODUCTION": {
            "BASE": 30,
            "RATIO": 1.16
        }
    },
    "IRON_MINE": {
        "NAME": "iron_mine",
        "LEVEL": 0,
        "MAX_LEVEL": 30,
        "REQUIREMENTS": {
            "WOOD": 75,
            "CLAY": 65,
            "IRON": 70,
            "TIME": 6,
            "RATIO": 1.26,
        },
        "POPULATION": {
            "BASE": 5,
            "RATIO": 1.155
        },
        "PRODUCTION": {
            "BASE": 30,
            "RATIO": 1.16
        }
    },
    "FARM": {
        "NAME": "farm",
        "LEVEL": 1,
        "MAX_LEVEL": 30,
        "REQUIREMENTS": {
            "WOOD": 59,
            "CLAY": 53,
            "IRON": 39,
            "TIME": 1,
            "RATIO": 1.26,
        },
        "POPULATION": {
            "BASE": 0,
            "RATIO": 1.
        },
        "POPULATION_INIT": 240,
        "POPULATION_RATIO": 1.17,
    },
    "WAREHOUSE": {
        "NAME": "warehouse",
        "LEVEL": 1,
        "MAX_LEVEL": 30,
        "REQUIREMENTS": {
            "WOOD": 60,
            "CLAY": 50,
            "IRON": 50,
            "TIME": 1,
            "RATIO": 1.26,
        },
        "POPULATION": {
            "BASE": 0,
            "RATIO": 1.
        },
        "CAPACITY_INIT": 1000,
        "CAPACITY_RATIO": 1.2295,
    },
    "HIDING_PLACE": {
        "NAME": "hiding_place",
        "LEVEL": 0,
        "MAX_LEVEL": 10,
        "REQUIREMENTS": {
            "WOOD": 50,
            "CLAY": 60,
            "IRON": 50,
            "TIME": 1,
            "RATIO": 1.26,
        },
        "POPULATION": {
            "BASE": 2,
            "RATIO": 1.16
        },
        "CAPACITY_INIT": 150,
        "CAPACITY_RATIO": 1.333,
    },
    "BARRACKS": {
        "NAME": "barracks",
        "LEVEL": 0,
        "MAX_LEVEL": 25,
        "REQUIREMENTS": {
            "WOOD": 200,
            "CLAY": 170,
            "IRON": 90,
            "TIME": 1,
            "RATIO": 1.26,
        },
        "POPULATION": {
            "BASE": 7,
            "RATIO": 1.16
        },
        "SPEED_FACTOR_INIT": 0.63,
        "SPEED_FACTOR_RATIO": 0.95,
        "UNLOCK": [
            ["Headquarters", 3]
        ]
    },
    "STABLE": {
        "NAME": "stable",
        "LEVEL": 0,
        "MAX_LEVEL": 20,
        "REQUIREMENTS": {
            "WOOD": 270,
            "CLAY": 240,
            "IRON": 260,
            "TIME": 1,
            "RATIO": 1.26,
        },
        "POPULATION": {
            "BASE": 8,
            "RATIO": 1.16
        },
        "SPEED_FACTOR_INIT": 0.63,
        "SPEED_FACTOR_RATIO": 0.95,
        "UNLOCK": [
            ["Headquarters", 10],
            ["Barracks", 5],
            ["Smithy", 5],
        ]
    },
    "WORKSHOP": {
        "NAME": "workshop",
        "LEVEL": 0,
        "MAX_LEVEL": 15,
        "REQUIREMENTS": {
            "WOOD": 300,
            "CLAY": 240,
            "IRON": 260,
            "TIME": 1,
            "RATIO": 1.26,
        },
        "POPULATION": {
            "BASE": 8,
            "RATIO": 1.16
        },
        "SPEED_FACTOR_INIT": 0.63,
        "SPEED_FACTOR_RATIO": 0.95,
        "UNLOCK": [
            ["Headquarters", 10],
            ["Smithy", 10],
        ]
    },
    "ACADEMY": {
        "NAME": "Academy",
        "LEVEL": 0,
        "MAX_LEVEL": 1,
        "REQUIREMENTS": {
            "WOOD": 15000,
            "CLAY": 25000,
            "IRON": 10000,
            "TIME": 1,
            "RATIO": 1.26,
        },
        "POPULATION": {
            "BASE": 80,
            "RATIO": 1.16
        },
        "SPEED_FACTOR_INIT": 0.63,
        "SPEED_FACTOR_RATIO": 0.95,
        "UNLOCK": [
            ["Headquarters", 20],
            ["Smithy", 20],
            ["Market", 10],
        ]
    },
    "SMITHY": {
        "NAME": "Smithy",
        "LEVEL": 0,
        "MAX_LEVEL": 20,
        "REQUIREMENTS": {
            "WOOD": 220,
            "CLAY": 180,
            "IRON": 240,
            "TIME": 1,
            "RATIO": 1.26,
        },
        "POPULATION": {
            "BASE": 20,
            "RATIO": 1.16
        },
        "SPEED_FACTOR_INIT": 0.91,
        "SPEED_FACTOR_RATIO": 0.912,
        "UNLOCK": [
            ["Headquarters", 5],
            ["Barracks", 1],
        ]
    },
    "MARKET": {
        "NAME": "Market",
        "LEVEL": 0,
        "MAX_LEVEL": 25,
        "REQUIREMENTS": {
            "WOOD": 100,
            "CLAY": 100,
            "IRON": 100,
            "TIME": 1,
            "RATIO": 1.26,
        },
        "POPULATION": {
            "BASE": 20,
            "RATIO": 1.16
        },
        "NUMBER_OF_MERCHANTS_INIT": 1,
        "NUMBER_OF_MERCHANTS_FACTOR": 1.28,
        "UNLOCK": [
            ["Headquarters", 3],
            ["Warehouse", 2],
        ]
    },
    "WALL": {
        "NAME": "Wall",
        "LEVEL": 0,
        "MAX_LEVEL": 20,
        "REQUIREMENTS": {
            "WOOD": 50,
            "CLAY": 100,
            "IRON": 20,
            "TIME": 1,
            "RATIO": 1.26,
        },
        "POPULATION": {
            "BASE": 5,
            "RATIO": 1.16
        },
        "FACTOR_FOR_DEFENDING_TROOPS_INIT": 0.04,
        "FACTOR_FOR_DEFENDING_TROOPS_RATIO": 1.08,
        "UNLOCK": [
            ["Headquarters", 3]
        ]
    },
}