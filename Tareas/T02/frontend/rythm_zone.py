from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QHBoxLayout,
                             QVBoxLayout, QPushButton, QMainWindow)
from PyQt5.QtCore import pyqtSignal, QObject, QTimer, QThread, QRect

from time import sleep
import sys
import os
from PyQt5.QtGui import QPixmap
from random import randint, choice
import parameters as p


# Front-end de la sección de juego o Zona de ritmo
# Produce Flechas como QThreads y mueve las labels
# Verifica visualmente que las flechas se apretaron al momento adecuado
# para mandar la señal al backend y actualizar puntajes/combos

class DanceMove(QThread):

    update_pos = pyqtSignal(QLabel, int, int)
    kill_move = pyqtSignal(QThread)
    move_valid = pyqtSignal(bool, str)

    def __init__(self, lparent, limit_x, limit_y):
        super().__init__()
        self.parent = self
        self.arrowdir = choice(["left", "up", "right", "down"])
        prob_flecha = randint(0, 100)
        if prob_flecha <= p.NORMAL_PROB:
            self.arrowtype = "normal"
        elif p.X2_PROB >= prob_flecha > p.NORMAL_PROB:
            self.arrowtype = "x2"
        elif p.FREEZE_PROB >= prob_flecha > p.X2_PROB:
            self.arrowtype = "freeze"
        else:
            self.arrowtype = "golden"

        self.image_route = os.path.join(
            p.KEY_SPRITE_DIR[0], p.KEY_SPRITE_DIR[1], p.KEY_SPRITES[self.arrowdir][self.arrowtype])
        self.label = QLabel(lparent)
        self.label.setGeometry(-50, -50, p.ARROW_SIZE, p.ARROW_SIZE)
        self.label.setPixmap(QPixmap(self.image_route))
        self.label.setScaledContents(True)
        self.label.setVisible(True)
        self.label.setStyleSheet("""
        QLabel {
            background-color: transparent;
            }
        """)

        self.center = (0, 0)
        self.limit_x = limit_x
        self.limit_y = p.KEY_ZONE_YLIMIT

        self.__position = (0, 0)
        self.position = (
            p.KEY_ZONE_LANES[self.arrowdir], p.KEY_ZONE_LANE_HEIGHT)

        self.label.show()
        self.start()

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, valor):
        self.__position = valor
        self.update_pos.emit(self.label, *self.position)

    def run(self):
        while self.position[0] < self.limit_x \
                and self.position[1] < self.limit_y:
            sleep(0.01)
            new_x = self.position[0]
            new_y = self.position[1] + 1
            self.center = ((new_x + 60)/2, (new_y + 60)/2)
            self.position = (new_x, new_y)

        if self.position[1] == self.limit_y:
            self.label.setVisible(False)
            self.exit()
            self.kill_move.emit(self)
            # print("Se acabo")


# Moves arrow within the RythmZone and checks if moves are correctly performed
class RythmZone(QObject):
    move_score = pyqtSignal(bool, str)
    pengu_move = pyqtSignal(str)
    neutral_pengu = pyqtSignal()

    # Receives instance of GameWindow as parent
    def __init__(self, parent):
        super().__init__()
        self.pasos = []
        self.game_window = parent
        self.game_window.dancemove.connect(self.check_dancemove)

    # Creates arrow as a QThread, connects signals to arrow
    def new_arrow(self):
        new_arrow = DanceMove(
            self.game_window, self.game_window.width(), self.game_window.height())
        new_arrow.update_pos.connect(self.update_label)
        new_arrow.kill_move.connect(self.delete_move)
        self.pasos.append(new_arrow)

    # Moves the label within the dancezone inside the GameWindow
    def update_label(self, label, x, y):
        label.move(x, y)

    # removes QThread corresponding to the arrow
    def delete_move(self, move):
        self.pasos.remove(move)

    # checks visually that the key was correctly pressed
    def check_dancemove(self, rect):
        valid_move = False
        if self.pasos:
            for paso in self.pasos:
                if rect.intersected(QRect(paso.position[0], paso.position[1],
                                          p.ARROW_SIZE, p.ARROW_SIZE)) and paso.label.isVisible():
                    valid_move = True
                    paso.label.setVisible(False)
                    self.move_score.emit(True, paso.arrowtype)
                    self.pengu_move.emit(paso.arrowdir)
                    # self.neutral_pengu.emit()
                    break
            if not valid_move:
                self.move_score.emit(False, paso.arrowtype)
        else:
            self.move_score.emit(False, "normal")


if __name__ == '__main__':
    app = QApplication([])
    form = VentanaZonaRitmo()
    sys.exit(app.exec_())
