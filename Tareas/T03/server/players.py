
from random import shuffle
from threading import Lock

# Código extraído de AF05 y adaptado para esta tarea

# Cambiar parámetro y ponerlo en parametros.json

PLAYER_NUM = 4


class Player:

    id_ = 0

    def __init__(self, username):
        self.id_player = Player.id_
        self.username = username
        Player.id_ += 1

        # Todos los playeres comienzan como bots, es decir, no tienen socket ni address.
        self.client_socket = None
        self.address = None

    def __repr__(self):
        name = self.username if self.username is not None else "<SIN NOMBRE>"
        return name


def read_names(path):
    """
    Recibe el path del archivo de nombres.
    Retorna una lista con strings correspondientes.
    """
    names_list = []
    with open(path) as archivo:
        names = archivo.readlines()
        for name in names:
            names_list.append(name.strip())
    shuffle(names_list)
    # print(names_list[:PLAYER_NUM])
    return names_list[:PLAYER_NUM]


def create_player_list(nameslist):
    """
    Recibe una lista con strings de nombres
    Retorna una lista con instancias de la clase player.
    """
    players_list = []
    for name in nameslist:
        player = Player(name.strip())
        players_list.append(player)
    # print(players_list)
    return players_list
