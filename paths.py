import json
import os


BASE_DIR = os.getcwd()
DOC_NAME = 'ALL_PATHS.json'
ALL_PATHS = {}
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
	"file_dir_specification_template"
)

full_dir_all_paths = os.path.join(BASE_DIR, DOC_NAME)


# Если .json файл существует

if os.path.exists(full_dir_all_paths):
	with open(full_dir_all_paths, 'r') as file:
		ALL_PATHS = json.load(file)
		# print(ALL_PATHS)

		# Проверка ключей полученного dict

		if not tuple(ALL_PATHS.keys()) == PATH_KEYS:

			# Если ключи не соответствуют кортежу PATH_KEYS

			ALL_PATHS = dict.fromkeys(PATH_KEYS)

# Если .json файл не существует

else:
	ALL_PATHS = dict.fromkeys(PATH_KEYS)


# Сохранить переменную ALL_PATHS в .json файл

def save_all_paths():
	with open(full_dir_all_paths, 'w') as f:
		json.dump(ALL_PATHS, f)