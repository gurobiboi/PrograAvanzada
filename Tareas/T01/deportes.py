from abc import ABC, abstractmethod
import parametros as param
from deportista import Deportista
from delegacion import Delegacion, DelegacionDCCrotona, DelegacionIEEEsparta

# Clase abstracta de deportes. Recibe competidores, los valida y calcula el ganador
# Lo que cambia entre cada clase heredada es la forma en que calcula el ganador
# usando una fórmula diferente en cada caso
class Deporte(ABC):

    def __init__(self, deportista_jugador, deportista_enemigo, deleg_jugador, deleg_enemigo):
        self.deportista_jugador = deportista_jugador
        self.deportista_enemigo = deportista_enemigo
        self.delegacion_jugador = deleg_jugador
        self.delegacion_enemigo = deleg_enemigo
        self.implemento = False
        self.riesgo_deporte = 0

    # Validan que los deportistas no esten lesionados y que el nivel de implementos
    # Sea el necesario. Ocupa la funcion lesionarse para los deportistas que compiten
    def validar(self, deportista, delegacion):
        if deportista != None and not deportista.lesionado and \
        not (delegacion.implem_deportivos < param.NIVEL_IMPLEMENTOS and self.implemento):
            deportista.lesionarse(self.riesgo_deporte)
            return True
        else:
            return False

    # Llama a la funcion validar() y en caso de que ambos deportistas sean
    # validados, calcula el ganador
    def calcular_ganador(self):
        if not self.validar(self.deportista_jugador, self.delegacion_jugador) \
        and self.validar(self.deportista_enemigo, self.delegacion_enemigo):
            print(f"Gana {self.deportista_enemigo.nombre} por reglamento!")
            return self.deportista_enemigo, self.deportista_jugador

        elif self.validar(self.deportista_jugador, self.delegacion_jugador) \
        and not self.validar(self.deportista_enemigo, self.delegacion_enemigo):
            print(f"Gana {self.deportista_jugador.nombre} por reglamento!")
            return self.deportista_jugador, self.deportista_enemigo

        elif not self.validar(self.deportista_jugador, self.delegacion_jugador) \
        and not self.validar(self.deportista_enemigo, self.delegacion_enemigo):
            print(f"Ningún jugador cumple con el reglamento, se declara empate!")
            return None, None
        else:
            return self.formula_ganador(self.deportista_jugador, self.deportista_enemigo)

    @abstractmethod
    def formula_ganador(self, jugador, enemigo):
        pass


class DeporteAtletismo(Deporte):

    def __init__(self, deportista_jugador, deportista_enemigo, deleg_jugador, deleg_enemigo):
        super().__init__(deportista_jugador, deportista_enemigo, deleg_jugador, deleg_enemigo)
        self.riesgo_deporte = param.RIESGO_ATLETISMO

    def formula_ganador(self, jugador, enemigo):
        puntaje_jugador = max(param.PUNTAJE_MINIMO,
                              param.PONDERADOR_ATLETISMO_VEL * jugador.velocidad + 
                              param.PONDERADOR_ATLETISMO_RES * jugador.resistencia +
                              param.PONDERADOR_ATLETISMO_MORAL * jugador.moral)

        puntaje_enemigo = max(param.PUNTAJE_MINIMO,
                              param.PONDERADOR_ATLETISMO_VEL * enemigo.velocidad + 
                              param.PONDERADOR_ATLETISMO_RES * enemigo.resistencia +
                              param.PONDERADOR_ATLETISMO_MORAL * enemigo.moral)

        if puntaje_jugador > puntaje_enemigo:
            print(f"Gana {jugador} !")
            return jugador, enemigo
        elif puntaje_jugador < puntaje_enemigo:
            print(f"Gana {enemigo} !")
            return enemigo, jugador
        else:
            print("Empate!")
            return None, None


