WHITE = (1, 1, 1, 1)
BLACK = (0, 0, 0, 1)

RESOURCES = {
    "INIT": {
        "WOOD": 500,
        "CLAY": 500,
        "IRON": 400,
    },
    "PRODUCTION": {
        "WOOD": .8,
        "CLAY": .8,
        "IRON": .8,
    },
    "RATIO": 1.5,
    "ICON": {
        "WOOD": "img/wood.png",
        "CLAY": "img/Clay.png",
        "IRON": "img/iron.png",
        "BOOTY": "img/Booty.png",
        "POPULATION": "img/Pop.png",
        "TIME": ""
    }
}

BUILDINGS = {
    "HEADQUARTERS": {
        "NAME": "headquarters",
        "ICON": "",
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
    "RALLY_POINT": {
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
            ["headquarters", 3]
        ],
        "UNITS": ["spear_fighter", "swordsman", "axeman", "archer"]
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
            ["headquarters", 10],
            ["barracks", 5],
            ["smithy", 5],
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

UNITS = {
    "SPEAR_FIGHTER": {
        "NAME": "spear_fighter",
        "ICON": "img/Unit_spear_60.png",
        "TYPE": "general",
        "REQUIREMENTS": {
            "WOOD": 50,
            "CLAY": 30,
            "IRON": 10,
            "POPULATION": 1,
            "UNLOCK": [
                ["barracks", 1]
            ]
        },
        "ATK": 10,
        "DEFENCE": {
            "GENERAL": 15,
            "CAVALRY": 45,
            "ARCHER": 20
        },
        "SPEED": 18,
        "CAPACITY": 25
    },
    "SWORDSMAN": {
        "NAME": "swordsman",
        "ICON": "img/Unit_sword_60.png",
        "TYPE": "general",
        "REQUIREMENTS": {
            "WOOD": 30,
            "CLAY": 30,
            "IRON": 70,
            "POPULATION": 1,
            "UNLOCK": [
                ["smithy", 1]
            ]
        },
        "ATK": 25,
        "DEFENCE": {
            "GENERAL": 50,
            "CAVALRY": 15,
            "ARCHER": 40
        },
        "SPEED": 22,
        "CAPACITY": 15
    },
    "AXEMAN": {
        "NAME": "axeman",
        "ICON": "img/Unit_axe_60.png",
        "TYPE": "general",
        "REQUIREMENTS": {
            "WOOD": 60,
            "CLAY": 30,
            "IRON": 40,
            "POPULATION": 1,
            "UNLOCK": [
                ["smithy", 2]
            ]
        },
        "ATK": 40,
        "DEFENCE": {
            "GENERAL": 10,
            "CAVALRY": 5,
            "ARCHER": 10
        },
        "SPEED": 18,
        "CAPACITY": 10
    },
    "ARCHER": {
        "NAME": "archer",
        "ICON": "img/Unit_archer_60.png",
        "TYPE": "archer",
        "REQUIREMENTS": {
            "WOOD": 100,
            "CLAY": 30,
            "IRON": 60,
            "POPULATION": 1,
            "UNLOCK": [
                ["barracks", 5],
                ["smithy", 5]
            ]
        },
        "ATK": 15,
        "DEFENCE": {
            "GENERAL": 50,
            "CAVALRY": 40,
            "ARCHER": 5
        },
        "SPEED": 18,
        "CAPACITY": 10
    },
    "SCOUT": {
        "NAME": "scout",
        "TYPE": "cavalry",
        "REQUIREMENTS": {
            "WOOD": 50,
            "CLAY": 50,
            "IRON": 20,
            "POPULATION": 2,
            "UNLOCK": [
                ["stable", 1]
            ]
        },
        "ATK": 0,
        "DEFENCE": {
            "GENERAL": 2,
            "CAVALRY": 1,
            "ARCHER": 2
        },
        "SPEED": 9,
        "CAPACITY": 0,
        "SPECIAL_ABILITIES": [
            "When attacking, can only be caught by other scouts.",
            "After attacking, reveals extra information in the battle report."
        ]
    },
    "LIGHT_CAVALRY": {
        "NAME": "light_cavalry",
        "TYPE": "cavalry",
        "REQUIREMENTS": {
            "WOOD": 125,
            "CLAY": 100,
            "IRON": 250,
            "POPULATION": 4,
            "UNLOCK": [
                ["stable", 3]
            ],
            "RESEARCH": {
                "WOOD": 2200,
                "CLAY": 2400,
                "IRON": 2000,
            }
        },
        "ATK": 130,
        "DEFENCE": {
            "GENERAL": 30,
            "CAVALRY": 40,
            "ARCHER": 30
        },
        "SPEED": 10,
        "CAPACITY": 80
    },
    "MOUNTED_ARCHER": {
        "NAME": "mounted_archer",
        "TYPE": "archer",
        "REQUIREMENTS": {
            "WOOD": 250,
            "CLAY": 100,
            "IRON": 150,
            "POPULATION": 5,
            "UNLOCK": [
                ["stable", 5]
            ],
            "RESEARCH": {
                "WOOD": 3000,
                "CLAY": 2400,
                "IRON": 2000,
            }
        },
        "ATK": 100,
        "DEFENCE": {
            "GENERAL": 40,
            "CAVALRY": 30,
            "ARCHER": 50
        },
        "SPEED": 10,
        "CAPACITY": 50
    },
    "HEAVY_CAVALRY": {
        "NAME": "heavy_cavalry",
        "TYPE": "cavalry",
        "REQUIREMENTS": {
            "WOOD": 200,
            "CLAY": 150,
            "IRON": 600,
            "POPULATION": 6,
            "UNLOCK": [
                ["stable", 10],
                ["smithy", 15]
            ],
            "RESEARCH": {
                "WOOD": 3000,
                "CLAY": 2400,
                "IRON": 2000,
            }
        },
        "ATK": 150,
        "DEFENCE": {
            "GENERAL": 200,
            "CAVALRY": 80,
            "ARCHER": 180
        },
        "SPEED": 11,
        "CAPACITY": 50
    },
    "RAM": {
        "NAME": "ram",
        "TYPE": "general",
        "REQUIREMENTS": {
            "WOOD": 300,
            "CLAY": 200,
            "IRON": 200,
            "POPULATION": 5,
            "UNLOCK": [
                ["workshop", 1]
            ],
            "RESEARCH": {
                "WOOD": 1200,
                "CLAY": 1600,
                "IRON": 800,
            }
        },
        "ATK": 2,
        "DEFENCE": {
            "GENERAL": 20,
            "CAVALRY": 50,
            "ARCHER": 20
        },
        "SPEED": 30,
        "CAPACITY": 0,
        "SPECIAL_ABILITIES": [
            "Damages Walls and reduces their effects in battle."
        ]
    },
    "CATAPULT": {
        "NAME": "catapult",
        "TYPE": "general",
        "REQUIREMENTS": {
            "WOOD": 320,
            "CLAY": 400,
            "IRON": 100,
            "POPULATION": 8,
            "UNLOCK": [
                ["workshop", 2],
                ["Smithy", 12]
            ],
            "RESEARCH": {
                "WOOD": 1600,
                "CLAY": 2000,
                "IRON": 1200,
            }
        },
        "ATK": 100,
        "DEFENCE": {
            "GENERAL": 100,
            "CAVALRY": 50,
            "ARCHER": 100
        },
        "SPEED": 30,
        "CAPACITY": 0,
        "SPECIAL_ABILITIES": [
            "Damages selected enemy building."
        ]
    },
    "PALADIN": {
        "NAME": "paladin",
        "TYPE": "cavalry",
        "REQUIREMENTS": {
            "WOOD": 20,
            "CLAY": 20,
            "IRON": 40,
            "POPULATION": 10,
            "UNLOCK": [
                ["statue", 1]
            ],
        },
        "ATK": 150,
        "DEFENCE": {
            "GENERAL": 250,
            "CAVALRY": 400,
            "ARCHER": 150
        },
        "SPEED": 10,
        "CAPACITY": 100,
        "SPECIAL_ABILITIES": [
            "Can learn different skills.",
            "Can earn experience and gain levels.",
            "Possible to recruit more paladins by conquering other villages.",
            "Units travelling with the Paladin as support, travel at the Paladin's speed."
        ]
    },
    "NOBLE": {
        "NAME": "noble",
        "TYPE": "general",
        "REQUIREMENTS": {
            "WOOD": 40000,
            "CLAY": 50000,
            "IRON": 50000,
            "POPULATION": 100,
            "UNLOCK": [
                ["academy", 1],
                ["headquarters", 20],
                ["smithy", 20],
                ["market", 10]
            ],
        },
        "ATK": 30,
        "DEFENCE": {
            "GENERAL": 100,
            "CAVALRY": 50,
            "ARCHER": 100
        },
        "SPEED": 35,
        "CAPACITY": 0,
        "SPECIAL_ABILITIES": [
            "Reduces attacked village's loyalty by 20 to 35 points."
        ]
    },
    "MILITIA": {
        "NAME": "militia",
        "TYPE": "general",
        "REQUIREMENTS": {
            "WOOD": 0,
            "CLAY": 0,
            "IRON": 0,
            "POPULATION": 0,
        },
        "ATK": 0,
        "DEFENCE": {
            "GENERAL": 15,
            "CAVALRY": 45,
            "ARCHER": 25
        },
        "SPEED": 0,
        "CAPACITY": 0
    },

}
