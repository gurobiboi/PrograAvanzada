import sys
import os
from time import sleep
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.QtCore import pyqtSignal, QRect, QObject
import parameters as p
from frontend.rythm_zone import RythmZone

window_name, base_class = uic.loadUiType(os.path.join('UI', 'SummaryWin.ui'))


def hook(type_error, traceback):
    print(type_error)
    print(traceback)


class SummaryWindow(window_name, base_class):
    openwindow_signal = pyqtSignal(int, int, int, int, int, str)
    endgame = pyqtSignal()
    mainwindow_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.openwindow_signal.connect(self.give_summary)

    def give_summary(self, currentscore, songscore, combo, wrongmoves, approval, songdif):
        self.songscore.setText(str(songscore))
        self.currentscore.setText(str(currentscore))
        self.combo.setText("X" + str(combo))
        self.wrongmoves.setText(str(wrongmoves))
        if approval >= 0:
            self.approval.setText("%" + str(approval))
        else:
            self.approval.setText("%" + "0")

        if approval >= p.GAME_MIN_APPROVAL[songdif]:
            self.message.setText(
                "Tuviste la aprobación necesaria, puedes seguir jugando!")
            self.backButton.clicked.connect(self.close)
        else:
            self.message.setText(
                "No obtuviste la aprobación necesaria, termina el juego :(")
            self.backButton.clicked.connect(self.quitgame)

        self.show()

    def quitgame(self):
        self.close()
        self.endgame.emit()
        self.mainwindow_signal.emit()
