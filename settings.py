from collections import OrderedDict

WHITE = (1, 1, 1, 1)
BLACK = (0, 0, 0, 1)


RESOURCES = {
    "INIT": {
        "WOOD": 5000,
        "CLAY": 5000,
        "IRON": 5000,
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
    },
    "MENUS": {
        "HEADER": [0.4, 0.25, 0.35],
        "CONTENT": [0.1, 0.3, 0.25, 0.35]
    }
}

BUILDINGS = {
    "HEADQUARTERS": {
        "NAME": "headquarters",
        "ICON": "img/Buildings/Main1.png",
        "LEVEL": 4,
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
        "TIME_REDUCE": 1/1.05,
        "MENUS": {
            "TIME": [0.25, 0.25, 0.25, 0.25],
            "AVAILABLES": [0.25, 0.12, 0.12, 0.12, 0.12, 0.12, 0.15],
            "UNAVAILABLES": [0.25, 0.75]
        },
        "DESCRIPTION": """
        In the Headquarters you can construct new buildings or upgrade existing ones.
        The higher the level of your Headquarters,
        the faster the constructions will be finished.
        As soon as your Headquarters is upgraded to level 15,
        you will be able to demolish buildings in this village
        (requires 100% loyalty).
        """
    },
    "RALLY_POINT": {
        "NAME": "rally_point",
        "ICON": "img/Buildings/Place1.png",
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
        "DESCRIPTION": """
        On the rally point your fighters meet.
        Here you can command your armies.""",
        "SCAVENGING": {
            "DESCRIPTION": """
            Send your troops away to scavenge for resources surrounding your village.
            The units will return when they collect enough resources -
            but have in mind once you send the troops away you can't recall them.
            """,
            "LOCK_ICON": "img/Scavenging/lock.png",
            "POSSIBLE_UNITS": [
                "spear_fighter", "swordsman", "axeman", "archer",
                "light_cavalry", "mounted_archer", "heavy_cavalry", "paladin"],
            "ALL": OrderedDict({
                "Lackadaisical Looters": {
                    "wood": 25,
                    "clay": 30,
                    "iron": 25,
                    "time": 30,
                    "icon": "img/Scavenging/lackadaisical_looters.png",
                    "icon_gray": "img/Scavenging/lackadaisical_looters_gray.png",
                    "loot_factor": 0.1
                },
                "Humble Haulers": {
                    "wood": 250,
                    "clay": 300,
                    "iron": 250,
                    "time": 3600,
                    "icon": "img/Scavenging/humble_haulers.png",
                    "icon_gray": "img/Scavenging/humble_haulers_gray.png",
                    "loot_factor": 0.25
                },
                "Clever Collectors": {
                    "wood": 1000,
                    "clay": 1200,
                    "iron": 1000,
                    "time": 3600*3,
                    "icon": "img/Scavenging/clever_collectors.png",
                    "icon_gray": "img/Scavenging/clever_collectors_gray.png",
                    "loot_factor": 0.5
                },
                "Great Gatherers": {
                    "wood": 10000,
                    "clay": 12000,
                    "iron": 10000,
                    "time": 3600*6,
                    "icon": "img/Scavenging/great_gatherers.png",
                    "icon_gray": "img/Scavenging/great_gatherers_gray.png",
                    "loot_factor": 0.75
                }
            })
        }
    },
    "STATUE": {
        "NAME": "statue",
        "ICON": "img/Buildings/Statue1.png",
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
        "ICON": "img/Buildings/Wood1.png",
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
        "DESCRIPTION": """
        Outside of your village in the dark forests
        your lumberjacks cut massive trees to produce wood in the timber camp,
        which is needed for buildings and weapons.
        The higher its level the more wood is produced."""
    },
    "CLAY_PIT": {
        "NAME": "clay_pit",
        "ICON": "img/Buildings/Stone1.png",
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
        },
        "DESCRIPTION": """
        In the clay pit your workers extract clay,
        which is important for new buildings.
        The higher its level the more clay is produced."""
    },
    "IRON_MINE": {
        "NAME": "iron_mine",
        "ICON": "img/Buildings/Iron1.png",
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
        },
        "DESCRIPTION": "In the iron mine your workers dig the war-crucial iron.\nThe higher its level the more iron is produced."
    },
    "FARM": {
        "NAME": "farm",
        "ICON": "img/Buildings/Farm1.png",
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
        "ICON": "img/Buildings/Storage1.png",
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
        "CAPACITY_INIT": 10000,
        "CAPACITY_RATIO": 1.2295,
    },
    "HIDING_PLACE": {
        "NAME": "hiding_place",
        "ICON": "img/Buildings/Hide1.png",
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
        "ICON": "img/Buildings/Barracks1.png",
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
        "UNITS": ["spear_fighter", "swordsman", "axeman", "archer"],
        "DESCRIPTION": "In the barracks you can recruit infantry.\nThe higher its level the faster the recruitment of troops will be finished."
    },
    "STABLE": {
        "NAME": "stable",
        "ICON": "img/Buildings/Stable1.png",
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
            ["headquarters", 2],
            ["barracks", 5],
            ["smithy", 5],
        ]
    },
    "WORKSHOP": {
        "NAME": "workshop",
        "ICON": "img/Buildings/Garage1.png",
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
        "ICON": "img/Buildings/Snob1.png",
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
        "ICON": "img/Buildings/Smith1.png",
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
        "ICON": "img/Buildings/Market1.png",
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
        "ICON": "img/Buildings/Wall1.png",
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
            ["barracks", 1]
        ]
    },
}

UNITS = {
    "SPEAR_FIGHTER": {
        "NAME": "spear_fighter",
        "ICON": "img/Units/Icon/unit_spear.png",
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
        "ICON": "img/Units/Icon/unit_sword.png",
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
        "ICON": "img/Units/Icon/unit_axe.png",
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
        "ICON": "img/Units/Icon/unit_archer.png",
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
        "ICON": "img/Units/Icon/unit_spy.png",
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
        "ICON": "img/Units/Icon/unit_light.png",
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
        "ICON": "img/Units/Icon/unit_marcher.png",
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
        "ICON": "img/Units/Icon/unit_heavy.png",
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
        "ICON": "img/Units/Icon/unit_ram.png",
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
        "ICON": "img/Units/Icon/unit_catapult.png",
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
        "ICON": "img/Units/Icon/unit_knight.png",
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
        "ICON": "img/Units/Icon/unit_snob.png",
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
        "ICON": "img/Units/Icon/unit_militia.png",
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
