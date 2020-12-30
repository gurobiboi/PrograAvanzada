import parametros
from menu_principal import MenuInicio
from partida import Partida
from tabla_puntajes import TablaPuntajes


Numero_barcos = parametros.NUM_BARCOS
radio_explosion = parametros.RADIO_EXP

while True:
    tabla_puntajes = TablaPuntajes("puntajes.txt")
    opc = ["Iniciar una Partida", "Ver el Ranking de Puntajes", "Salir"]
    menu_inicio = MenuInicio("Menu de Inicio", opc, tabla_puntajes)

    nuevo_jugador = menu_inicio.input()
    print("\n")
    if nuevo_jugador[0] == 1:
        partida_nueva = Partida(nuevo_jugador[2], nuevo_jugador[3],
                                radio_explosion, Numero_barcos)
        partida_nueva.turno_jugador()
        puntaje_final = partida_nueva.puntaje_final
        tabla_puntajes.agregar(nuevo_jugador[1], puntaje_final)
        print("\n")
