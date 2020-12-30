from abc import ABC, abstractmethod
from random import uniform, choice
import parametros as param
from tableros import tablero_deportistas
from deportista import Deportista

# Clase abstracta Delegacion, tiene instancias de Deportistas como equipo
# y realiza varias acciones referentes a los deportistas en sus métodos.
class Delegacion(ABC):

    def __init__(self, entrenador, equipo, moral_equipo,
                 dinero):
        self.entrenador = entrenador
        self.equipo = equipo
        self.medallas = {"atletismo": 0, "ciclismo": 0, "gimnasia": 0, "natacion": 0}
        self.moral_equipo = 0
        self.calcular_moral()
        self.__dinero = dinero
        self.habilidad_disponible = True
        self.nombre = None

    @property
    def dinero(self):
        return self.__dinero

    @dinero.setter
    def dinero(self, monto):
        if monto < 0:
            self.__dinero = 0
        else:
            self.__dinero = monto

    # Busca nuevo deportista dentro de los disponible y lo agrega al equipo
    def fichar(self, deportistas_disponibles):
        print(f"Se tiene {self.dinero} disponible \n")
        tablero_deportistas(deportistas_disponibles, True)
        fichaje = input("Escriba el nombre del deportista que piensa reclutar: ")
        while not (isinstance(fichaje, str) and fichaje in deportistas_disponibles):
            print("Opción inválida, intente denuevo \n")
            fichaje = input("Escriba el nombre del deportista que piensa reclutar: ")
        if deportistas_disponibles[fichaje].precio <= self.dinero:
            self.equipo[fichaje] = deportistas_disponibles[fichaje]
            self.equipo[fichaje].identidad = self.nombre
            deportistas_disponibles.pop(fichaje)
            self.dinero -= self.equipo[fichaje].precio
        else:
            print("No se tiene dinero suficiente para fichar a este deportista!\n")

    @abstractmethod
    def entrenar_deportista(self, deportista):
        pass

    @abstractmethod
    def sanar_deportista(self, deportista):
        pass
    
    # Compra tecnología dependiendo el tipo elegido
    def comprar_tec(self):
        print("Puede comprar 2 tipos de elementos: Deportivos o Médicos")
        tipo = input("Elija un tipo de elemento: ")
        while tipo.upper() != "DEPORTIVOS" and tipo.upper() != "MEDICOS":
            print("Opción inválida, selecciones entre Deportivos y Médicos")
            tipo = input("Elija un tipo de elemento: ")
        
        if self.dinero >= param.COSTO_IMPLEMENTOS:
            if tipo.upper() == "DEPORTIVOS":
                self.implem_deportivos *= param.AUMENTO_EFECTIVIDAD_IMPLEMENTOS + 1
            else:
                self.implem_medicos *= param.AUMENTO_EFECTIVIDAD_IMPLEMENTOS + 1
            self.dinero -= param.COSTO_IMPLEMENTOS
        else:
            print("Dinero Insuficiente para comprar elementos")

    @abstractmethod
    def habilidad_especial(self):
        pass

    @abstractmethod
    def premiar(self, deportista, ganador = True):
        pass

    # Calcula la moral del equipo
    def calcular_moral(self):
        aux_moral = 0
        for deportista in self.equipo.values():
            aux_moral += deportista.moral
        self.moral_equipo = aux_moral / len(self.equipo)
        return int(self.moral_equipo)

    def __str__(self):
        return self.nombre


