import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from MainWindow_V2 import Ui_MainWindow


class Main_window(QMainWindow):
    def __int__(self):
        self.ui = Ui_MainWindow()
        super.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Main_window()
    window.show()

    sys.exit(app.exec_())