class DeporteCiclismo(Deporte):

    def __init__(self, deportista_jugador, deportista_enemigo, deleg_jugador, deleg_enemigo):
        super().__init__(deportista_jugador, deportista_enemigo, deleg_jugador, deleg_enemigo)
        self.riesgo_deporte = param.RIESGO_CICLISMO
        self.implemento = True

    def formula_ganador(self, jugador, enemigo):
        puntaje_jugador = max(param.PUNTAJE_MINIMO,
                              param.PONDERADOR_CICLISMO_VEL * jugador.velocidad + 
                              param.PONDERADOR_CICLISMO_RES * jugador.resistencia +
                              param.PONDERADOR_CICLISMO_FLEX * jugador.flexibilidad)

        puntaje_enemigo = max(param.PUNTAJE_MINIMO,
                              param.PONDERADOR_CICLISMO_VEL * enemigo.velocidad + 
                              param.PONDERADOR_CICLISMO_RES * enemigo.resistencia +
                              param.PONDERADOR_CICLISMO_FLEX * enemigo.flexibilidad)

        if puntaje_jugador > puntaje_enemigo:
            print(f"Gana {jugador} !")
            return jugador, enemigo
        elif puntaje_jugador < puntaje_enemigo:
            print(f"Gana {enemigo} !")
            return enemigo, jugador
        else:
            print("Empate!")
            return None, None


class DeporteGimnasia(Deporte):

    def __init__(self, deportista_jugador, deportista_enemigo, deleg_jugador, deleg_enemigo):
        super().__init__(deportista_jugador, deportista_enemigo, deleg_jugador, deleg_enemigo)
        self.riesgo_deporte = param.RIESGO_GIMNASIA
        self.implemento = True

    def formula_ganador(self, jugador, enemigo):
        puntaje_jugador = max(param.PUNTAJE_MINIMO,
                              param.PONDERADOR_GIMNASIA_MORAL * jugador.moral + 
                              param.PONDERADOR_GIMNASIA_RES * jugador.resistencia +
                              param.PONDERADOR_GIMNASIA_FLEX * jugador.flexibilidad)

        puntaje_enemigo = max(param.PUNTAJE_MINIMO,
                              param.PONDERADOR_GIMNASIA_MORAL * enemigo.moral + 
                              param.PONDERADOR_GIMNASIA_RES * enemigo.resistencia +
                              param.PONDERADOR_GIMNASIA_FLEX * enemigo.flexibilidad)

        if puntaje_jugador > puntaje_enemigo:
            print(f"Gana {jugador} !")
            return (jugador, enemigo)
        elif puntaje_jugador < puntaje_enemigo:
            print(f"Gana {enemigo} !")
            return (enemigo, jugador)
        else:
            print("Empate!")
            return None, None


class DeporteNatacion(Deporte):

    def __init__(self, deportista_jugador, deportista_enemigo, deleg_jugador, deleg_enemigo):
        super().__init__(deportista_jugador, deportista_enemigo, deleg_jugador, deleg_enemigo)
        self.riesgo_deporte = param.RIESGO_NATACION

    def formula_ganador(self, jugador, enemigo):
        puntaje_jugador = max(param.PUNTAJE_MINIMO,
                              param.PONDERADOR_NATACION_VEL * jugador.velocidad + 
                              param.PONDERADOR_NATACION_RES * jugador.resistencia +
                              param.PONDERADOR_NATACION_FLEX * jugador.flexibilidad)

        puntaje_enemigo = max(param.PUNTAJE_MINIMO,
                              param.PONDERADOR_NATACION_VEL * enemigo.velocidad + 
                              param.PONDERADOR_NATACION_RES * enemigo.resistencia +
                              param.PONDERADOR_NATACION_FLEX * enemigo.flexibilidad)
        
        if puntaje_jugador > puntaje_enemigo:
            print(f"Gana {jugador} !")
            return (jugador, enemigo)
        elif puntaje_jugador < puntaje_enemigo:
            print(f"Gana {enemigo} !")
            return (enemigo, jugador)
        else:
            print("Empate!")
            return None, None