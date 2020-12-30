from abc import ABC, abstractmethod
from campeonato import Campeonato
from delegacion import Delegacion, DelegacionDCCrotona, DelegacionIEEEsparta
from parametros import DIAS_COMPETENCIA


# Clase abstracta del menu. Recibe opciones y tiene
# métodos que las permite visualizar
class Menu(ABC):

    def __init__(self, opciones, volver=True):
        self.opciones = {}
        self.numero_opciones = 0
        for opcion in opciones:
            self.numero_opciones += 1
            self.opciones[str(self.numero_opciones)] = opcion

        if volver:
            self.numero_opciones += 1
            self.opciones[str(self.numero_opciones)] = "Volver atrás"

        self.numero_opciones += 1
        self.opciones[str(self.numero_opciones)] = "Salir del Programa"

    def volver(self):
        pass

    @abstractmethod
    def eleccion(self):
        pass

    def Salir(self):
        print("Ha seleccionado salir del programa, adiós!")
        quit()

    def mostrar_menu(self):
        for opcion in self.opciones:
            print(f" [{opcion}] {self.opciones[opcion]} \n")


# recibe deportistas disponibles y los parametros de las delegaciones
# método eleccion dice que hacer al elegir cada opción
class MenuInicio(Menu):

    def __init__(self, deportistas_disp, DCC, IEE,
                 volver=False, opciones=["Comenzar Nueva Partida"]):
        super().__init__(opciones, volver=False)
        self.menu_principal = None
        self.deportistas = deportistas_disp
        self.equipo_DCC = DCC[0]
        self.moral_DCC = DCC[1]
        self.dinero_DCC = DCC[2]
        self.equipo_IEE = IEE[0]
        self.moral_IEE = IEE[1]
        self.dinero_IEE = IEE[2]


    def eleccion(self):
        self.mostrar_menu()
        alternativa = input("Seleccione el número de la acción que desea realizar: ")
        while alternativa not in self.opciones:
            print("Alternativa incorrecta, seleccione nuevamente")
            self.mostrar_menu()
            alternativa = input("Seleccione el número de la acción que desea realizar: ")
        if alternativa == "1":
            self.comenzar_partida()
        else:
            self.Salir()

    # Comienza partida en caso de que jugador lo desee.
    # Pide nombre y delegacion a usar
    # Crea instancias de las delegaciones iniciales
    # Crea instancia del campeonato
    # Crea instancia de menu principal
    # El menu itera hasta que jugador ya no quiera seguir jugando
    def comenzar_partida(self):
        while True:
            nombre_usuario = input("Introduzca su nombre para el juego: ")

            while not (nombre_usuario.isalnum()):
                print("Debe seleccionar sólo números y/o letras!")
                nombre_usuario = input("Introduzca su nombre para el juego: ")

            nombre_rival = input("Introduzca el nombre de su rival para el juego: ")

            while not (nombre_usuario.isalnum()):
                print("Debe seleccionar sólo números y/o letras!")
                nombre_usuario = input("Introduzca el nombre de su rival para el juego: ")

            print("Existen 2 delegaciones: IEEEsparta y DCCrotona")
            delegacion_usuario = input("Porfavor, seleccione con cual delegación quiere competir: ")
            while delegacion_usuario.upper() != "IEEESPARTA" and \
            delegacion_usuario.upper() != "DCCROTONA":
                print("Opción inválida!")
                print("Existen 2 delegaciones: IEEEsparta y DCCrotona")
                delegacion_usuario = input("Porfavor, seleccione con cual delegación quiere competir: ")

            if delegacion_usuario.upper() == "IEEESPARTA":
                usuario_del = DelegacionIEEEsparta(nombre_usuario, self.equipo_IEE, self.moral_IEE,
                                                   self.dinero_IEE)
                rival_del = DelegacionDCCrotona(nombre_rival, self.equipo_DCC,
                                                self.moral_DCC, self.dinero_DCC )
                olimpiada = Campeonato(usuario_del, rival_del)

            elif delegacion_usuario.upper() == "DCCROTONA":
                usuario_del = DelegacionDCCrotona(nombre_usuario, self.equipo_DCC,
                                                  self.moral_DCC, self.dinero_DCC )
                rival_del = DelegacionIEEEsparta(nombre_rival, self.equipo_IEE,
                                                 self.moral_IEE, self.dinero_IEE) 
                olimpiada = Campeonato(usuario_del, rival_del)

            self.menu_principal = MenuPrincipal(olimpiada, self.deportistas)
            self.menu_principal.eleccion()

            seguir = input("Desea seguir jugando (Si/no)?: ")
            while seguir.upper() != "SI" and seguir.upper() != "NO":
                print("Opcion invalida, escriba si o no")
                seguir = input("Desea seguir jugando (Si/no)?: ")
            if seguir.upper() == "NO":
                self.Salir()


