# Start window
import sys
import os
from time import sleep
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.QtCore import pyqtSignal, QRect

window_name, base_class = uic.loadUiType(os.path.join('UI', 'StartWindow.ui'))


# Front-end de la ventana de inicio
# Se comunica con otras ventanas y le entrega info
# del nombre del jugador al backend


def hook(type_error, traceback):
    print(type_error)
    print(traceback)


class StartWindow(window_name, base_class):

    gamestart_signal = pyqtSignal(str)
    rankings_signal = pyqtSignal()
    openwindow_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButtonStart.clicked.connect(self.start_game)
        self.errormessage = QMessageBox()
        self.errormessage.setText("Porfavor, ingrese un nombre válido!")
        self.openwindow_signal.connect(self.show)
        self.pushButtonRankings.clicked.connect(self.rankings)

    def start_game(self, name):
        if not (self.nameEdit.text().isalnum() and self.nameEdit.text() != ""):
            self.errormessage.exec()
        else:
            self.hide()
            self.gamestart_signal.emit(self.nameEdit.text())

    def rankings(self):
        self.hide()
        self.rankings_signal.emit()


if __name__ == "__main__":
    app = QApplication([])
    start_window = StartWindow()
    start_window.show()
    sys.exit(app.exec_())
