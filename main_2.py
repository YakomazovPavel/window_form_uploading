import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from MainWindow_V2 import Ui_MainWindow
from PySide6 import QtUiTools
from paths import BASE_DIR, ALL_PATHS, save_all_paths

# Добавить переменную, хранящую последний указанный путь пользователем (отрезать файл на конце, если указывался шаблон)


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.last_path = BASE_DIR
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Меню выбора дирректории со стандартными именами шаблонов
        self.ui.action_select_many_templates.triggered.connect(
            lambda: self.select_many_templates)

        # Меню выбора файла шаблона ОЛ
        self.ui.action_select_temperature_template.triggered.connect(
            lambda: self.select_template(key="file_dir_temperature_template"))

        self.ui.action_select_pressure_template.triggered.connect(
            lambda: self.select_template(key="file_dir_pressure_template"))

        self.ui.action_select_flow_template.triggered.connect(
            lambda: self.select_template(key="file_dir_flow_template"))

        self.ui.action_select_level_template.triggered.connect(
            lambda: self.select_template(key="file_dir_level_template"))

        self.ui.action_select_analyzer_template.triggered.connect(
            lambda: self.select_template(key="file_dir_analyzer_template"))
        
        self.ui.action_select_control_valve_template.triggered.connect(
            lambda: self.select_template(key="file_dir_control_valve_template"))
        
        self.ui.action_select_shut_off_valve_template.triggered.connect(
            lambda: self.select_template(key="file_dir_shut_off_valve_template"))

        self.ui.action_select_environments_descriptions.triggered.connect(
            lambda: self.select_template(key="file_dir_environments_descriptions"))
        
        self.ui.action_select_tsp_template.triggered.connect(
            lambda: self.select_template(key="file_dir_tsp_template"))

        self.ui.action_select_io_template.triggered.connect(
            lambda: self.select_template(key="file_dir_io_template"))

        self.ui.action_select_kj_template.triggered.connect(
            lambda: self.select_template(key="file_dir_kj_template"))

        self.ui.action_select_specification_template.triggered.connect(
            lambda: self.select_template(key="file_dir_specification_template"))
        

        # Меню выбора директории для сохранения
        self.ui.action_select_shared_save_directory.triggered.connect(
            lambda: self.select_directory(key="dir_shared_save_directory"))

        self.ui.action_select_ol_save_directory.triggered.connect(
            lambda: self.select_directory(key="dir_ol_save_directory"))

        self.ui.action_select_tsp_save_directory.triggered.connect(
            lambda: self.select_directory(key="dir_tsp_save_directory"))

        self.ui.action_select_io_save_directory.triggered.connect(
            lambda: self.select_directory(key="dir_io_save_directory"))
            
        self.ui.action_select_kj_save_directory.triggered.connect(
            lambda: self.select_directory(key="dir_kj_save_directory"))

        self.ui.action_select_specifaication_save_directory.triggered.connect(
            lambda: self.select_directory(key="dir_specifaication_save_directory"))


    # Выбор шаблона
    def select_template(self, key):
        dir = QFileDialog.getOpenFileName(self, "Open Directory", self.last_path, "Word (*.docx)")
        ALL_PATHS[key] = dir[0]
        self.last_path = os.path.split(dir[0])[0]
        # print(self.last_path)


    # Выбор нескольких шаблонов
    def select_many_templates(self):

        # Пользователь выбирает директорию, в которой содержаться шаблоны со стандартными названиями
        dir = QFileDialog.getExistingDirectory(self, "Open Directory", self.last_path)
        self.last_path = dir
        default_templates_names = {
            "temperature" :              ["Температура", "температура", "Temperature", "temperature"],
            "pressure" :                 ["Давление", "давление", "Pressure", "pressure"],
            "flow" :                     ["Расход", "расход", "Flow", "flow"],
            "level" :                    ["Уровень", "уровень", "Level", "level"],
            "analyzer" :                 ["Анализатор", "анализатор", "Analyzer", "analyzer"],
            "control_valve" :            ["Регулирующий клапан", "регулирующий клапар", "ЗРА", "зра"],
            "shut_off_valve" :           ["Отсечной клапан", "отсечной клапан", "Задвижка", "задвижка", "ЗРА", "зра"],
            "environments_descriptions" :["Среды", "среды", "Среда", "среда"],
            "io" :                       ["ИО", "ио", "Информационное обеспечение", "информационное обеспечение"],
            "tsp" :                      ["ТСП", "тсп", "Таблица соединений и подключений", "таблица соединений и подключений"],
            "kj" :                       ["КЖ", "кж", "Кабельный журнал", "кабельный журнал"],
            "specification" :            ["СП", "сп", "Спецификация", "спецификация"],
        }
        # TODO:
        # Описать поиск всех возможных названий файла шаблона для конкретного типа файла
        # В цикле пройтись по всем ключам
        # Во вложенном цикле пройтись по всем синонимам названия файла
        # Если такой файл существует в указанном пути, записать путь к шаблону в ALL_PATHS

        if (os.path.exists(os.path.join(dir, "Температура.docx")) or 
            os.path.exists(os.path.join(dir, "температура.docx"))):
            ALL_PATHS["file_dir_temperature_template"] = ""
        print(self.last_path)

    
    # Выбор общей дирректории
    def select_directory(self, key):
        dir = QFileDialog.getExistingDirectory(self, "Open Directory", self.last_path)
        ALL_PATHS[key] = dir
        self.last_path = dir
        # print(self.last_path)

    
    # Обработка закрытия приложения
    def closeEvent(self, event):
        print("Application is closed")
        save_all_paths()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
