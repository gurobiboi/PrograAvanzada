import os
# KEYS AVAILABLE
ARROW_SIZE = 61
KEYS_AVAILABLE = ["A", "W", "S", "D"""]
KEY_ZONE_LANE_HEIGHT = 130
KEY_ZONE_YLIMIT = 670 + ARROW_SIZE
KEY_ZONE_YSTART = 670
KEY_ZONE_LANES = {"left": 20, "up": 115, "down": 205, "right": 298}
KEY_SPRITE_DIR = ['sprites', 'flechas']
KEY_SPRITES = {
    "left": {"normal": "left_1.png", "x2": "left_3.png", "freeze": "left_4.png", "golden": "left_2.png"},
    "right": {"normal": "right_1.png", "x2": "right_3.png", "freeze": "right_4.png", "golden": "right_2.png"},
    "up": {"normal": "up_1.png", "x2": "up_3.png", "freeze": "up_4.png", "golden": "up_2.png"},
    "down": {"normal": "down_1.png", "x2": "down_3.png", "freeze": "down_4.png", "golden": "down_2.png"}
}

# SONGS DIRECTORY
SONG_MAIN_DIR = "songs"

# PENGU MOVES PATHS
PENGU_COLORS = ["amarillo", "celeste", "morado", "rojo", "verde"]
PENGU_MOVES = ["abajo.png", "abajo_izquierda.png", "abajo_derecha.png",
               "arriba.png", "arriba_izquierda.png", "arriba_derecha.png",
               "izquierda.png", "derecha.png", "tres_flechas.png", "cuatro_flechas.png", "neutro.png"]
PENGU_SPRITES = {}
for color in PENGU_COLORS:
    for move in PENGU_MOVES:
        if move == "abajo.png":
            PENGU_SPRITES[color+','+"down"] = os.path.join(
                "sprites", "pinguirin_" + color, color + "_" + move)
        elif move == "arriba.png":
            PENGU_SPRITES[color+','+"up"] = os.path.join(
                "sprites", "pinguirin_" + color, color + "_" + move)
        elif move == "izquierda.png":
            PENGU_SPRITES[color+','+"left"] = os.path.join(
                "sprites", "pinguirin_" + color, color + "_" + move)
        elif move == "derecha.png":
            PENGU_SPRITES[color+','+"right"] = os.path.join(
                "sprites", "pinguirin_" + color, color + "_" + move)
        elif move == "neutro.png":
            PENGU_SPRITES[color+','+"neutral"] = os.path.join(
                "sprites", "pinguirin_" + color, color + "_" + move)

RANKINGS_NUM = 5

# ARROW PARAMETERS
ARROW_BASE_POINTS = 1
# ARROW TYPE PROBABILITIES
NORMAL_CHANCE = 50
X2_CHANCE = 30
FREEZE_CHANCE = 10
GOLDEN_CHANCE = 10
# AUX TO CALCULATE PROB PROPERLY
NORMAL_PROB = NORMAL_CHANCE
X2_PROB = NORMAL_CHANCE + X2_CHANCE
FREEZE_PROB = NORMAL_CHANCE + X2_CHANCE + FREEZE_CHANCE
GOLDEN_PROB = 100 - GOLDEN_CHANCE

# ARROW SUM ACCORDING TO TYPE
X2_ARROW_VALUE = 2
GOLDEN_ARROW_VALUE = 10


# SONG PARAMETERS
GAME_ZONE_SPEED = {"Principiante": 1000,
                   "Aficionado": 750, "Maestro cumbia": 500}
GAME_ZONE_DURATION = {"Principiante": 20,
                      "Aficionado": 45, "Maestro cumbia": 60}
GAME_MIN_APPROVAL = {"Principiante": 30,
                     "Aficionado": 50, "Maestro cumbia": 70}
DELAY_END_ROUND = 20
ARROW_TRAVEL_TIME = 15
ROUND_POINTS_BASE = 100


# ALLOWED DELAY
Y_DELAY = 50
X_DELAY = 50

# STATS POSITION
COMBO_NUMBER_POS = [230, 20, 41, 31]
MAXCOMBO_NUMBER_POS = [280, 60, 31, 21]
PROGRESS_BAR_POS = [490, 20, 221, 23]
WINPROGRESS_BAR_POS = [490, 60, 221, 23]

# STORE POSITION
CURRENT_BALANCE_POS = [120, 80, 101, 31]

# RANKINGS FILE ROUTE
RANKINGS_FILE_ROUTE = ['backend', 'rankings.txt']
