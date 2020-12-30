from collections import namedtuple
from copy import deepcopy


class BolsilloCriaturas(list):

    def append(self, criatura):
        if len(self)<=5:
           super(BolsilloCriaturas, self).append(criatura)
        else:
            print("Se tienen 6 criaturas en el bolsillo, no es posible agregarla")

    def cantidad_criaturas_estrella(self):
        num_criaturas_estrella = 0
        for criatura in self:
            if criatura.hp_base + criatura.atk + criatura.sp_atk + criatura.defense > 400:
                num_criaturas_estrella +=1
        return num_criaturas_estrella

    def __add__(self, bolsillo_enemigo):
        criatura_enemiga = bolsillo_enemigo[0]
        # print(criatura_enemiga)
        for criatura in bolsillo_enemigo[1:]:
            if criatura.sp_atk + criatura.atk > criatura_enemiga.sp_atk + criatura_enemiga.atk:
                # print(f"Ahora {criatura} es la más fuerte")
                criatura_enemiga = criatura
        criatura_jugador = self[0]
        # print(criatura_jugador)
        for criatura in self[1:]:
            if criatura.sp_atk + criatura.atk < criatura_jugador.sp_atk + criatura_jugador.atk:
                # print(f"Ahora {criatura} es la más fuerte")
                criatura_jugador = criatura

        self.remove(criatura_jugador)
        self.append(criatura_enemiga)
        bolsillo_enemigo.remove(criatura_enemiga)
        bolsillo_enemigo.append(criatura_jugador)




if __name__ == '__main__':
    # NO MODIFICAR
    # El siguiente codigo te ayudara a hacer debugging,
    # simplemente ejecútalo para ver cómo vas

    # Criaturas de prueba
    # (Se deja hp_base por simplicidad)
    Criatura = namedtuple(
        "Criatura",
        ["nombre", "tipo", "hp_base", "atk", "sp_atk", "defense"],
    )
    criaturas_de_prueba = [
        Criatura("Cristian", "Water", 44, 48, 50, 65),
        Criatura("María José", "Fire", 78, 84, 109, 78),
        Criatura("Antonio", "Poison", 40, 60, 31, 30),
        Criatura("Joaquín", "Grass", 60, 62, 80, 63),
        Criatura("Dani", "Normal", 110, 160, 80, 110),
        Criatura("Tomás", "Rock", 35, 60, 40, 44),
    ]

    # Bolsillo de prueba
    bolsillo = BolsilloCriaturas()
    print("El bolsillo debería tener 0 criaturas")
    print(f"Tiene {len(bolsillo)} criaturas")
    # print(bolsillo)
    print()

    # Aquí se prueba si el método append esta correctamente implmentado
    for criatura in criaturas_de_prueba:
        bolsillo.append(criatura)
    print("El bolsillo debería tener 6 criaturas")
    print(f"El bolsillo tiene... {len(bolsillo)} criaturas")
    # print(bolsillo)
    print()

    bolsillo.append(Criatura("Benja", "Electric", 50, 60, 120, 95))
    print(f"(Deberías ver un mensaje de error porque no puedes agregar una séptima criatura)")
    print(f"El bolsillo tiene... {len(bolsillo)} criaturas")
    # print(bolsillo)
    print()

    print("El bolsillo debería tener 1 criatura estrella")
    n = bolsillo.cantidad_criaturas_estrella()
    if type(n) is int:
        print(f"El bolsillo tiene... {n} criaturas estrella")
    else:
        print("El método cantidad_criaturas_estrella aún no esta completado correctamente")
    print()

    # Bolsillo enemigo de prueba
    bolsillo_enemigo = deepcopy(bolsillo)
    bolsillo + bolsillo_enemigo
    contador_fuerte = len([criatura for criatura in bolsillo if criatura.nombre == "Dani"])
    contador_debil = len([criatura for criatura in bolsillo if criatura.nombre == "Antonio"])
    if contador_fuerte == 2 and contador_debil == 0:
        print("Método __add__ de Bolsillo: OK")
    else:
        print("El método __add__ aún no esta completado correctamente")
