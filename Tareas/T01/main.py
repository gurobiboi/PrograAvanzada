from collections import namedtuple
from campeonato import Campeonato
from delegacion import Delegacion, DelegacionDCCrotona, DelegacionIEEEsparta
from deportista import Deportista
from dia_competencia import DiaCompetencia
from deportes import Deporte, DeporteAtletismo, DeporteCiclismo, DeporteGimnasia, DeporteNatacion
from menus import Menu, MenuEntrenador, MenuInicio, MenuPrincipal
from tableros import tablero_deportistas, tablero_delegacion, tablero_competencia

print("👌")
# Lee los deportistas disponibles en un diccionario
base_deportistas = {}
with open("deportistas.csv", "r") as data_deportistas:
    header = data_deportistas.readline().strip("\n").split(",")
    Registro_deportista = namedtuple("Deportista", [header[0], header [1], header[2],
                                                    header[3], header[4], header[5], header[6]])
    for line in data_deportistas:
        deport = Registro_deportista(*line.strip("\n").split(","))
        objeto_deportista = Deportista(deport.nombre, int(deport.flexibilidad), 
                                       int(deport.velocidad),int(deport.resistencia),
                                       int(deport.moral), deport.lesionado, int(deport.precio))
        base_deportistas[objeto_deportista.nombre] = objeto_deportista

# Lee las delegaciones iniciales y sus deportistas
with open("delegaciones.csv", "r") as data_delegaciones:
    header = data_delegaciones.readline().strip("\n").split(",")
    Registro_delegacion = namedtuple("Delegacion", [header[0], header [1], header[2],
                                                    header[3], header[4]])
    for line in data_delegaciones:
        deleg = Registro_delegacion(*line.strip("\n").split(","))
        if deleg.Delegacion == "IEEEsparta":
            equipo_IEEE = {}
            for deportista in deleg.Equipo.split(";"):
                for deportista_disp in base_deportistas:
                    if deportista_disp == deportista:
                        base_deportistas[deportista_disp].identidad= "IEEEsparta"
                        equipo_IEEE[deportista_disp] = base_deportistas[deportista_disp]
                        
            for deportista in equipo_IEEE:
                base_deportistas.pop(deportista)
            IEEE = [equipo_IEEE, float(deleg.Moral), int(deleg.Dinero)]
        if deleg.Delegacion == "DCCrotona":
            equipo_DCC = {}
            for deportista in deleg.Equipo.split(";"):
                for deportista_disp in base_deportistas:
                    if deportista_disp == deportista:
                        base_deportistas[deportista_disp].identidad= "DCCrotona"
                        equipo_DCC[deportista_disp] = base_deportistas[deportista_disp]
            for deportista in equipo_DCC:
                base_deportistas.pop(deportista)

            DCC = [equipo_DCC, float(deleg.Moral), int(deleg.Dinero)]

menu_inicial = MenuInicio(base_deportistas, DCC, IEEE)
menu_inicial.eleccion()
