import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from MainWindow_V2 import Ui_MainWindow
from PySide6 import QtUiTools


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())