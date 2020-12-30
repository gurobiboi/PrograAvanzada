import parameters as p
from frontend.summary_window import SummaryWindow
from frontend.rythm_zone import RythmZone
from backend.game_window import CurrentGame, CurrentSong
from frontend.rankings_window import RankingsWindow
from frontend.game_window import GameWindow
from frontend.start_window import StartWindow
from PyQt5.QtWidgets import QApplication
import sys
sys.path.append("..")
sys.path.append("..")


def hook(type_error, traceback):
    print(type_error)
    print(traceback)


if __name__ == '__main__':
    sys.__excepthook__ = hook
    app = QApplication([])
    start_win = StartWindow()
    rankings_win = RankingsWindow()
    game_win = GameWindow()
    game_logic = CurrentGame()
    summ_win = SummaryWindow()

    start_win.rankings_signal = rankings_win.openwindow_signal
    rankings_win.back_signal = start_win.openwindow_signal

    start_win.gamestart_signal = game_win.openwindow_signal
    game_win.reset_game_signal.connect(game_logic.reset_user)

    game_logic.close_game_win.connect(game_win.close)
    game_logic.back_to_main_menu = start_win.openwindow_signal

    game_win.start_round_signal.connect(game_logic.start_song)
    game_logic.update_current_combo.connect(
        game_win.update_currentcombo_layout)
    game_logic.update_max_combo.connect(game_win.update_maxcombo_layout)
    game_logic.update_progress.connect(game_win.update_progressBar)
    game_logic.update_approval.connect(game_win.update_ApprovalBar)
    game_logic.round_summary_signal = summ_win.openwindow_signal

    summ_win.mainwindow_signal = start_win.openwindow_signal
    summ_win.endgame.connect(game_logic.endgame)
    game_win.sudden_quit.connect(game_logic.endgame)

    game_logic.write_score.connect(rankings_win.writescore)
    game_logic.pengu_move_signal.connect(game_win.move_pengu_sprite)
    game_logic.pengu_neutral_signal.connect(game_win.neutral_pengu_sprite)

    start_win.show()
    sys.exit(app.exec_())
