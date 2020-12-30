from tablero import print_tablero
from random import randint


class Partida:

    def __init__(self, N, M, radio_exp, num_barcos):
        self.tablero_jugador = [[" "]*M for _ in range(N)]
        self.tablero_enemigo = [[" "]*M for _ in range(N)]
        self.coordenadas_dict = {}
        for columna in range(0, len(self.tablero_jugador[0])):
            abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            self.coordenadas_dict[abc[columna]] = columna
        self.barcos_jugador = num_barcos
        self.barcos_enemigo = num_barcos
        self.max_num = num_barcos
        self.bomba_cruz, self.bomba_X, self.bomba_Diamante = 1, 1, 1
        self.radio_explosion = radio_exp
        self.asignar_barcos(num_barcos, N, M)
        self.puntaje_final = 0

    def asignar_barcos(self, num_barcos, N, M):
        self.barcos_jugador = 0
        self.barcos_enemigo = 0
        while self.barcos_jugador < num_barcos:
            x, y = randint(0, N-1), randint(0, M-1)
            if self.tablero_jugador[x][y] == " ":
                self.tablero_jugador[x][y] = 'B'
                self.barcos_jugador += 1
        while self.barcos_enemigo < num_barcos:
            x, y = randint(0, N-1), randint(0, M-1)
            if self.tablero_enemigo[x][y] == " ":
                self.tablero_enemigo[x][y] = 'B'
                self.barcos_enemigo += 1

    def ver_tablero(self, bombas_disponibles=False):
        print_tablero(self.tablero_enemigo, self.tablero_jugador)
        if bombas_disponibles is True:
            print(f"\nTienes {self.bomba_cruz}",
                  f"Bomba Cruz Disponible \nTienes {self.bomba_X}",
                  f"Bomba X Disponible \nTienes {self.bomba_Diamante}",
                  "Bomba Diamante Disponible\n")
        # Sacar esto alfinal
        # print(self.tablero_jugador, self.tablero_enemigo)

    def introducir_coordenada(self):
        coord_X, coord_Y, Y = 1000, 1000, 1000
        print("\nSe lanzara una bomba, APUNTA!\n")
        self.ver_tablero(False)
        while not (0 <= int(coord_X) <= len(self.tablero_enemigo)-1 and
                   Y.upper() in self.coordenadas_dict):
            Y = input("Inserte la columna de ataque como una letra: ")
            coord_Y = self.coordenadas_dict.get(Y.upper(), 1000)
            coord_X = input("Inserte la fila de ataque: ")
            while not coord_X.isnumeric():
                print("Ingrese un número")
                coord_X = input("Inserte la fila de ataque: ")
            if not (0 <= int(coord_X) <= len(self.tablero_enemigo)-1 and
                    coord_Y <= len(self.tablero_enemigo[0])-1):
                print("Coordenada Inválida, intente nuevamente")
        if self.tablero_enemigo[int(coord_X)][coord_Y] == " " or \
           self.tablero_enemigo[int(coord_X)][coord_Y] == "B":
            print(f"Se lanzo una bomba en la coordenada {Y.upper(), coord_X}")
            return [coord_Y, int(coord_X)]
        else:
            print("La coordenada elegida ya se encuentra" +
                  " descubierta, debe ingresar una coordenada nueva!")
            return self.introducir_coordenada()

    def explosion_bomba(self, Y, X, tipobomba):
        barcos_hundidos = 0
        coord = []
        print(f"Se explota la bomba {tipobomba} !")
        if tipobomba == "Regular":
            coord.append([X, Y])
        elif tipobomba == "Cruz":
            for i in range(max(0, X-self.radio_explosion+1),
                           min(len(self.tablero_enemigo),
                               X + self.radio_explosion)):
                coord.append([i, Y])
            for j in range(max(0, Y-self.radio_explosion+1),
                           min(len(self.tablero_enemigo[X]),
                               Y + self.radio_explosion)):
                coord.append([X, j])
            self.bomba_cruz = 0
        elif tipobomba == "X":
            for i in range(max(0, X-self.radio_explosion+1),
                           min(len(self.tablero_enemigo),
                               X+self.radio_explosion)):
                if 0 <= Y + X - i <= len(self.tablero_enemigo[0])-1:
                    coord.append([i, Y + X - i])
                if 0 <= Y - X + i <= len(self.tablero_enemigo[0])-1:
                    coord.append([i, Y - X + i])
            self.bomba_X = 0
        elif tipobomba == "Diamante":
            for i in range(max(0, X-self.radio_explosion+1),
                           min(len(self.tablero_enemigo),
                               X+self.radio_explosion)):
                coord.append([i, Y])
            for j in range(max(0, Y-self.radio_explosion+1),
                           min(len(self.tablero_enemigo[X]),
                               Y + self.radio_explosion)):
                coord.append([X, j])
            for i in range(max(0, X-self.radio_explosion+2),
                           min(len(self.tablero_enemigo),
                               X+self.radio_explosion-1)):
                if 0 <= Y + X - i <= len(self.tablero_enemigo[0])-1:
                    coord.append([i, Y + X - i])
                if 0 <= Y - X + i <= len(self.tablero_enemigo[0])-1:
                    coord.append([i, Y - X + i])
            self.bomba_Diamante = 0
        for par in coord:
            if self.tablero_enemigo[par[0]][par[1]] == "B":
                self.tablero_enemigo[par[0]][par[1]] = \
                    self.tablero_enemigo[par[0]][par[1]].replace("B", "F")
                barcos_hundidos += 1
            else:
                self.tablero_enemigo[par[0]][par[1]] = \
                    self.tablero_enemigo[par[0]][par[1]].replace(" ", "X")
        self.barcos_enemigo -= barcos_hundidos
        self.ver_tablero(False)
        print(f"Has hundido {barcos_hundidos} barco(s) enemigos,"
              + f" le quedan {self.barcos_enemigo} barco(s) al enemigo!")
        if barcos_hundidos > 0 and self.barcos_enemigo > 0:
            print("Puedes lanzar nuevamente! \n")
            self.lanzar_bomba()

    def turno_jugador(self):
        while self.barcos_jugador and self.barcos_enemigo > 0:
            seleccion = 0
            print("-- Menu de Juego --")
            self.ver_tablero(False)
            print("[1] Rendirse \n[2] Lanzar Bomba\n[3] Salir del Programa\n")
            while seleccion not in ["1", "2", "3"]:
                seleccion = input("Ingresa tu seleccion: ")
                if seleccion not in ["1", "2", "3"]:
                    print("Opción inválida, intente nuevamente")
            if seleccion == "2":
                self.lanzar_bomba()
                if self.barcos_enemigo > 0:
                    self.turno_oponente()
            elif seleccion == "1":
                print("Te has rendido!\n")
                self.barcos_jugador = 0
            else:
                print("Adios, hasta la proxima!")
                quit()
        if self.barcos_jugador == 0:
            self.terminar_partida("Oponente")
        else:
            self.terminar_partida("Jugador")

    def terminar_partida(self, ganador):
        if ganador == "Oponente":
            print("Has perdido la partida :(.")
            print("Mejor suerte para la próxima!\n")
        if ganador == "Jugador":
            print("\nFelicitaciones, has ganado !!!!\n")
        enemigos_desc = 0
        aliados_desc = 0
        for fila in self.tablero_enemigo:
            enemigos_desc += fila.count("F")
        for fila in self.tablero_jugador:
            aliados_desc += fila.count("F")
        filasp = len(self.tablero_jugador)
        colp = len(self.tablero_jugador[0])
        self.puntaje_final = max(0, (filasp*colp*self.max_num*(enemigos_desc -
                                                               aliados_desc)))

    def lanzar_bomba(self):
        bomba_seleccionada = None
        alternativa_valida = 0
        self.ver_tablero(True)
        while alternativa_valida == 0:
            print("Que tipo de bomba desea lanzar?\n")
            print("[1] Bomba Regular\n[2] Bomba Cruz",
                  "\n[3] Bomba X \n[4] Bomba Diamante\n")

            bomba_seleccionada = input("Selecciona una opción: ")
            if bomba_seleccionada == "1":
                alternativa_valida = 1
                coordXY = self.introducir_coordenada()
                self.explosion_bomba(coordXY[0], coordXY[1], "Regular")
            elif bomba_seleccionada == "2" and self.bomba_cruz == 1:
                alternativa_valida = 1
                coordXY = self.introducir_coordenada()
                self.explosion_bomba(coordXY[0], coordXY[1], "Cruz")
            elif bomba_seleccionada == "3" and self.bomba_X == 1:
                alternativa_valida = 1
                coordXY = self.introducir_coordenada()
                self.explosion_bomba(coordXY[0], coordXY[1], "X")
            elif bomba_seleccionada == "4" and self.bomba_Diamante == 1:
                alternativa_valida = 1
                coordXY = self.introducir_coordenada()
                self.explosion_bomba(coordXY[0], coordXY[1], "Diamante")
            else:
                print("Se ha seleccionado una opción inválida o una bomba ",
                      "especial sin municion, inserte una opcion valida")

    def turno_oponente(self):
        print("\nTurno del oponente!")
        coordenada_valida = 0
        barcos_hundidos = 0
        if self.barcos_enemigo > 0:
            while coordenada_valida != 1:
                x = randint(0, len(self.tablero_jugador)-1)
                y = randint(0, len(self.tablero_jugador[0])-1)
                if self.tablero_jugador[x][y] == " ":
                    self.tablero_jugador[x][y] = \
                    self.tablero_jugador[x][y].replace(" ", "X")
                    coordenada_valida = 1
                elif self.tablero_jugador[x][y] == "B":
                    self.tablero_jugador[x][y] = \
                    self.tablero_jugador[x][y].replace("B", "F")
                    barcos_hundidos = 1
                    coordenada_valida = 1
        self.barcos_jugador -= barcos_hundidos
        if barcos_hundidos == 1:
            print("El oponente ha hundido uno de tus barcos, " +
                  f"te quedan {self.barcos_jugador} barco(s) vivo(s)1!")
            if self.barcos_jugador > 0:
                print("Oponente lanza nuevamente !\n")
                self.turno_oponente()
        else:
            print("El oponente ha fallado, que suerte!")


if __name__ == "__main__":
    partida_nueva = Partida(3, 3, 3, 1)
    # partida_nueva.asignar_barcos(3, 5, 4)

    partida_nueva.turno_jugador()
    # Falta:
    # Evite hacer daño en lugares fuera de la lista
    # Hacer daño sobre lugar afectado
    # turno oponente
    # Dar score cuando se termine la partida
