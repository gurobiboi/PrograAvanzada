
import sys
from server import Server

if __name__ == "__main__":
    HOST = "localhost"
    PORT = 47365

    SERVER = Server(HOST, PORT)

    try:
        while True:
            input("Presione Ctrl+C para cerrar el servidor...")
    except KeyboardInterrupt:
        print("Cerrando servidor...")
