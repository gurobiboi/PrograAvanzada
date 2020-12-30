from random import uniform
from parametros import (MINIMO_HABILIDADES, MAXIMO_HABILIDADES,
                        PUNTOS_ENTRENAMIENTO)


# Clase deportista, tiene atributos pedidos y métodos
# entrenar y lesionarse
class Deportista:
    def __init__(self, nombre, flexibilidad, velocidad,
                 resistencia, moral, lesionado, precio):
        self.nombre = nombre
        self.__velocidad = velocidad
        self.__resistencia = resistencia
        self.__flexibilidad = flexibilidad
        self.__moral = moral
        if lesionado == "True":
            self.lesionado = True
        else:
            self.lesionado = False
        self.precio = precio
        self.identidad = None

    @property
    def velocidad(self):
        return self.__velocidad

    @velocidad.setter
    def velocidad(self, valor_nuevo):
        if valor_nuevo < MINIMO_HABILIDADES:
            self.__velocidad = int(MINIMO_HABILIDADES)
        elif valor_nuevo > MAXIMO_HABILIDADES:
            self.__velocidad = int(MAXIMO_HABILIDADES)
        else:
            self.__velocidad = int(round(valor_nuevo, 0))
    @property
    def resistencia(self):
        return self.__resistencia

    @resistencia.setter
    def resistencia(self, valor_nuevo):
        if valor_nuevo < MINIMO_HABILIDADES:
            self.__resistencia = int(MINIMO_HABILIDADES)
        elif valor_nuevo > MAXIMO_HABILIDADES:
            self.__resistencia = int(MAXIMO_HABILIDADES)
        else:
            self.__resistencia = int(round(valor_nuevo, 0))
    @property
    def flexibilidad(self):
        return self.__flexibilidad

    @flexibilidad.setter
    def flexibilidad(self, valor_nuevo):
        if valor_nuevo < MINIMO_HABILIDADES:
            self.__flexibilidad = int(MINIMO_HABILIDADES)
        elif valor_nuevo > MAXIMO_HABILIDADES:
            self.__flexibilidad = int(MAXIMO_HABILIDADES)
        else:
            self.__flexibilidad = int(round(valor_nuevo, 0))
    @property
    def moral(self):
        return self.__moral

    @moral.setter
    def moral(self, valor_nuevo):
        if valor_nuevo < MINIMO_HABILIDADES:
            self.__moral = int(MINIMO_HABILIDADES)
        elif valor_nuevo > int(MAXIMO_HABILIDADES):
            self.__moral = int(MAXIMO_HABILIDADES)
        else:
            self.__moral = int(round(valor_nuevo, 0))

    # Entrena la habilidad indicada
    def entrenar(self, habilidad, ponderador=1):
        if habilidad == "VELOCIDAD":
            self.velocidad += PUNTOS_ENTRENAMIENTO * ponderador
        elif habilidad == "RESISTENCIA":
            self.resistencia += PUNTOS_ENTRENAMIENTO * ponderador
        elif habilidad == "FLEXIBILIDAD":
            self.flexibilidad += PUNTOS_ENTRENAMIENTO * ponderador

    # Se lesiona con cierta probabilidad
    def lesionarse(self, riesgo):
        lesion = uniform(0, 1)
        if lesion <= riesgo:
            print(f"{self.nombre} se ha lesionado durante la competencia!")
            self.lesionado = True

    def __str__(self):
        return self.nombre