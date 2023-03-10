import json
import os

# from docx import Document

BASE_DIR = os.getcwd()
DOC_NAME = 'SETTINGS.json'

# Создание дополнительных директории, если их не существует

paths = [
    os.path.join(BASE_DIR, 'Выгрузка'),
    os.path.join(BASE_DIR, 'Выгрузка', 'Опросные листы'),
    os.path.join(BASE_DIR, 'Шаблоны')
]

for path in paths:
    if not os.path.exists(path):
        os.makedirs(path)

# TODO: Добавить провеку существования дирректории и файлов, указанных в SETTINGS
# TODO: Добавить проверку имени файлов из SETTINGS (удаление запрещенных символов)
# TODO: Создать singlton-класс для SETTINGS с методами чтения значения из json-файла, и сохранения в файл!

DEFAULT_SETTINGS = {

    # Ссылки на базы
    "link_database": "",
    "link_reference_database": "",

    # Директории для сохранения
    "dir_shared_save_directory": paths[0],
    "dir_ol_save_directory": paths[1],
    "dir_tsp_save_directory": paths[0],
    "dir_io_save_directory": paths[0],
    "dir_kj_save_directory": paths[0],
    "dir_specifaication_save_directory": paths[0],

    # Директории для шаблонов
    "file_dir_temperature_template": "",
    "file_dir_pressure_template": "",
    "file_dir_flow_template": "",
    "file_dir_level_template": "",
    "file_dir_analyzer_template": "",
    "file_dir_control_valve_template": "",
    "file_dir_shut_off_valve_template": "",
    "file_dir_environments_descriptions": "",
    "file_dir_tsp_template": "",
    "file_dir_io_template": "",
    "file_dir_kj_template": "",
    "file_dir_specification_template": "",
    "file_dir_all_template": "",

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


# def create_json_file(path, keys):
#     # Если .json файл существует
#
#     if os.path.exists(path):
#         with open(path, 'r', encoding='cp1251') as file:
#             json_file = json.load(file)
#
#             # Проверка ключей полученного dict
#
#             if set(json_file.keys()) == keys:
#                 return json_file
#                 # Если ключи не соответствуют ключам из дефолных настроек
#             else:
#                 print('Файл SETTINGS.json содержит некоректные ключи')
#                 return dict.fromkeys(keys)

def create_json_file(path, keys):
    # Если .json файл существует

    if os.path.exists(path):
        with open(path, 'r', encoding='cp1251') as file:
            json_file = json.load(file)

            # Проверка ключей полученного dict
            # reading_keys = set(json_file.keys())

            # Удаляем ключи, которых нет в дефолтных настройках
            # for key in set(json_file.keys()):
            #     if key not in keys:
            #         json_file.pop(key)

            # Добавляем ключи из дефолных настроек, которые отсутстуют в прочитанном json
            for key in keys:
                if key not in set(json_file.keys()):
                    json_file.update({key: DEFAULT_SETTINGS[key]})

            return json_file

            # if set(json_file.keys()) == keys:
            #     return json_file
            #     # Если ключи не соответствуют ключам из дефолных настроек
            # else:
            #     print('Файл SETTINGS.json содержит некоректные ключи')
            #     return dict.fromkeys(keys)


    # Если .json файл не существует

    else:
        return DEFAULT_SETTINGS


def save_json_file(path_to_file, dictionary):
    with open(path_to_file, 'w') as f:
        json.dump(dictionary, f, cls=None, ensure_ascii=False, sort_keys=False, indent=4, separators=(',', ': '))
        # json.dump(dictionary, f, ensure_ascii=False)


# full_dir_all_settings = os.path.join(BASE_DIR, DOC_NAME)

# SETTINGS = create_json_file(os.path.join(BASE_DIR, DOC_NAME), PATH_KEYS)
SETTINGS = create_json_file(os.path.join(BASE_DIR, DOC_NAME), set(DEFAULT_SETTINGS.keys()))

# print('')
# a = SETTINGS['template_temperature']
# print(a['Позиция'])

# save_json_file(os.path.join(BASE_DIR, DOC_NAME), SETTINGS)
# print('')
