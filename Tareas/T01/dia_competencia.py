from deportes import DeporteAtletismo, DeporteCiclismo, DeporteGimnasia, DeporteNatacion


# La clase DiaCompetencia recibe a los competidores,crea las instancias 
# de deportes para cada día de competencia, llama a las funciones de 
# los deportes para calcular los ganadores y los premia terminado el día.
class DiaCompetencia:

    def __init__(self, dia, equipo_jugador, equipo_enemigo, delegaciones):
        self.dia = dia
        self.equipo_jugador = equipo_jugador
        self.equipo_enemigo = equipo_enemigo
        self.delegaciones = delegaciones
        self.atletismo = DeporteAtletismo(equipo_jugador["atletismo"],
                                          equipo_enemigo["atletismo"],
                                          delegaciones[0], delegaciones[1])
        self.ciclismo = DeporteCiclismo(equipo_jugador["ciclismo"],
                                        equipo_enemigo["ciclismo"],
                                        delegaciones[0], delegaciones[1])
        self.gimnasia = DeporteGimnasia(equipo_jugador["gimnasia"],
                                        equipo_enemigo["gimnasia"],
                                        delegaciones[0], delegaciones[1])
        self.natacion = DeporteNatacion(equipo_jugador["natacion"],
                                        equipo_enemigo["natacion"],
                                        delegaciones[0], delegaciones[1])
        self.ganadores = {}
        self.perdedores = {}
        with open("resultados.txt", "a") as file:
            file.write(f"\n Dia: {self.dia * 2 + 2}\n")
            file.write("\r\n")
        self.competir()
        self.premiar_dia()

    # Hace competir a los deportistas
    def competir(self):
        self.ganadores["atletismo"], self.perdedores["atletismo"]  = self.atletismo.calcular_ganador()
        self.ganadores["ciclismo"], self.perdedores["ciclismo"]  = self.ciclismo.calcular_ganador()
        self.ganadores["gimnasia"], self.perdedores["gimnasia"] = self.gimnasia.calcular_ganador()
        self.ganadores["natacion"], self.perdedores["natacion"] = self.natacion.calcular_ganador()

    # Premia alfinal del día a los deportistas ganadores, llamando a la funcion premiar de
    # la delegación correspondiente
    def premiar_dia(self): 
        for deporte in self.ganadores:
            if self.ganadores[deporte] is not None:
                ganador, perdedor = self.ganadores[deporte].nombre, self.perdedores[deporte].nombre
                if ganador in self.delegaciones[0].equipo:
                    self.delegaciones[0].premiar(ganador, deporte)
                    if perdedor in self.delegaciones[1].equipo:
                        self.delegaciones[1].premiar(perdedor, deporte, ganador=False)
            
                elif ganador in self.delegaciones[1].equipo:
                    self.delegaciones[1].premiar(ganador, deporte)
                    if ganador in self.delegaciones[0].equipo:
                        self.delegaciones[0].premiar(perdedor, deporte, ganador=False)
