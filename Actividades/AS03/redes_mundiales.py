import os

from cargar_archivos import cargar_aeropuertos, cargar_conexiones
from entidades import Aeropuerto, Conexion
from collections import deque

UMBRAL = 40000


class RedesMundiales:

    def __init__(self):
        # Estructura donde se guardaran los aeropuertos
        # Cada llave es un id y el valor es una instancia de Aeropuerto
        self.aeropuertos = {}

    def agregar_aeropuerto(self, aeropuerto_id, nombre):
        # Agregar un aeropuerto a la estructura
        nuevo_aeropuerto = Aeropuerto(aeropuerto_id, nombre)
        self.aeropuertos[aeropuerto_id] = nuevo_aeropuerto

    def agregar_conexion(self, aeropuerto_id_partida, aeropuerto_id_llegada, infectados):
        # Crear la conexion de partida-llegada para el par de aeropuertos
        conexion = Conexion(aeropuerto_id_partida,
                            aeropuerto_id_llegada, infectados)
        if aeropuerto_id_partida in self.aeropuertos and aeropuerto_id_llegada in self.aeropuertos:
            if conexion not in self.aeropuertos[aeropuerto_id_partida].conexiones:
                self.aeropuertos[aeropuerto_id_partida].conexiones.append(
                    conexion)

    def cargar_red(self, ruta_aeropuertos, ruta_conexiones):

        # Primero se crean todos los aeropuertos
        for aeropuerto_id, nombre in cargar_aeropuertos(ruta_aeropuertos):
            self.agregar_aeropuerto(aeropuerto_id, nombre)

        # Después generamos las conexiones
        for id_partida, id_salida, infectados in cargar_conexiones(ruta_conexiones):
            self.agregar_conexion(id_partida, id_salida, infectados)

    def eliminar_conexion(self, conexion):
        id_partida = conexion.aeropuerto_inicio_id
        id_llegada = conexion.aeropuerto_llegada_id
        aeropuerto_inicio = self.aeropuertos.get(id_partida)
        for c in aeropuerto_inicio.conexiones:
            if c.aeropuerto_llegada_id == id_llegada:
                aeropuerto_inicio.conexiones.remove(c)
                break

    def eliminar_aeropuerto(self, aeropuerto_id):
        if aeropuerto_id not in self.aeropuertos:
            raise ValueError(
                f"No puedes eliminar un aeropuerto que no existe ({aeropuerto_id})")
        if self.aeropuertos[aeropuerto_id].conexiones:
            raise ValueError(
                f"No puedes eliminar un aeropuerto con conexiones ({aeropuerto_id})")
        del self.aeropuertos[aeropuerto_id]

    def infectados_generados_desde_aeropuerto(self, aeropuerto_id):
        # Muestra la cantidad de infectados generados por un aeropuerto
        #usa BFS
        visitados = []
        infectados_acumulados = 0
        nodo_inicial = self.aeropuertos[aeropuerto_id]
        queue = deque([nodo_inicial])
        while len(queue) > 0:
            nodo = queue.popleft()

            if nodo in visitados:
                continue

            visitados.append(nodo)

            for vecino in nodo.conexiones:
                if vecino.aeropuerto_llegada_id not in visitados:
                    queue.append(
                        self.aeropuertos[vecino.aeropuerto_llegada_id])
                    infectados_acumulados += vecino.infectados
        print(f"La cantidad estimada de infectados generados por el aeropuerto {self.aeropuertos[aeropuerto_id].nombre} es de {infectados_acumulados}")
        return infectados_acumulados

    def verificar_candidatos(self, ruta_aeropuertos_candidatos, ruta_conexiones_candidatas):
        # Se revisa cada aeropuerto candidato con las agregars conexiones candidatas.
        # Se elimina el aeropuerto en caso de que este genere muchos infectados
        aeropuertos_candidatos = []
        conexiones_candidatas = []
        for aeropuerto_id, nombre in cargar_aeropuertos(ruta_aeropuertos_candidatos):
            self.agregar_aeropuerto(aeropuerto_id, nombre)

        for id_partida, id_salida, infectados in cargar_conexiones(ruta_conexiones_candidatas):
            self.agregar_conexion(id_partida, id_salida, infectados)
            if self.infectados_generados_desde_aeropuerto(id_partida) > UMBRAL:
                self.eliminar_conexion(Conexion(id_partida, id_salida, infectados))
                print(f"Se eliminó la conexión {Conexion(id_partida, id_salida, infectados)} al romper las reglas de seguridad")

    def escala_mas_corta(self, id_aeropuerto_1, id_aeropuerto_2, MAXITERACIONES = 50):
        # Usa BFS para encontrar desde el nodo de origen el nodo de destino.
        # Como BFS siempre encuentra primero el camino más corto, devolveremos el primer camino encontrado
        # Se va registrando la ruta por la cual se llega a cada nodo para devolver la ruta más corta
        # cuando se llega al nodo de destino
        maxnum = 0
        visitados = []
        camino = []
        distancia = 0
        nodo_inicial = self.aeropuertos[id_aeropuerto_1]
        queue = deque([nodo_inicial])
        camino_final = []
        while len(queue) > 0:
            nodo = queue.popleft()

            # Cuando encuentra el nodo de destino con BFS se mira en camino la ruta
            # por la cual se llego a aquel nodo
            if nodo.id == id_aeropuerto_2:
                nodo_actual = id_aeropuerto_2
                while nodo_actual != id_aeropuerto_1 and camino and maxnum <= MAXITERACIONES:
                    for conexion in camino:
                        if conexion[1] == nodo_actual:
                            camino_final.insert(0, str(conexion[0])+ "->" + str(nodo_actual))
                            camino.remove(conexion)
                            nodo_actual = conexion[0]
                            
                    maxnum +=1
                queue = []

            else:
                if nodo in visitados:
                    continue

                visitados.append(nodo)

                for vecino in nodo.conexiones:
                    if vecino.aeropuerto_llegada_id not in visitados:
                        queue.append(
                            self.aeropuertos[vecino.aeropuerto_llegada_id])
                        camino.append((nodo.id, vecino.aeropuerto_llegada_id))
                        # Appendea el par (nodo A, nodo B) donde A es el nodo por el cual se llegó a B
        if maxnum <= MAXITERACIONES and camino_final:
            print(f"Ruta más corta entre {id_aeropuerto_1} y {id_aeropuerto_2}: {camino_final}")
        else:
            return None

if __name__ == "__main__":
    # I: Construcción de la red
    # Instanciación de la red de aeropuertos
    redmundial = RedesMundiales()
    # Carga de datos (utiliza agregar_aeropuerto y agregar_conexion)
    redmundial.cargar_red(
        os.path.join("datos", "aeropuertos.txt"),
        os.path.join("datos", "conexiones.txt"),
    )

    # II: Consultas sobre la red
    # Verificar si conteo de infectados funciona
    # Para el aeropuerto 8 debería ser 2677
    redmundial.infectados_generados_desde_aeropuerto(8)
    # Para el aeropuerto 7 debería ser 10055
    redmundial.infectados_generados_desde_aeropuerto(7)
    # Para el aeropuerto 12 debería ser 30000
    redmundial.infectados_generados_desde_aeropuerto(4)

    # III: Simulación sobre la red
    # Utilizamos lo que hemos hecho para aplicar los cambios sobre la red
    redmundial.verificar_candidatos(
        os.path.join("datos", "aeropuertos_candidatos.txt"),
        os.path.join("datos", "conexiones_candidatas.txt"),
    )
    # Descomentar la prox linea para probar la función escala_mas_corta
    redmundial.escala_mas_corta(4,16)
    