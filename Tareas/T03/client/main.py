
from client import Client
from PyQt5.QtWidgets import QApplication
import sys

if __name__ == "__main__":
    # Se establece el host y port.
    # Puedes modificar estos valores si lo deseas.
    HOST = "localhost"
    PORT = 47365

    APP = QApplication([])
    # Se instancia el Cliente.
    CLIENT = Client(HOST, PORT)

    # Se inicia app de PyQt
    ret = APP.exec_()
    sys.exit(ret)
