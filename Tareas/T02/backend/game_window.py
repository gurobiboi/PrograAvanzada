import sys
import os
from math import floor
from time import sleep
from PyQt5.QtCore import pyqtSignal, QTimer, QObject
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QHBoxLayout,
                             QVBoxLayout, QPushButton)
from PyQt5.QtGui import QPixmap
import parameters as p
from PyQt5.QtMultimedia import QSound


# Se controla todo el backend de la ventaja de juego.
# guarda puntaje, dinero, progreso en canciones, etc.
# mantiene los QThreads de las flechas de juego


# Parte de backend del juego en general
class CurrentGame(QObject):

    signal_start_song = pyqtSignal(str, str)
    update_max_combo = pyqtSignal(int)
    update_current_combo = pyqtSignal(int)
    update_progress = pyqtSignal(int)
    update_approval = pyqtSignal(int)
    round_summary_signal = pyqtSignal(int, int, int, int, int, str)
    close_game_win = pyqtSignal()
    write_score = pyqtSignal(str, int)
    pengu_move_signal = pyqtSignal(str)
    pengu_neutral_signal = pyqtSignal()
    back_to_main_menu = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.money = 0
        self.score = 0
        self.name = None

    def reset_user(self, name):
        self.name = name
        self.money = 0
        self.score = 0

    def update_score(self, approval, arrow_sum, maxcombo, wrongmoves, songdif):
        song_score = maxcombo + arrow_sum * p.ARROW_BASE_POINTS
        self.score += song_score
        print(f"Lograste {song_score} ptos en la canción!")
        self.round_summary_signal.emit(
            self.score, song_score, maxcombo, wrongmoves, approval, songdif)

    def start_song(self, song, diff, rythmzone):
        print(diff)
        song = CurrentSong(song, diff)
        zone = rythmzone
        zone.pengu_move = self.pengu_move_signal
        zone.neutral_pengu = self.pengu_neutral_signal
        song.new_arrow_signal.connect(zone.new_arrow)
        song.current_combo_signal = self.update_current_combo
        song.max_combo_signal = self.update_max_combo
        song.progress_bar_signal = self.update_progress
        song.approval_bar_signal = self.update_approval
        song.song_ended_signal.connect(self.update_score)
        zone.move_score.connect(song.update_score)
        song.startsong()
        song.exec_()

    def endgame(self):
        self.write_score.emit(self.name, self.score)
        self.close_game_win.emit()
        self.back_to_main_menu.emit()

# Parte del backend de la cancion actual que se está jugando (o la ronda actual)


class CurrentSong(QObject):

    new_arrow_signal = pyqtSignal()
    current_combo_signal = pyqtSignal(int)
    max_combo_signal = pyqtSignal(int)
    progress_bar_signal = pyqtSignal(int)
    approval_bar_signal = pyqtSignal(int)
    song_ended_signal = pyqtSignal(int, int, int, int, str)

    def __init__(self, song, songdiff):
        super().__init__()
        self.current_time = 0
        self.dif = songdiff
        self.time_max = p.GAME_ZONE_DURATION[songdiff] + p.DELAY_END_ROUND
        self.timer = QTimer()
        self.timer.setInterval(p.GAME_ZONE_SPEED[songdiff])
        self.timer.timeout.connect(self.create_arrow)
        self.right_moves = 0
        self.wrong_moves = 0
        self.current_combo = 0
        self.max_combo = 0
        self.arrow_sum = 0
        self.total_moves = 0
        self.arrowtraveltime = p.ARROW_TRAVEL_TIME * 1000/1000
        self.songroute = os.path.join(p.SONG_MAIN_DIR, song)
        self.sound = QSound(self.songroute)
        self.sound.play()

    # Sends signal to RythmZone() create arrow
    def create_arrow(self):
        songtime = self.time_max - p.DELAY_END_ROUND
        if self.current_time <= songtime:
            self.new_arrow_signal.emit()
            self.current_time += 1
            self.total_moves += 1

        if songtime < self.current_time <= self.time_max:
            self.current_time += 1

        if self.arrowtraveltime < self.current_time <= songtime + self.arrowtraveltime:
            self.progress_bar_signal.emit(
                int(100*(self.current_time-self.arrowtraveltime)/songtime))

        if self.current_time == self.time_max:
            self.end_round()

    def startsong(self):
        self.progress_bar_signal.emit(0)
        self.approval_bar_signal.emit(0)
        self.max_combo_signal.emit(0)
        self.current_combo_signal.emit(0)
        self.timer.start()

    def update_score(self, good, arrow_type):
        if good:
            self.right_moves += 1
            self.update_combo(True)
            if arrow_type == "normal" or arrow_type == "freeze":
                self.arrow_sum += 1
            elif arrow_type == "x2":
                self.arrow_sum += p.X2_ARROW_VALUE
            else:
                self.arrow_sum += p.GOLDEN_ARROW_VALUE
        else:
            self.wrong_moves += 1
            self.update_combo(False)

        score = floor(p.ROUND_POINTS_BASE*(self.right_moves -
                                           self.wrong_moves)/self.total_moves)
        self.approval_bar_signal.emit(int(score))

    def update_combo(self, hit):
        if hit:
            self.current_combo += 1
            if self.current_combo > self.max_combo:
                self.max_combo = self.current_combo
                self.max_combo_signal.emit(self.max_combo)
        else:
            self.current_combo = 0
        self.current_combo_signal.emit(self.current_combo)

    def end_round(self):
        self.timer.stop()
        self.sound.stop()
        score = floor(p.ROUND_POINTS_BASE*(self.right_moves -
                                           self.wrong_moves)/(self.total_moves))
        self.approval_bar_signal.emit(int(score))
        self.song_ended_signal.emit(
            int(score), self.arrow_sum, self.max_combo, self.wrong_moves, self.dif)
