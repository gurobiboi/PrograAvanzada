import random
import time
from threading import Thread, Event, Lock, Timer

from parametros import (PROB_IMPOSTOR, PROB_ARREGLAR_SABOTAJE,
                        TIEMPO_ENTRE_TAREAS, TIEMPO_TAREAS, TIEMPO_SABOTAJE,
                        TIEMPO_ENTRE_ACCIONES, TIEMPO_ESCONDITE)

from funciones import (elegir_accion_impostor, print_progreso, print_anuncio,
                       print_sabotaje, cargar_sabotajes, print_explosión)


class Tripulante(Thread):

    def __init__(self, color, tareas, evento_sabotaje, diccionario_tareas):
        # No modificar
        super().__init__(daemon=True)
        self.color = color
        self.tareas = tareas
        self.esta_vivo = True
        self.diccionario_tareas = diccionario_tareas
        self.evento_sabotaje = evento_sabotaje
        # Si quieres agregar lineas, hazlo desde aca
        self.lock_sabotaje = Lock()

    def run(self):
        while self.esta_vivo and self.tareas:
            if not self.evento_sabotaje.is_set() and self.tareas:
                #  print("se realizará tarea")
                self.hacer_tarea()
                time.sleep(TIEMPO_ENTRE_TAREAS)
            else:
                while self.evento_sabotaje.is_set() and self.esta_vivo:
                    if not self.lock_sabotaje.locked():
                        prob = random.uniform(0, 1)
                        if prob <= PROB_ARREGLAR_SABOTAJE:
                            self.arreglar_sabotaje()
                        time.sleep(TIEMPO_ENTRE_TAREAS)

    def hacer_tarea(self):
        tarea_activa = random.choice(self.tareas)
        while True:
            if not self.diccionario_tareas[tarea_activa]["lock"].locked():
                self.diccionario_tareas[tarea_activa]["lock"].acquire()
                # print(f"se realizará tarea {tarea_activa}")
                break
        tiempo_tarea = random.randint(TIEMPO_TAREAS[0],TIEMPO_TAREAS[1])
        progreso_tarea = 0
        for _ in range(5):
            if self.esta_vivo == True:
                print_progreso(self.color, tarea_activa, progreso_tarea)
                time.sleep(tiempo_tarea/5)
                progreso_tarea += 20
        if progreso_tarea == 100:
            self.tareas.remove(tarea_activa)
            self.diccionario_tareas[tarea_activa]["lock"].release()
            self.diccionario_tareas[tarea_activa]["realizado"] = True

    def arreglar_sabotaje(self):
        if not self.lock_sabotaje.locked() and self.evento_sabotaje.is_set():
            self.lock_sabotaje.acquire()
            with self.lock_sabotaje:
                print_anuncio(self.color, "ha comenzado a arreglar el sabotaje")
                tiempo_arreglo = random.randint(TIEMPO_SABOTAJE[0],TIEMPO_SABOTAJE[1])
                progreso_arreglo = 0
                for _ in range(4):
                    if self.esta_vivo == True:
                        print_progreso(self.color, "Arreglando Sabotaje", progreso_arreglo)
                        time.sleep(tiempo_arreglo/4)
                        progreso_arreglo +=25
                    else:
                        break
                if progreso_arreglo == 100:
                    print_anuncio(self.color, "ha arreglado el sabotaje!")
                    self.evento_sabotaje.clear()
                    self.lock_sabotaje.release()
                else:
                    self.lock_sabotaje.release()


class Impostor(Tripulante):

    def __init__(self, color, tareas, evento_sabotaje, diccionario_tareas, tripulantes, evento_termino):
        # No modificar
        super().__init__(color, tareas, evento_sabotaje, diccionario_tareas)
        self.tripulantes = tripulantes
        self.evento_termino = evento_termino
        self.sabotajes = cargar_sabotajes()
        # Si quieres agregar lineas, hazlo desde aca

    def run(self):
        while self.tripulantes or not self.evento_termino.is_set():
            accion = elegir_accion_impostor()
            if accion == "Matar":
                self.matar_jugador()
            elif accion == "Sabotear":
                self.sabotear()
            else:
                time.sleep(TIEMPO_ESCONDITE)
            time.sleep(TIEMPO_ENTRE_ACCIONES)

    def matar_jugador(self):
        victima = random.choice(self.tripulantes)
        print_anuncio(victima.color, 'ha sido asesinade!')
        self.tripulantes.remove(victima)
        print(f"Quedan {len(self.tripulantes)} tripulantes vivos!")
        victima.esta_vivo = False
        

    def sabotear(self):
        if not self.evento_sabotaje.is_set():
            evento = random.choice(self.sabotajes)
            tiempo_alea = random.randint(TIEMPO_SABOTAJE[0], TIEMPO_SABOTAJE[1])
            timer_sabotaje = Timer(tiempo_alea, self.terminar_sabotaje())
            self.evento_sabotaje.set()
            print_sabotaje(evento)
    def terminar_sabotaje(self):
        if self.evento_sabotaje.is_set():
            for tripulante in self.tripulantes:
                tripulante.esta_vivo = False
            print_explosión()
            self.evento_termino.set()


if __name__ == "__main__":
    print("\n" + " INICIANDO PRUEBA DE TRIPULANTE ".center(80, "-") + "\n")
    # Se crea un diccionario de tareas y un evento sabotaje de ejemplos.
    ejemplo_tareas = {
            "Limpiar el filtro de oxigeno": {
                "lock": Lock(),
                "realizado": False,
                "nombre": "Limpiar el filtro de oxigeno"
            }, 
            "Botar la basura": {
                "lock": Lock(),
                "realizado": False,
                "nombre":  "Botar la basura"
            }
        }
    ejemplo_evento = Event()

    # Se intancia un tripulante de color ROJO
    rojo = Tripulante("Rojo", list(ejemplo_tareas.keys()), ejemplo_evento, ejemplo_tareas)

    rojo.start()

    time.sleep(5)
    # ==============================================================
    # Descomentar las siguientes lineas para probar el evento sabotaje.

    print(" HA COMENZADO UN SABOTAJE ".center(80, "*"))
    ejemplo_evento.set()

    rojo.join()

    print("\n-" + "="*80 + "\n")
    print(" PRUEBA DE TRIPULANTE TERMINADA ".center(80, "-"))
    if sum((0 if x["realizado"] else 1 for x in ejemplo_tareas.values())) > 0:
        print("El tripulante no logró completar todas sus tareas. ")
    elif ejemplo_evento.is_set():
        print("El tripulante no logró desactivar el sabotaje")
    else:
        print("El tripulante ha GANADO!!!")
