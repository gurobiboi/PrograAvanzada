class TablaPuntajes:

    def __init__(self, archivo):
        self.datos = {}
        self.txt = archivo
        with open(self.txt) as rankings:
            for line in rankings:
                (key, val) = line.split(",")
                val = val.strip("\n")
                self.datos[key] = int(val)

    def __str__(self):
        lista = [(key, val) for key, val in
                 sorted(self.datos.items(), key=lambda x: x[1], reverse=True)]
        lista_ordenada = ""
        for jugador, puntaje in lista[:5]:
            lista_ordenada += f"{jugador:5.5s}" + "     " + \
                              f"{str(puntaje):8.8s}" + "\n"
        return lista_ordenada

    def agregar(self, apodo, puntaje):
        while apodo in self.datos:
            apodo = apodo + "1"
        self.datos[apodo] = puntaje
        nueva_linea = apodo+"," + str(puntaje)
        with open(self.txt, "a") as tabla:
            tabla.write("\n")
            tabla.write(nueva_linea)


if __name__ == "__main__":
    tabla = TablaPuntajes("puntajes.txt")
    print(tabla)