class DelegacionIEEEsparta(Delegacion):

    def __init__(self, entrenador, equipo, moral,
                 dinero):
        super().__init__(entrenador, equipo, moral,
                         dinero)
        self.nombre = "IEEEsparta"
        self.excelencia_respeto = round(uniform(param.IEEE_EXC_RESPETO_MIN, param.IEEE_EXC_RESPETO_MAX), 1)
        self.implem_deportivos = round(uniform(param.IEEE_IMPL_DEPORTIVOS_MIN, param.IEEE_IMPL_DEPORTIVOS_MAX), 1)
        self.implem_medicos = round(uniform(param.IEEE_IMPL_MEDICOS_MIN, param.IEEE_IMPL_MEDICOS_MAX), 1)

    # Entrena la habilidad e;egida del deportista elegido
    def entrenar_deportista(self):
        if self.dinero >= param.COSTO_ENTRENAR:
            tablero_deportistas(self.equipo)

            deportista = input("Escriba el nombre del deportista que piensa entrenar: ")
            while not (isinstance(deportista, str) and deportista in self.equipo):
                print("Opción inválida, intente denuevo \n")
                deportista = input("Escriba el nombre del deportista que piensa entrenar: ")

            habilidad = input("Eliga que habilidad desea entrenar (velocidad, flexibilidad o resistencia): ")
            while habilidad.upper() != "VELOCIDAD" and habilidad.upper() != "FLEXIBILIDAD" and habilidad.upper() != "RESISTENCIA":
                print("Opción inválida, intente denuevo \n")
                habilidad = input("Eliga que habilidad desea entrenar (velocidad, flexibilidad o resistencia): ")
            
            self.equipo[deportista].entrenar(habilidad.upper(), param.IEEE_EFECTIVIDAD_ENTRENAMIENTO)
            print(f"Has entrenado la {habilidad} de {deportista} !")
            self.dinero -= param.COSTO_ENTRENAR
        else:
            print("Insuficiente dinero, no se puede entrenar al deportista!")

    # Sana el deportista elegido
    def sanar_deportista(self):
        if self.dinero >= param.COSTO_SANAR:
            tablero_deportistas(self.equipo)

            deportista = input("Escriba el nombre del deportista que piensa sanar: ")
            while not (isinstance(deportista, str) and deportista in self.equipo):
                print("Opción inválida, intente denuevo \n")
                deportista = input("Escriba el nombre del deportista que piensa sanar: ")

            formula_recuperar = round(min(1, max(0, (self.equipo[deportista].moral *
                                                (self.implem_medicos +
                                                self.excelencia_respeto)/200))), 1)
            recuperar_real = round(uniform(0, 1), 1)
            if recuperar_real <= formula_recuperar:
                self.equipo[deportista].lesionado = False
                print(f"{deportista} se ha sanado!")
            else:
                print(f"Se ha fallado sanando a {deportista} =(")
            self.dinero -= param.COSTO_SANAR
        else:
            print("Dinero insuficiente para sanar a un deportista!")

    # Funcion premia al deportista que gano una competencia, recibe medalla
    # y dinero por ganar y aumenta stats del deportista y delegacion
    # También escribe en resultados.txt el ganador

    def premiar(self, deportista, deporte, ganador = True):
        if ganador:

            self.medallas[deporte] += 1
            self.excelencia_respeto += param.EXC_RESPETO_MEDALLA_WIN
            self.dinero += param.DINERO_DELEGACION_MEDALLA_WIN
            self.equipo[deportista].moral += param.MORAL_DEPORTISTA_MEDALLA_WIN
            with open("resultados.txt", "a") as file:
                file.write(f"Competencia: {deporte}\n")
                file.write(f"Delegacion Ganadora: {self.nombre}\n")
                file.write(f"Deportista Ganador: {deportista}\n")
                file.write("\r\n")

        else:
            self.excelencia_respeto -= param.EXC_RESPETO_MEDALLA_LOSE
            self.equipo[deportista].moral -= param.MORAL_DEPORTISTA_MEDALLA_LOSE * 2

    def habilidad_especial(self):
        if self.habilidad_disponible:
            print("Ocupaste tu habilidad y los deportistas de tu equipo elevan su moral!! ")
            for deportista in self.equipo.values():
                deportista.moral = param.MAXIMO_HABILIDADES
            self.habilidad_disponible = False
        else:
            print("Ya se usó la habilidad especial!")


