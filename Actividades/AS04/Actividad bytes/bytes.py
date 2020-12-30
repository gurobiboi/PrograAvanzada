import os


def reparar_imagen(ruta_entrada, ruta_salida):
    bytes_salida = []
    with open(ruta_entrada, "rb") as byte_file:
        datos = byte_file.read()
        mis_bytes = bytearray(datos)
    for j in range(0, len(mis_bytes), 32):
        chunk = bytearray(mis_bytes[j:32+j])
        if chunk[0] == 1:
            print(chunk)
            inverso = bytearray()
            for i in range(16-1, -1, -1):
                inverso.append(chunk[i])
            chunk[0:16] = inverso
        bytes_salida.append(chunk[0:16])
        
    # print(bytes_salida)
    with open(ruta_salida, "wb") as byte_file_salida:
        for array in bytes_salida:
            byte_file_salida.write(array)

#--- NO MODIFICAR ---#
def reparar_imagenes(carpeta_entrada, carpeta_salida):
    for filename in os.listdir(os.path.join(os.getcwd(), carpeta_entrada)):
        reparar_imagen(
            os.path.join(os.getcwd(), carpeta_entrada, filename),
            os.path.join(os.getcwd(), carpeta_salida, filename)
        )


if __name__ == '__main__':
    try:
        reparar_imagenes('corruptas', 'caratulas')
        print("Imagenes reparadas (recuerda revisar que se carguen correctamente)")
    except Exception as error:
        print(f'Error: {error}')
        print("No has podido reparar las caratulas :'c")
