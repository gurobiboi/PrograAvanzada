from PyQt5.QtCore import pyqtSignal, QObject, QTimer
from start_window import StartWindow

class Controller(QObject):


    def __init__(self, parent):
        super().__init__()

        self.start_window = StartWindow()
        self.show_start_window()

    def show_start_window(self):
        self.start_window.show()