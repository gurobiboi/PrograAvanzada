from tableros import tablero_deportistas, tablero_competencia, tablero_delegacion
from dia_competencia import DiaCompetencia
from random import choice
from parametros import DIAS_COMPETENCIA


# La clase campeonato recibe las delegaciones y va creando los días de competencia
# usando la clase DiaCompetencia
class Campeonato:
    def __init__(self, delegacion_usuario, delegacion_rival):
        self.usuario = delegacion_usuario
        self.rival = delegacion_rival
        self.dia_actual = 0
        self.dias_competencia = {}
        self.medallero = {"usuario": self.usuario.medallas, "rival": self.rival.medallas}
    
    # Calcula moral de los equipos
    def moral_equipos(self):
        print(f"Moral del Equipo {self.usuario.nombre}: {self.usuarios.calcular_moral()}\n")
        print(f"Moral del Equipo {self.rival.nombre}: {self.usuarios.rival_moral()}\n")
    
    # Realiza las competencias del dia actual creando instancias de la clase DiaCompetencia
    # Para esto pide primero los competidores del usuario y usa random para el oponente
    def realizar_competencias(self):
        print("Llegó la hora de elegir a los competidores! \n")
        tablero_deportistas(self.usuario.equipo)

        usuario_atl, usuario_cicl, usuario_gimn, usuario_nata = None, None, None, None
        while usuario_atl not in self.usuario.equipo:
            usuario_atl = input("Escriba el nombre de su deportista para Atletismo: ")

        tablero_deportistas(self.usuario.equipo)
        while usuario_cicl not in self.usuario.equipo:
            usuario_cicl = input("Escriba el nombre su deportista para Ciclismo: ")

        tablero_deportistas(self.usuario.equipo)
        while usuario_gimn not in self.usuario.equipo:
            usuario_gimn = input("Seleccione a su deportista para Gimnasia: ")

        tablero_deportistas(self.usuario.equipo)
        while usuario_nata not in self.usuario.equipo:
            usuario_nata = input("Seleccione a su deportista para Natacion: ")
        
        usuario_competidores = {"atletismo": self.usuario.equipo[usuario_atl],
                                "ciclismo": self.usuario.equipo[usuario_cicl],
                                "gimnasia": self.usuario.equipo[usuario_gimn],
                                "natacion": self.usuario.equipo[usuario_nata]}

        rival_competidores = {"atletismo": choice(list(self.rival.equipo.values())),
                              "ciclismo": choice(list(self.rival.equipo.values())),
                              "gimnasia": choice(list(self.rival.equipo.values())),
                              "natacion": choice(list(self.rival.equipo.values()))}

        self.dias_competencia[self.dia_actual] = DiaCompetencia(self.dia_actual, usuario_competidores,
                                                                rival_competidores,
                                                                [self.usuario,
                                                                self.rival])
        self.dia_actual += 1
        if self.dia_actual >= DIAS_COMPETENCIA/2:
            self.terminar_campeonato()

    # Muestra el estado actual del campeonato, delegaciones y medallero
    def mostrar_estado(self):
        print("\n")
        tablero_delegacion(self.usuario)
        tablero_deportistas(self.usuario.equipo)
        print("*"*100)
        print("*"*100)
        tablero_delegacion(self.rival)
        tablero_deportistas(self.rival.equipo)
        print("*"*100)
        print("*"*100)
        print("\n")

    # Termina el campeonato cuando se llega al último dia
    # Felicita al competidor ganador
    def terminar_campeonato(self):
        print("\nHa terminado el última día de competencias!\n")
        total_medallas_usuario = 0
        total_medallas_rival = 0
        for deporte in self.medallero["usuario"]:
            total_medallas_usuario += self.medallero["usuario"][deporte]
        for deporte in self.medallero["rival"]:
            total_medallas_rival += self.medallero["rival"][deporte]
        if total_medallas_usuario > total_medallas_rival:
            print(f"\n HA GANADO {self.usuario.nombre}, DIRIGIDO POR {self.usuario.entrenador} !!!!!!!\n")
        elif total_medallas_usuario < total_medallas_rival:
            print(f"\n HA GANADO {self.rival.nombre}, DIRIGIDO POR {self.rival.entrenador}  !!!!!!!\n")
        else:
            print("Se declara un empate!")
        