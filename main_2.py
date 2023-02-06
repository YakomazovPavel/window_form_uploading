import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from MainWindow_V2 import Ui_MainWindow
from PySide6 import QtUiTools
from paths import BASE_DIR, ALL_PATHS, save_all_paths


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.action_select_temperature_template.triggered.connect(
            # self.action_select_temperature_template)
            lambda: self.action_select_temperature_template(key="file_dir_temperature_template"))
        self.ui.action_select_shared_save_directory.triggered.connect(
            self.action_select_shared_save_directory)

    def action_select_temperature_template(self, key):
        dir = QFileDialog.getOpenFileName(
            self, "Open Directory", BASE_DIR, "Word (*.docx)")
        print(dir[0])
        ALL_PATHS[key] = dir[0]
        save_all_paths()


    def action_select_shared_save_directory(self):
        dir = QFileDialog.getExistingDirectory(
            self, "Open Directory", BASE_DIR)
        print(dir)
        ALL_PATHS["dir_shared_save_directory"] = dir
        save_all_paths()



if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())