import sys
import os
from time import sleep
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QComboBox
from PyQt5.QtCore import pyqtSignal, QRect, QObject
from PyQt5.QtGui import QPixmap
import parameters as p
from frontend.rythm_zone import RythmZone

window_name, base_class = uic.loadUiType(os.path.join('UI', 'GameWindow.ui'))


def hook(type_error, traceback):
    print(type_error)
    print(traceback)

# Front-end de la ventana de juego
# No incluye las flechas de la cancion actual, las cuales se procesan en rythm_zone.py
# Mueve sprites si es necesario, actualiza números como combos y barra de progreso


class GameWindow(window_name, base_class):

    dancemove = pyqtSignal(QRect)
    start_round_signal = pyqtSignal(str, str, QObject)
    openwindow_signal = pyqtSignal(str)
    reset_game_signal = pyqtSignal(str)
    move_pengu_sprite = pyqtSignal(str)
    neutral_pengu_sprite = pyqtSignal()
    sudden_quit = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.widget.isactive = False
        self.widget_2.isactive = False
        self.widget_3.isactive = False
        self.widget_4.isactive = False
        self.move_pengu_sprite.connect(self.move_pengu)
        self.neutral_pengu_sprite.connect(self.neutral_pengu_move)
        self.openwindow_signal.connect(self.start_game)
        self.pushButton_roundstart.clicked.connect(self.start_round)
        self.pushButton_quit.clicked.connect(self.sudden_quit)

        for song in os.listdir(p.SONG_MAIN_DIR):
            self.songbox.addItem(song)

    def start_game(self, name):
        self.reset_game_signal.emit(name)
        self.show()

    def start_round(self):
        rythmzone = RythmZone(self)
        errormessage = QMessageBox()
        errormessage.setText("Le falta seleccionar una canción o dificultad!")

        song = ""
        difficulty = str(self.comboBox_2.currentText())
        song = str(self.songbox.currentText())
        if difficulty not in p.GAME_ZONE_SPEED:
            errormessage.exec()
        else:
            self.start_round_signal.emit(song, difficulty, rythmzone)

    def move_pengu(self, direction):
        sprite_route = p.PENGU_SPRITES["amarillo," + direction]
        self.active_pengu.setPixmap(QPixmap(sprite_route))

    def neutral_pengu_move(self):
        sprite_route = p.PENGU_SPRITES["amarillo," + "neutral"]
        self.active_pengu.setPixmap(QPixmap(sprite_route))

    def send_dancemove(self, keycell):
        self.dancemove.emit(keycell.geometry())

    def keyPressEvent(self, event):
        key_pressed = event.text().upper()
        if key_pressed in p.KEYS_AVAILABLE:
            self.color_key(p.KEYS_AVAILABLE.index(key_pressed))

    def keyReleaseEvent(self, event):
        key_released = event.text().upper()
        if key_released in p.KEYS_AVAILABLE:
            self.decolor_key(p.KEYS_AVAILABLE.index(key_released))

    def color_key(self, keypressed):
        # Limpiar esto con parametros
        if keypressed == 0:
            self.widget.setStyleSheet("""
        QWidget {
            background-color: rgb(255, 69, 0);
            }
        """)
            self.widget.isactive = True
            self.send_dancemove(self.widget)
        elif keypressed == 1:
            self.widget_2.setStyleSheet("""
        QWidget {
            background-color: rgb(255, 69, 0);
            }
        """)
            self.widget_2.isactive = True
            self.send_dancemove(self.widget_2)
        elif keypressed == 2:
            self.widget_3.setStyleSheet("""
        QWidget {
            background-color: rgb(255, 69, 0);
            }
        """)
            self.widget_3.isactive = True
            self.send_dancemove(self.widget_3)
        elif keypressed == 3:
            self.widget_4.setStyleSheet("""
        QWidget {
            background-color: rgb(255, 69, 0);
            }
        """)
            self.widget_4.isactive = True
            self.send_dancemove(self.widget_4)

    def decolor_key(self, keypressed):
        if keypressed == 0:
            self.widget.setStyleSheet("""
        QWidget {
            background-color: rgb(85, 170, 225);
            }
        """)
            self.widget.isactive = False
        elif keypressed == 1:
            self.widget_2.setStyleSheet("""
        QWidget {
            background-color: rgb(85, 170, 225);
            }
        """)
            self.widget_2.isactive = False
        elif keypressed == 2:
            self.widget_3.setStyleSheet("""
        QWidget {
            background-color: rgb(85, 170, 225);
            }
        """)
            self.widget_3.isactive = False
        elif keypressed == 3:
            self.widget_4.setStyleSheet("""
        QWidget {
            background-color: rgb(85, 170, 225);
            }
        """)
            self.widget_4.isactive = False

    def update_currentcombo_layout(self, mult):
        self.label_combo.setText(str(mult))

    def update_maxcombo_layout(self, mult):
        self.label_max_combo.setText(str(mult))

    def update_progressBar(self, percentage):
        self.progressBar.setValue(percentage)

    def update_ApprovalBar(self, percentage):
        self.progressBar_2.setValue(percentage)


if __name__ == '__main__':
    app = QApplication([])
    form = DanceZoneWindow()
    form.show()
    print(form.widget.geometry())
    sys.exit(app.exec_())
