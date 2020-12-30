import os
from random import choice, sample

from bolsillo import BolsilloCriaturas
from entidades import Criatura, Entrenador


def cargar_criaturas(archivo_criaturas):
    lista_criaturas = {}
    with open("criaturas.csv") as archivo:
        next(archivo)
        for line in archivo:
            criatura = line.split(",")
            key, value = criatura[0], Criatura(criatura[0], criatura[1], int(criatura[2]), int(criatura[3]), int(criatura[4]), int(criatura[5]))
            lista_criaturas[key] = value
    return(lista_criaturas)


def cargar_rivales(archivo_rivales):
    lista_rivales = []
    criaturas = cargar_criaturas("criaturas.csv")
    with open("rivales.csv") as archivo:
        next(archivo)
        for line in archivo:
            datos_rival = line.split(",")
            rival = datos_rival[0]
            criaturas_rival = datos_rival[1].strip("\n").split(";")
            bolsillo_rival = BolsilloCriaturas()
            for criatura in criaturas_rival:
                bolsillo_rival.append(criaturas[criatura])
            lista_rivales.append(Entrenador(rival, bolsillo_rival))
    return lista_rivales



def crear_jugador(nombre):
    criaturas = cargar_criaturas("criaturas.csv")
    criaturas_jugador = sample(list(criaturas),6)
    bolsillo_jugador = BolsilloCriaturas()
    for criatura in criaturas_jugador:
        bolsillo_jugador.append(criaturas[criatura])
    jugador = Entrenador(nombre, bolsillo_jugador)
    return jugador

if __name__ == "__main__":
    # NO MODIFICAR
    # El siguiente codigo te ayudara a debugear este archivo.
    # Simplemente corre este archivo (cargar_datos.py)

    # Aquí revisamos si te encuentras en la ruta adecuada, para esto
    # vemos si el archivo criaturas.csv se encuentra dentro de la
    # carpera en la que estás trabajando
    if "criaturas.csv" not in list(os.walk(os.getcwd()))[0][2]:
        print(f"No estas en el directorio adecuado!")
    criaturas = cargar_criaturas("criaturas.csv")
    rivales = cargar_rivales("rivales.csv")
    jugador = crear_jugador("El Cracks")

    # Aquí revisamos si retornas lo adecuado, para esto se revisa si
    # lo retornado es una instancia de la clase correspondiente
    if (type(criaturas) is not dict or \
        not all(type(criatura) is Criatura for criatura in criaturas.values())):
            print("Recuerda: cargar_criaturas retorna un diccionario con Criatura")
    else:
        print("Lista de Criatura tiene formato correcto")
    if type(rivales) is not list or not all(type(rival) is Entrenador for rival in rivales):
        print("Recuerda: cargar_rivales retorna una lista de Entrenador")
    else:
        print("Lista de Entrenador tiene formato correcto")

    # Aquí revisamos que los datos que deben ser entregados como int
    # al __init__ de Criaturas se almacenen con el tipo correcto
    if type(criaturas) is dict:
        if not all(
            type(atributo) is int
            for criatura in criaturas.values()
            for atributo in [criatura.hp_base, criatura.atk, criatura.sp_atk, criatura.defense]
        ):
            print("Recuerda: los atributos de Criatura hp, atk, sp_atk y defensa deben ser int")
        else:
            print("Instancias de Criatura tienen atributos con tipo correcto")

    # Aquí revisamos que la cantidad de Criaturas en el Bolsillo del
    # Jugador sea la adecuada
    if type(jugador) is not Entrenador or len(jugador.bolsillo) < 6:
        print("Recuerda: debes agregar 6 Criaturas a tu bolsillo")
    else:
        print("Jugador tiene la cantidad correcta de Criatura en su Bolsillo")
