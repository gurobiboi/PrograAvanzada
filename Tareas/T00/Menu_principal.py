class MenuInicio:
    def __init__(self, name, options, tabla_puntajes):
        self.menu_nombre = name
        self.menu_opciones = {}
        self.rankings = tabla_puntajes
        for option in options:
            self.menu_opciones[str(options.index(option)+1)] = option

    def input(self):
        menu_seleccion = 0
        for option, name_option in self.menu_opciones.items():
            print(f"{option}. {name_option}")
        while menu_seleccion not in self.menu_opciones:
            menu_seleccion = input("Indique su opción: ")
            if menu_seleccion not in self.menu_opciones:
                print("Opción inválida, vuelva a seleccionar una opción")
            if menu_seleccion in self.menu_opciones:
                print("\nSe escogió la opción: " +
                      f"{self.menu_opciones[menu_seleccion]}")
        if menu_seleccion == "1":
            return self.iniciar_partida()
        elif menu_seleccion == "2":
            opcion_volver = 1
            print(self.rankings)
            while opcion_volver != "0":
                opcion_volver = input("Para volver, presione el numero 0: ")
            return [0, 0, 0, 0]
        else:
            quit()

    def iniciar_partida(self):
        apodo = "%"
        filas = ""
        columnas = ""
        while not (apodo.isalnum() and len(apodo) <= 5):
            apodo = input("Ingrese su apodo " +
                          "(extension maxima, 5 caracteres): ")
            if not apodo.isalnum() or len(apodo) > 5:
                print("Apodo inválido, intente nuevamente")
        print(f"Bienvenido {apodo} !")
        while not (filas.isnumeric() and 3 <= int(filas) <= 15 and
                   columnas.isnumeric() and 3 <= int(columnas) <= 15):
            filas = input("Seleccione el numero de filas" +
                          "(maximo 15 minimo 3): ")
            columnas = input("Seleccione el numero de columnas " +
                             "(maximo 15 minimo 3): ")
            if not (filas.isnumeric() and 3 <= int(filas) <= 15 and
                    columnas.isnumeric() and 3 <= int(columnas) <= 15):
                print("\nTamano invalido, intente nuevamente porfavor\n")
        return [1, apodo, int(filas), int(columnas)]


if __name__ == "__main__":
    # Se crea menu inicio
    menu = MenuInicio("Menu de Inicio",
                      ["Iniciar una Partida",
                       "Ver el Ranking de Puntajes", "Salir"], "Hola")
    a = menu.input()
    print(a)
    quit()
