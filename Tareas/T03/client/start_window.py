import os
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

window_name, base_class = uic.loadUiType(os.path.join('UI', 'StartWindow.ui'))


def hook(type_error, traceback):
    print(type_error)
    print(traceback)


class StartWindow(window_name, base_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)




if __name__ == "__main__":
    app = QApplication([])
    start_window = StartWindow()
    start_window.show()
    sys.exit(app.exec_())