# Menu principal al estar ya dentro de una partida.
# Recibe instancia de campeonato y deportistas disponibles
# Menu itera hasta que campeonato termine
class MenuPrincipal(Menu):

    def __init__(self, campeonato, deportistas_disp, opciones=["Menu Entrenador",
                 "Simular competencias", "Mostrar Estado"], volver=False):
        super().__init__(opciones, volver=False)
        self.campeonato = campeonato
        self.deportistas_disp = deportistas_disp
        self.menu_entrenador = MenuEntrenador(campeonato.usuario, self.deportistas_disp)

    # Dice que hacer en caso de cada opción elegida
    # Va mostrando Día, moral de equipo
    def eleccion(self):
        while self.campeonato.dia_actual < DIAS_COMPETENCIA/2:
            print(f"\nDia Actual: {self.campeonato.dia_actual * 2 + 1}\n")
            print(f"Moral Equipo {self.campeonato.usuario.nombre}: {self.campeonato.usuario.calcular_moral()}")
            print(f"Moral Equipo {self.campeonato.rival.nombre}: {self.campeonato.rival.calcular_moral()}\n")
            self.mostrar_menu()
            alternativa = input("Seleccione el número de la acción que desea realizar: ")
            while alternativa not in self.opciones:
                print("Alternativa incorrecta, seleccione nuevamente")
                self.mostrar_menu()
                alternativa = input("Seleccione el número de la acción que desea realizar: ")
            if alternativa == "1":
                self.menu_entrenador.eleccion()
            elif alternativa == "2":
                print(f"\nDia Actual: {self.campeonato.dia_actual * 2 + 2}\n")
                print(f"Moral Equipo {self.campeonato.usuario.nombre}: {self.campeonato.usuario.calcular_moral()}")
                print(f"Moral Equipo {self.campeonato.rival.nombre}: {self.campeonato.rival.calcular_moral()}\n")
                self.campeonato.realizar_competencias()
            elif alternativa == "3":
                self.campeonato.mostrar_estado()
            else:
                self.Salir()


# Menu entrenador. Da opciones como fichar, sanar, entrenar, entre otros.
# Recibe delegación y lista de deportistas disponibles
# Para cada acción llama a la clase delegación
class MenuEntrenador(Menu):

    def __init__(self, delegacion, deportistas_disp, volver=False, 
                 opciones=["Fichar", "Entrenar", "Sanar",
                           "Comprar Tecnología", "Usar habilidad especial"]):
        super().__init__(opciones, volver=True)
        self.delegacion = delegacion
        self.deportistas_disp = deportistas_disp

    def eleccion(self):
        while True:
            self.mostrar_menu()
            alternativa = input("Seleccione el número de la acción que desea realizar: ")
            while alternativa not in self.opciones:
                print("Alternativa incorrecta, seleccione nuevamente")
                self.mostrar_menu()
                alternativa = input("Seleccione el número de la acción que desea realizar: ")
            if alternativa == "1":
                self.delegacion.fichar(self.deportistas_disp)
            elif alternativa == "2":
                self.delegacion.entrenar_deportista()
            elif alternativa == "3":
                self.delegacion.sanar_deportista()
            elif alternativa == "4":
                self.delegacion.comprar_tec()
            elif alternativa == "5":
                self.delegacion.habilidad_especial()
            elif alternativa == "6":
                break
            else:
                self.Salir()
