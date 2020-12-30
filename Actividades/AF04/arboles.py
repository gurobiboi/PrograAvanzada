class Nodo:
    def __init__(self, tipo, valor, padre):
        self.tipo = tipo
        self.valor = valor
        self.padre = padre

        self.hijos = []


class PlataformaMusical:
    def __init__(self, nombre_plataforma):
        self.raiz = Nodo("plataforma", nombre_plataforma, None)

    def agregar_cancion(self, info_cancion):
        genero = next((self.raiz.hijos.index(nodo) for nodo in self.raiz.hijos if nodo.valor == info_cancion['genero']), None)
        # print(f"genero:{genero}")
        if genero != None:
            artista = next((nodo.padre.hijos.index(nodo) for nodo in self.raiz.hijos[genero].hijos if nodo.valor == info_cancion['artista']), None)
           # print(f"artista:{artista}")
            if artista != None:
                album = next((nodo.padre.hijos.index(nodo) for nodo in self.raiz.hijos[genero].hijos[artista].hijos if nodo.valor == info_cancion['album']), None)
                # print(f"album:{album}")
                if album != None:
                    self.raiz.hijos[genero].hijos[artista].hijos[album].hijos.append(Nodo("cancion", info_cancion['nombre'], self.raiz.hijos[genero].hijos[artista].hijos[album]))
                else:
                    self.raiz.hijos[genero].hijos[artista].hijos.append(Nodo("album", info_cancion['album'], self.raiz.hijos[genero].hijos[artista]))
                    self.agregar_cancion(info_cancion)
            else:
                self.raiz.hijos[genero].hijos.append(Nodo("artista", info_cancion['artista'], self.raiz.hijos[genero]))
                self.agregar_cancion(info_cancion)
        else:
            self.raiz.hijos.append(Nodo("genero", info_cancion['genero'], self.raiz))
            self.agregar_cancion(info_cancion)


        
    def armar_arbol(self, informacion_canciones):
        print(f" Armando plataforma {self.raiz.valor} ".center(80, "*"))

        for cancion in informacion_canciones:
            self.agregar_cancion(cancion)

    def visualizar_arbol(self, nodo, margen=0):
        print(f'{"  " * margen}{nodo.valor}')
        if len(nodo.hijos) > 0:
            margen += 1
            for hijo in nodo.hijos:
                self.visualizar_arbol(hijo, margen)
