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
}