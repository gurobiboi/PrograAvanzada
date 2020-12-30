from collections import namedtuple, defaultdict


# Para esta parte necesitarás los contenidos de la semana 0
def cargar_datos(path):
    # Para esta función te puede servir el cuaderno 3 de la semana 0
    path_datos = path
    with open(path_datos, "rt") as archivo:
        next(archivo)
        lineas = [line.strip("\n") for line in archivo]
    return lineas
    

# De aquí en adelante necesitarás los contenidos de la semana 1
def crear_ayudantes(datos):
    # Completar función
    Ayudantes = []
    Register_ayudante = namedtuple("Ayudante_type", ["nombre", "cargo", "usuario"])
    while len(datos) > 0:
        current_datos = datos.pop(0).split(",")
        current_ayudante = Register_ayudante(current_datos[0],current_datos[1],current_datos[2])
        Ayudantes.append(current_ayudante)
    return Ayudantes

def encontrar_cargos(ayudantes):
    # Completar función
    cargos_posibles = set()
    for ayudante in ayudantes:
        cargos_posibles.add(ayudante.cargo)
    return cargos_posibles

def ayudantes_por_cargo(ayudantes):
    # Completar función
    list_ayudantes_por_cargo = defaultdict(list)
    for ayudante in ayudantes:
        list_ayudantes_por_cargo[ayudante.cargo].append(ayudante.nombre)

    return list_ayudantes_por_cargo


if __name__ == '__main__':
    datos = cargar_datos('ayudantes.csv')
    if datos is not None:
        print('Se lograron leer los datos')
        print(datos)
    else:
        print('Debes completar la carga de datos')

    ayudantes = crear_ayudantes(datos)
    if ayudantes is not None:
        print('\nLos ayudantes son:')
        for ayudante in ayudantes:
            print(ayudante)
    else:
        print('\nDebes completar la creación de Ayudantes')

    cargos = encontrar_cargos(ayudantes)
    if cargos is not None:
        print('\nLos cargos son:')
        for cargo in cargos:
            print(cargo)
    else:
        print('\nDebes completar la búsqueda de Cargos')

    clasificados = ayudantes_por_cargo(ayudantes)
    if clasificados is not None:
        print('\nLos ayudantes por cargos son:')
        for cargo in clasificados:
            print(f'\n{cargo}')
            for ayudante in clasificados[cargo]:
                print(ayudante)
    else:
        print('\nDebes completar la clasificación de Ayudantes')
        