from deportista import Deportista


# Estas funciones imprimen los tableros con informacion
# De los deportistas o delegacion
def tablero_deportistas(lista, precio=False):
    if precio:
        print("Nombre deportista"," "*9,"| Velocidad | Resistencia | Flexibilidad | Lesión | Precio ($)")
        for deportista in lista.values():
            print(f"{deportista.nombre:28s}  {deportista.velocidad: ^9d}   {deportista.resistencia: ^11d}",
                  f" {deportista.flexibilidad: ^14d}  {str(deportista.lesionado):<8s}   {deportista.precio:^3d}")
    else:
        print("Nombre deportista"," "*9,"| Velocidad | Resistencia | Flexibilidad | Lesión ")
        for deportista in lista.values():
            print(f"{deportista.nombre:28s}{deportista.velocidad: ^13d}"\
                    f"{deportista.resistencia: ^11d}{deportista.flexibilidad: ^19d}" \
                    f"{str(deportista.lesionado):>6s}")
    print("\n")


def tablero_delegacion(delegacion):
    print(delegacion.nombre)
    print(f"\nEntrenador: {delegacion.entrenador}")
    print(f"Moral de Equipo: {delegacion.calcular_moral()}")
    print(f"Excelencia y Respeto: {delegacion.excelencia_respeto:<3.2f}")
    print(f"Implementos deportivos: {delegacion.implem_deportivos:<3.2f}")
    print(f"Implementos Médicos: {delegacion.implem_medicos:<3.2f}")
    print(f"Dinero Disponible: {delegacion.dinero}\n")
    print("*"*15)
    print(f"Medallas:")
    for deporte in delegacion.medallas:
        print(f"{deporte}: {delegacion.medallas[deporte]}")
    print("*"*15)
def tablero_competencia(competencia):
    pass


if __name__ == "__main__":
    Seba = Deportista("Sebastian Yanez", 20, 20, 20, 20, False, 30)
    Diego = Deportista("Diego Yanez", 20, 20, 100, 20, True, 300)
    tablero_deportistas({"Sebastian" : Seba, "Diego": Diego}, True)