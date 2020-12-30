# Rankings window
import sys
import os
from time import sleep
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QLabel
from PyQt5.QtCore import pyqtSignal, QRect
import parameters as p


# Front-end de la ventana de rankings
# Actualiza labels de los scores cuando se llama la ventana

window_name, base_class = uic.loadUiType(
    os.path.join('UI', 'rankingsWindow.ui'))


def hook(type_error, traceback):
    print(type_error)
    print(traceback)


def clearLayout(layout):
    while layout.count():
        child = layout.takeAt(0)
        if child.widget():
            child.widget().deleteLater()


class RankingsWindow(window_name, base_class):

    openwindow_signal = pyqtSignal()
    back_signal = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.pushButton_back.clicked.connect(self.go_back)
        self.openwindow_signal.connect(self.readscores)

    def writescore(self, name, score):
        with open("rankings.txt", "a") as file:
            file.write(name + "," + str(score) + "\n")

    def readscores(self):
        clearLayout(self.scorelayout)
        rankings = []
        with open("rankings.txt", "r") as file:
            for line in file:
                rankings.append(line.strip("\n").split(","))
        print(rankings)
        rankings.sort(reverse=True, key=lambda x: int(x[1]))
        print(rankings)
        for i in range(min(len(rankings), p.RANKINGS_NUM)):
            score = QLabel()
            score.setText(rankings[i][0]+": "+rankings[i][1])
            score.setStyleSheet("""
        QWidget {
            font: 16pt "MS Shell Dlg 2";
            }
        """)
            self.scorelayout.addWidget(score)
        self.show()

    def go_back(self):
        self.hide()
        self.back_signal.emit()
