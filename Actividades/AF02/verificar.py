from estudiante import cargar_datos, cargar_datos_corto


def verificar_numero_alumno(alumno):  # Levanta la excepción correspondiente
    if not alumno.n_alumno.isnumeric() and alumno.n_alumno[-1] != "J":
        raise ValueError("El numero de alumno es incorrecto")
    elif int(alumno.n_alumno[0:2])!= alumno.generacion % 100:
        raise ValueError("El numero de alumno es incorrecto")
    elif not (alumno.n_alumno[2:4] == "63" and alumno.carrera == "Ingeniería") or \
             (alumno.n_alumno[2:4] == "61" and alumno.carrera == "College"):
        raise ValueError("El numero de alumno es incorrecto")

def corregir_alumno(estudiante): # Captura la excepción anterior
    try:
        verificar_numero_alumno(estudiante)
    except ValueError as error:
        print(f"Error: {error}")
        numero_erroneo = estudiante.n_alumno
        if not numero_erroneo[:-1].isnumeric():
            for caracter in numero_erroneo[:-1]:
                if not caracter.isnumeric():
                    numero_erroneo = numero_erroneo.strip(caracter)
                    numero_erroneo = numero_erroneo + caracter
                    break
        if not numero_erroneo[-1].isnumeric() and numero_erroneo[-1] != "J":
            numero_erroneo = numero_erroneo[0:-2] + "J"
        numero_erroneo = str(estudiante.generacion % 100) + numero_erroneo[2:]
        if estudiante.carrera == "Ingeniería":
            numero_erroneo = numero_erroneo[:2] + "63" + numero_erroneo[4:]
        elif estudiante.carrera == "College":
            numero_erroneo = numero_erroneo[:2] + "61" + numero_erroneo[4:]
        estudiante.n_alumno = numero_erroneo
    finally:
        print(f"{estudiante.nombre} está correctamente inscrite en el curso, todo en orden...\n")



# ************

def verificar_inscripcion_alumno(n_alumno, base_de_datos): # Levanta la excepción correspondiente
    if n_alumno not in base_de_datos:
        raise KeyError("El numero de alumno no se encuentra en la base de datos")
    else:
        return base_de_datos[n_alumno]


def inscripcion_valida(estudiante, base_de_datos):  # Captura la excepción anterior
    try:
        verificar_inscripcion_alumno(estudiante.n_alumno, base_de_datos)
    except KeyError as error:
        print(f"Error: {error}")
        print("¡Alerta! ¡Puede ser Dr. Pinto intentando atraparte!\n")



# ************

def verificar_nota(alumno):  # Levanta la excepción correspondiente
    if not isinstance(alumno.promedio, float):
        raise TypeError("El promedio no tiene el tipo correcto")
    else:
        return True

def corregir_nota(estudiante):  # Captura la excepción anterior
    try:
        verificar_nota(estudiante)
    except TypeError as error:
        print(f"Error: {error}")
        digitos = str(estudiante.promedio).split(",")
        if len(digitos) == 1:
            estudiante.promedio = float(digitos[0])
        elif len(digitos) == 2:
            estudiante.promedio = float(digitos[0]) + float(digitos[1])/10
    finally:
        print(f"Procediendo a hacer hack sobre {estudiante.promedio}... \n")


if __name__ == "__main__":
    datos = cargar_datos_corto("alumnos.txt")  # Se cargan los datos
    for alumno in datos.values():
        if alumno.carrera != "Profesor":
            corregir_alumno(alumno)
            inscripcion_valida(alumno, datos)
            corregir_nota(alumno)