class DelegacionDCCrotona(Delegacion):

    def __init__(self, entrenador, equipo, moral,
                 dinero):
        super().__init__(entrenador, equipo, moral,
                         dinero)
        self.nombre = "DCCrotona"
        self.excelencia_respeto = round(uniform(param.DCC_EXC_RESPETO_MIN, param.DCC_EXC_RESPETO_MAX), 1)
        self.implem_deportivos = round(uniform(param.DCC_IMPL_DEPORTIVOS_MIN, param.DCC_IMPL_DEPORTIVOS_MAX), 1)
        self.implem_medicos = round(uniform(param.DCC_IMPL_MEDICOS_MIN, param.DCC_IMPL_MEDICOS_MAX), 1)

    def entrenar_deportista(self):
        if self.dinero >= param.COSTO_ENTRENAR:
            tablero_deportistas(self.equipo)

            deportista = input("Escriba el nombre del deportista que piensa entrenar: ")
            while not (isinstance(deportista, str) and deportista in self.equipo):
                print("Opción inválida, intente denuevo \n")
                deportista = input("Escriba el nombre del deportista que piensa entrenar: ")

            habilidad = input("Eliga que habilidad desea entrenar (velocidad, flexibilidad o resistencia): ")
            while habilidad.upper() != "VELOCIDAD" and habilidad.upper() != "FLEXIBILIDAD" and habilidad.upper() != "RESISTENCIA":
                print("Opción inválida, intente denuevo \n")
                habilidad = input("Eliga que habilidad desea entrenar (velocidad, flexibilidad o resistencia): ")
            self.equipo[deportista].entrenar(habilidad.upper())
            print(f"Has entrenado la {habilidad} de {deportista} !")
            self.dinero -= param.COSTO_ENTRENAR
        else:
            print("Insuficiente dinero, no se puede entrenar al deportista!")

    def sanar_deportista(self):
        if self.dinero >= param.COSTO_SANAR:
            tablero_deportistas(self.equipo)

            deportista = input("Escriba el nombre del deportista que piensa sanar: ")
            while not (isinstance(deportista, str) and deportista in self.equipo):
                print("Opción inválida, intente denuevo \n")
                deportista = input("Escriba el nombre del deportista que piensa sanar: ")

            formula_recuperar = round(min(1, max(0, (self.equipo[deportista].moral *
                                                (self.implem_medicos +
                                                 self.excelencia_respeto)/200))), 1)
            recuperar_real = round(uniform(0, 1), 1)
            if recuperar_real <= formula_recuperar:
                self.equipo[deportista].lesionado = False
                print(f"{deportista} se ha sanado!") 
            else:
                print(f"Se ha fallado sanando a {deportista} =(")
            self.dinero -= param.COSTO_SANAR * 2
        else:
            print("Dinero insuficiente para sanar a un deportista!")

    def habilidad_especial(self):
        if self.habilidad_disponible:
            print("Ocupaste tu habilidad especial, ganas una medalla automaticamente!!!")
            self.premiar(choice(list(self.equipo)), "atletismo")
            self.habilidad_disponible = False
        else:
            print("Ya se usó la habilidad especial!")

    def premiar(self, deportista, deporte, ganador=True):
        if ganador:     
            self.medallas[deporte] += 1
            self.excelencia_respeto += param.EXC_RESPETO_MEDALLA_WIN
            self.dinero += param.DINERO_DELEGACION_MEDALLA_WIN
            self.equipo[deportista].moral += param.MORAL_DEPORTISTA_MEDALLA_WIN * 2
            with open("resultados.txt", "a") as file:
                file.write(f"Competencia: {deporte}\n")
                file.write(f"Delegacion Ganadora: {self.nombre}\n")
                file.write(f"Deportista Ganador: {deportista}\n")
                file.write("\r\n")
        else:
            self.excelencia_respeto -= param.EXC_RESPETO_MEDALLA_LOSE
            self.equipo[deportista].moral -= param.MORAL_DEPORTISTA_MEDALLA_LOSE
