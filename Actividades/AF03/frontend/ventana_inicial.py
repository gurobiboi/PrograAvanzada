import os
from PyQt5.QtWidgets import (
    QLabel, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton
)
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPixmap


class VentanaInicial(QWidget):

    senal_comparar_codigo = pyqtSignal(str)
    senal_abrir_menu_principal = pyqtSignal()

    def __init__(self, ancho, alto, ruta_logo):
        """Es el init de la ventana del menú de inicio. Puedes ignorarlo."""
        super().__init__()
        self.size = (ancho, alto)
        self.resize(ancho, alto)
        self.init_gui(ruta_logo)

    def init_gui(self, ruta_logo):
        vbox = QVBoxLayout(self)
        self.imagen = QLabel("",self)
        imagen = QPixmap(ruta_logo)
        self.imagen.setPixmap(imagen)
        self.imagen.setScaledContents(True)
        self.input_codigo = QLineEdit(self)
        self.boton_ingresar = QPushButton("Ingresar", self)
        self.setWindowTitle("DCCrew")
        self.texto = QLabel("Ingrese el código de partida: ")

        vbox_codigo = QHBoxLayout(self)
        vbox.addWidget(self.imagen)

        vbox.addLayout(vbox_codigo)
        vbox_codigo.addStretch(1)
        vbox_codigo.addWidget(self.texto)
        vbox_codigo.addWidget(self.input_codigo)
        vbox_codigo.addStretch(1)
        
        vbox.addWidget(self.boton_ingresar)

        self.boton_ingresar.clicked.connect(self.comparar_codigo)

        self.show()


    def comparar_codigo(self):
        """Método que emite la señal para comparar el código. Puedes ignorarlo.
        Recuerda que el QLineEdit debe llamarse 'input_codigo'"""
        codigo = self.input_codigo.text()
        self.senal_comparar_codigo.emit(codigo)

    def recibir_comparacion(self, son_iguales):
        """Método que recibe el resultado de la comparación. Puedes ignorarlo.
        Recuerda que el QLineEdit debe llamarse 'input_codigo'"""
        if not son_iguales:
            self.input_codigo.clear()
            self.input_codigo.setPlaceholderText("¡Inválido! Debe ser un código existente.")
        else:
            self.hide()
            self.senal_abrir_menu_principal.emit()
