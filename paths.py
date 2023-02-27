import json
import os

from docx import Document

BASE_DIR = os.getcwd()
DOC_NAME = 'SETTINGS.json'

# TODO: Добавить провеку существования дирректории и файлов
# TODO: Добавить проверку имени файлов (удаление запрещенных символов)
# TODO: Создать dict с дефолтными значениями
# TODO: Осуществлять проверку построчно (по ключам), если не удовлетворяет условию заменить это значение на дефолтное
# TODO: Создать singlton-класс для SETTINGS с методами чтения значения из json-файла, и сохранения в файл

DEFAULT_SETTINGS = {
# Пути для дирректорий сохранения
    "dir_shared_save_directory": os.path.join(BASE_DIR, "Выгрузка", "Выгрузка"),
    "dir_ol_save_directory": os.path.join(BASE_DIR, "Выгрузка", "Выгрузка", "Опросные листы"),
    "dir_tsp_save_directory": os.path.join(BASE_DIR, "Выгрузка", "Выгрузка"),
    "dir_io_save_directory": os.path.join(BASE_DIR, "Выгрузка", "Выгрузка"),
    "dir_kj_save_directory": os.path.join(BASE_DIR, "Выгрузка", "Выгрузка"),
    "dir_specifaication_save_directory": os.path.join(BASE_DIR, "Выгрузка", "Выгрузка"),

    # Пути для файлов шаблонов
    "file_dir_temperature_template": os.path.join(BASE_DIR, "Выгрузка", "Выгрузка", "Опросные листы", "Температура.docx"),
    "file_dir_pressure_template": os.path.join(BASE_DIR, "Выгрузка", "Выгрузка", "Опросные листы", "Давление.docx"),
    "file_dir_flow_template": os.path.join(BASE_DIR, "Выгрузка", "Выгрузка", "Опросные листы", "Расход.docx"),
    "file_dir_level_template": os.path.join(BASE_DIR, "Выгрузка", "Выгрузка", "Опросные листы", "Уровень.docx"),
    "file_dir_analyzer_template": "",
    "file_dir_control_valve_template": "",
    "file_dir_shut_off_valve_template": "",
    "file_dir_environments_descriptions": os.path.join(BASE_DIR, "Выгрузка", "Выгрузка", "Опросные листы", "Среды.docx"),
    "file_dir_tsp_template": os.path.join(BASE_DIR, "Выгрузка", "Шаблоны", "ТСП.docx"),
    "file_dir_io_template": os.path.join(BASE_DIR, "Выгрузка", "Шаблоны", "ИО.docx"),
    "file_dir_kj_template": os.path.join(BASE_DIR, "Выгрузка", "Шаблоны", "КЖ.docx"),
    "file_dir_specification_template": os.path.join(BASE_DIR, "Выгрузка", "Шаблоны", "Спецификация.docx"),

    # Имена для выгружаемых файлов
    "file_name_temperature_ol": "193-РП-АТХ1.ОЛ1",
    "file_name_pressure_ol": "193-РП-АТХ1.ОЛ2",
    "file_name_flow_ol": "193-РП-АТХ1.ОЛ3",
    "file_name_level_ol": "193-РП-АТХ1.ОЛ4",
    "file_name_analyzer_ol": "",
    "file_name_control_valve_ol": "",
    "file_name_shut_off_valve_ol": "",
    "file_name_tsp": "193-РП-АТХ2.С6",
    "file_name_io": "193-РП-АТХ2.В1",
    "file_name_kj": "193-РП-АТХ1.КЖ",
    "file_name_specification": "193-РП-АТХ1.СО",

    # Шаблоны
    "template_temperature": "",
    "template_pressure": "",
    "template_flow": "",
    "template_level": "",
    "template_control_valve": "",
    "template_shut_off_valve": "",
    "template_tsp": "",
    "template_io": "",
    "template_kj": "",
    "template_specification": ""
}

PATH_KEYS = (

    # Пути для дирректорий сохранения
    "dir_shared_save_directory",
    "dir_ol_save_directory",
    "dir_tsp_save_directory",
    "dir_io_save_directory",
    "dir_kj_save_directory",
    "dir_specifaication_save_directory",

    # Пути для файлов шаблонов
    "file_dir_temperature_template",
    "file_dir_pressure_template",
    "file_dir_flow_template",
    "file_dir_level_template",
    "file_dir_analyzer_template",
    "file_dir_control_valve_template",
    "file_dir_shut_off_valve_template",
    "file_dir_environments_descriptions",
    "file_dir_tsp_template",
    "file_dir_io_template",
    "file_dir_kj_template",
    "file_dir_specification_template",

    # Имена для выгружаемых файлов
    "file_name_temperature_ol",
    "file_name_pressure_ol",
    "file_name_flow_ol",
    "file_name_level_ol",
    "file_name_analyzer_ol",
    "file_name_control_valve_ol",
    "file_name_shut_off_valve_ol",
    "file_name_tsp",
    "file_name_io",
    "file_name_kj",
    "file_name_specification",

    # Шаблоны
    "template_temperature",
    "template_pressure",
    "template_flow",
    "template_level",
    "template_control_valve",
    "template_shut_off_valve",
    "template_tsp",
    "template_io",
    "template_kj",
    "template_specification"
)


def create_json_file(path, keys):
    # Если .json файл существует

    if os.path.exists(path):
        with open(path, 'r', encoding='cp1251') as file:
            json_file = json.load(file)

            # Проверка ключей полученного dict

            if tuple(json_file.keys()) == keys:
                return json_file
                # Если ключи не соответствуют кортежу
            else:
                return dict.fromkeys(keys)

    # Если .json файл не существует

    else:
        return dict.fromkeys(keys)


def save_json_file(path_to_file, dictionary):
    with open(path_to_file, 'w') as f:
        # json.dump(dictionary, f, cls=None, ensure_ascii=False, sort_keys=False, indent=4, separators=(',', ': '))
        json.dump(dictionary, f, ensure_ascii=False)


# full_dir_all_settings = os.path.join(BASE_DIR, DOC_NAME)

SETTINGS = create_json_file(os.path.join(BASE_DIR, DOC_NAME), PATH_KEYS)
# a = SETTINGS['template_temperature']
# print(a['Позиция'])

# save_json_file(os.path.join(BASE_DIR, DOC_NAME), SETTINGS)
# print('')
