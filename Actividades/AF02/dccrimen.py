from estudiante import cargar_datos
from verificar import corregir_alumno, corregir_nota, inscripcion_valida


class GymPro(Exception):
    def __init__(self, alumno):
        mensaje = "Wait a minute... Who are you?"
        self.profesor = alumno.nombre
        super().__init__(mensaje)
            
    def evitar_sospechas(self):
        print(f"¡Cuidado, viene {self.profesor}! Solo estaba haciendo mi último push...\n")


if __name__ == "__main__":
    datos = cargar_datos("alumnos.txt")
    nueva_base = dict()
    for alumno in datos.values():
        corregir_alumno(alumno)
        corregir_nota(alumno)
        nueva_base[alumno.n_alumno] = alumno
    for alumno in nueva_base.values():
        try:
            if alumno.carrera == "Profesor":
                raise GymPro(alumno)
            else:
                alumno.promedio = float(7.0)
                print(f"Promedio de {alumno.nombre} hackeado a promedio {alumno.promedio} \n")

        except GymPro as error:
            print(error)
            GymPro(alumno).evitar_sospechas()
