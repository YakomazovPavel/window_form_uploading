import copy

from connections import connectiondef
import pandas as pd
import numpy as np

from paths import SETTINGS


# Кастомная функция для группировки
def joinUniqu(x):
    uniqu = x.drop_duplicates()
    array = uniqu.values
    string = ''
    last = len(array) - 1
    for i in range(0, len(array)):
        string += str(array[i])
        if i != last:
            string += '\n'
    return string


# df1 = df1.groupby(by='A').agg({'B': joinUniqu, 'C': joinUniqu})


# templates = {
#     'Температура': {
#         'Позиция': (0, 4),
#         'Назначение': (1, 4),
#         'Место установки': (2, 4),
#         'Размер трубопровода': (3, 4),
#         # 'Материал трубопровода': (4, 4),
#         'Среда': (4, 4),
#         'Агрегатное состояние': (5, 4),
#         'T min': (6, 4),
#         'T max': (7, 4),
#         'T раб': (8, 4),
#         'Единицы измерения температуры': (8, 5),
#         'P min': (9, 4),
#         'P max': (10, 4),
#         'P раб': (11, 4),
#         'Единицы измерения давления': (11, 5),
#         'Плотность': (12, 4),
#         'Единицы измерения плотности': (12, 5),
#         'Вязкость': (13, 4),
#         'Единицы измерения вязкости': (13, 5),
#         'Агрессивность': (14, 4),
#         'Другие особые условия': (15, 4),
#         'Тип сенсора': (16, 4),
#         'Градуировка НСХ': (17, 4),
#         'Диаметр ЧЭ': (18, 4),
#         'Длина сенсора': (19, 4),
#         'Соединение с процессом чувствительного элемента': (20, 4),
#         'Температурная вставка (удлинитель)': (21, 4),
#         'Шкала прибора': (22, 4),
#         'Тип сигналов*': (23, 4),
#         'Напряжение питания': (24, 4),
#         'Схема подключения (сигнал)': (25, 4),
#         'Погрешность измерения': (26, 4),
#         'Взрывозащита*': (27, 4),
#         'Уровень безопасности SIL': (28, 4),
#         'Степень защиты': (29, 4),
#         'Тип корпуса': (30, 4),
#         'Материал корпуса': (31, 4),
#         'Тип защитной гильзы': (32, 4),
#         'Тип резьбы гильзы': (33, 4),
#         'Длина погружаемой части гильзы': (34, 4),
#         'Маркировка защитной гильзы': (35, 4),
#         'Местный индикатор': (36, 4),
#         'Кабельный ввод': (37, 4),
#         'Марка кабеля': (38, 4),
#         'Изготовитель': (39, 4),
#         'Модель': (40, 4),
#         'Примечание': (41, 4),
#     },
#     'Давление': {
#         'Позиция': (0, 4),
#         'Назначение': (1, 4),
#         'Место установки': (2, 4),
#         'Среда': (3, 4),
#         'Агрегатное состояние': (4, 4),
#         'T min': (5, 4),
#         'T max': (6, 4),
#         'T раб': (7, 4),
#         'Единицы измерения температуры': (7, 5),
#         'P min': (8, 4),
#         'P max': (9, 4),
#         'P раб': (10, 4),
#         'P стат': (11, 4),
#         'Перепад давления': (12, 4),
#         'Единицы измерения давления': (12, 5),
#         'Плотность': (13, 4),
#         'Единицы измерения плотности': (13, 5),
#         'Вязкость': (14, 4),
#         'Единицы измерения вязкости': (14, 5),
#         'Агрессивность': (15, 4),
#         'Другие особые условия': (16, 4),
#         'Измеряемый параметр': (17, 4),
#         'Шкала прибора': (18, 4),
#         'Тип сигналов*': (19, 4),
#         'Напряжение питания': (20, 4),
#         'Схема подключения (сигнал)': (21, 4),
#         'Погрешность измерения': (22, 4),
#         'Взрывозащита*': (23, 4),
#         'Степень защиты': (24, 4),
#         'Уровень безопасности SIL': (25, 4),
#         'Материал корпуса': (26, 4),
#         'Соединение с процессом': (27, 4),
#         'Мембранный разделитель': (28, 4),
#         'Подвод импульсных трубок': (29, 4),
#         'Сторона высокого давления': (30, 4),
#         'Тип вентильного блока': (31, 4),
#         'Тип резьбы вентильного блока для подключения импульсных линий / датчика': (32, 4),
#         'Тип дренажного соединения вентильного блока': (33, 4),
#         'Ниппель для присоединения импульсных линий': (34, 4),
#         'Местный индикатор': (35, 4),
#         'Комплект монтажных частей': (36, 4),
#         'Кабельный ввод': (37, 4),
#         'Марка кабеля': (38, 4),
#         'Изготовитель': (39, 4),
#         'Модель': (40, 4),
#         'Примечание': (41, 4),
#     },
#     'Расход': {
#         'Позиция': (0, 4),
#         'Назначение': (1, 4),
#         'Место установки': (2, 4),
#         'Размер трубопровода': (3, 4),
#         'Материал трубопровода': (4, 4),
#         'Среда': (5, 4),
#         'Агрегатное состояние': (6, 4),
#         'Q min': (7, 4),
#         'Q max': (8, 4),
#         'Q раб': (9, 4),
#         'Единицы измерения расхода': (9, 5),
#         'T min': (10, 4),
#         'T max': (11, 4),
#         'T раб': (12, 4),
#         'Единицы измерения температуры': (12, 5),
#         'P min': (13, 4),
#         'P max': (14, 4),
#         'P расч': (15, 4),
#         'P раб': (16, 4),
#         'Единицы измерения давления': (16, 5),
#         'Плотность': (17, 4),
#         'Единицы измерения плотности': (17, 5),
#         'Вязкость': (18, 4),
#         'Единицы измерения вязкости': (18, 5),
#         'Агрессивность': (19, 4),
#         'Другие особые условия': (20, 4),
#         'Метод измерения': (21, 4),
#         'Шкала прибора': (22, 4),
#         'Единицы измерения шкалы приборв': (22, 5),
#         'Погрешность': (23, 4),
#         'Тип сигналов*': (24, 4),
#         'Напряжение питания': (25, 4),
#         'Схема подключения (сигнал)': (26, 4),
#         'Местный индикатор': (27, 4),
#         'Кабельный ввод': (28, 4),
#         'Марка кабеля': (29, 4),
#         'Взрывозащита*': (30, 4),
#         'Степень защиты': (31, 4),
#         'Уровень безопасности SIL': (32, 4),
#         'Тип диафрагмы': (33, 4),
#         'Номер исполнения': (34, 4),
#         'Материал диафрагмы': (35, 4),
#         'Способ отбора давления': (36, 4),
#         'Тип фланцев': (37, 4),
#         'DN фланцев': (38, 4),
#         'PN фланцев, кгс/см2': (39, 4),
#         'Разделительные сосуды/мембраны/вентильные блоки': (40, 4),
#         'Комплект монтажных частей': (41, 4),
#         'Изготовитель': (42, 4),
#         'Модель': (43, 4),
#         'Примечание': (44, 4)
#     },
#     'Уровень': {
#         'Позиция': (0, 4),
#         'Назначение': (1, 4),
#         'Место установки': (2, 4),
#         'Тип прибора': (3, 4),
#         'Тип аппарата': (4, 4),
#         'Диаметр (длина) /Ширина /Высота аппарата': (5, 4),
#         'Выносная камера (штуцер) на аппарате': (6, 4),
#         'Длина камеры (штуцера) на аппарате': (7, 4),
#         'Диаметр камеры (штуцера) на аппарате': (8, 4),
#         'Среда верхней среды': (9, 4),
#         'Среда нижней среды': (10, 4),
#         'T min': (11, 4),
#         'T max': (12, 4),
#         'T раб': (13, 4),
#         'Единицы измерения температуры': (13, 6),
#         'P min': (14, 4),
#         'P max': (15, 4),
#         'P раб': (16, 4),
#         'Единицы измерения давления': (16, 6),
#         'Плотность верхней среды': (17, 4),
#         'Плотность нижней среды': (18, 4),
#         'Единицы измерения плотности верхней среды': (18, 6),
#         'Вязкость верхней среды': (19, 4),
#         'Вязкость нижней среды': (20, 4),
#         'Единицы измерения вязкости верхней среды': (20, 6),
#         'Агрессивность верхней среды': (21, 4),
#         'Агрессивность нижней среды': (22, 4),
#         'Другие особые условия верхней среды': (23, 4),
#         'L min': (24, 4),
#         'L max': (25, 4),
#         'Единицы измерения уровня': (25, 6),
#         'Длина чувствительного элемента': (26, 4),
#         'Подвод импульсных трубок': (27, 4),
#         'Сторона высокого давления': (28, 4),
#         'Тип фланцев / резьбы': (29, 4),
#         'DN фланцев': (30, 4),
#         'PN фланцев': (31, 4),
#         'Выносная камера в комплекте с прибором': (32, 4),
#         'Тип фланцев выносной камеры': (33, 4),
#         'DN фланцев выносной камеры': (34, 4),
#         'PN фланцев выносной камеры': (35, 4),
#         'Измеряемый параметр': (36, 4),
#         'Шкала прибора': (37, 4),
#         'Тип сигналов*': (38, 4),
#         'Напряжение питания': (39, 4),
#         'Схема подключения (сигнал)': (40, 4),
#         'Погрешность измерения': (41, 4),
#         'Взрывозащита*': (42, 4),
#         'Уровень безопасности SIL': (43, 4),
#         'Степень защиты': (44, 4),
#         'Материал корпуса': (45, 4),
#         'Ответный фланец / бобышка в комплекте': (46, 4),
#         'Тип вентильного блока': (47, 4),
#         'Тип резьбы вентильного блока под импульсные линии/датчик': (48, 4),
#         'Тип дренажного соединения вентильного блока': (49, 4),
#         'Ниппель для присоединения импульсных линий': (50, 4),
#         'Местный индикатор': (51, 4),
#         'Комплект монтажных частей': (52, 4),
#         'Кабельный ввод': (53, 4),
#         'Марка кабеля': (54, 4),
#         'Изготовитель': (55, 4),
#         'Модель': (56, 4),
#         'Примечание': (57, 4),
#     },
#     'Регулирующий клапан': {
#         'Позиция': (0, 4),
#         'Назначение': (1, 4),
#         'Место установки': (2, 4),
#         'Размер трубопровода': (3, 4),
#         'Материал трубопровода': (4, 4),
#         'Среда': (5, 4),
#         'Агрегатное состояние': (6, 4),
#         'Q min': (7, 4),
#         'Q max': (8, 4),
#         'Q раб': (9, 4),
#         'Единицы измерения расхода': (9, 5),
#         'T min': (10, 4),
#         'T max': (11, 4),
#         'T раб': (12, 4),
#         'Единицы измерения температуры': (12, 5),
#         'P min': (13, 4),
#         'P max': (14, 4),
#         'P раб': (15, 4),
#         'P расч': (16, 4),
#         'Падение давления на клапане (макс)': (17, 4),
#         'Единицы измерения давления': (17, 5),
#         'Рабочий диапазон регулирования': (18, 4),
#         'Единицы измерения диапазона регулирования': (18, 5),
#         'Плотность': (19, 4),
#         'Единицы измерения плотности': (19, 5),
#         'Вязкость': (20, 4),
#         'Единицы измерения вязкости': (20, 5),
#         'Агрессивность': (21, 4),
#         'Другие особые условия': (22, 4),
#         'Направление потока': (23, 4),
#         'Тип привода': (24, 4),
#         'Класс герметичности': (25, 4),
#         'Пропускная характеристика': (26, 4),
#         'Направление действия': (27, 4),
#         'Давление питающего воздуха': (28, 4),
#         'Положение при отсутствии воздуха/электропитания': (29, 4),
#         'Тип позиционера': (30, 4),
#         'Напряжение питания позиционера': (31, 4),
#         'Выходной сигнал позиционера': (32, 4),
#         'Взрывозащита позиционера': (33, 4),
#         'Степень защиты позиционера': (34, 4),
#         'Манометр позиционера': (35, 4),
#         'Кабельный ввод позиционера': (36, 4),
#         'Марка кабеля позиционера': (37, 4),
#         'Соединение с процессом': (38, 4),
#         'Тип фланцев': (39, 4),
#         'DN фланцев': (40, 4),
#         'PN фланцев': (41, 4),
#         'DN существующего клапана': (42, 4),
#         'PN существующего клапана': (43, 4),
#         'Изготовитель': (44, 4),
#         'Модель': (45, 4),
#         'Примечание': (46, 4)
#     },
#     'Задвижка': {
#         'Позиция': (0, 4),
#         'Назначение': (1, 4),
#         'Место установки': (2, 4),
#         'Размер трубопровода': (3, 4),
#         'Материал трубопровода': (4, 4),
#         'Среда': (5, 4),
#         'Агрегатное состояние': (6, 4),
#         'Q min': (7, 4),
#         'Q max': (8, 4),
#         'Q раб': (9, 4),
#         'Единицы измерения расхода': (9, 5),
#         'T min': (10, 4),
#         'T max': (11, 4),
#         'T раб': (12, 4),
#         'Единицы измерения температуры': (12, 5),
#         'P min': (13, 4),
#         'P max': (14, 4),
#         'P раб': (15, 4),
#         'P расч': (16, 4),
#         'Падение давления на клапане (макс)': (17, 4),
#         'Единицы измерения давления': (17, 5),
#         'Плотность': (18, 4),
#         'Единицы измерения плотности': (18, 5),
#         'Вязкость': (19, 4),
#         'Единицы измерения вязкости': (19, 5),
#         'Агрессивность': (20, 4),
#         'Другие особые условия': (21, 4),
#         'Направление потока': (22, 4),
#         'Класс герметичности': (23, 4),
#         'Тип привода': (24, 4),
#         'Давление питающего воздуха': (25, 4),
#         'Положение при отсутствии воздуха / электропитания': (26, 4),
#         'Время открытия / закрытия': (27, 4),
#         'Ручное управление': (28, 4),
#         'Уровень безопасности SIL': (29, 4),
#         'Напряжение питания': (30, 4),
#         'Взрывозащита': (31, 4),
#         'Степень защиты': (32, 4),
#         'Кабельный ввод (сигнал)': (33, 4),
#         'Марка кабеля (сигнал)': (34, 4),
#         'Тип конечного выключателя': (35, 4),
#         'Положение конечного выключателя': (36, 4),
#         'Взрывозащита конечного выключателя': (37, 4),
#         'Степень защиты конечного выключателя': (38, 4),
#         'Соединительная коробка конечного выключателя': (39, 4),
#         'Кабельный ввод конечного выключателя': (40, 4),
#         'Марка кабеля конечного выключателя': (41, 4),
#         'Соединение с процессом': (42, 4),
#         'Тип фланцев': (43, 4),
#         'DN фланцев': (44, 4),
#         'PN фланцев': (45, 4),
#         'DN существующего клапана': (46, 4),
#         'PN существующего клапана': (47, 4),
#         'Изготовитель': (48, 4),
#         'Модель': (49, 4),
#         'Примечание': (50, 4)
#     }
# }
def check_column_name(db_col_name, template_col_name):
    col_temp = np.array(list(template_col_name))
    mask = np.in1d(col_temp, db_col_name)
    error_col_name = col_temp[~mask]
    if len(error_col_name) > 0:
        print(f'В базе отсутствуют столбцы {error_col_name}')
        return True
    else:
        return False


def getTemptureForOL():
    pp = connectiondef('Перечень приборов')
    env = connectiondef('Среда')
    tempture = connectiondef('Температура')

    df_pp = pd.DataFrame(pp[1:], columns=pp[0]).fillna('')
    df_pp = df_pp[df_pp['Параметр'] == 'Температура']
    df_env = pd.DataFrame(env[1:], columns=env[0]).fillna('')
    df_tempture = pd.DataFrame(tempture[1:], columns=tempture[0]).fillna('')

    df = pd.merge(left=df_pp,
                  right=df_tempture,
                  how='left',
                  on='Позиция',
                  indicator=True,
                  suffixes=('_x', '')).drop(['_merge'], axis=1).reset_index(drop=True).fillna('')
    df['Примечание'] = df['Примечание'].astype('str') + ' ' + df['Примечание_x'].astype('str')
    df.replace('  ', '-', inplace=True)
    df.drop(df.filter(regex='_x$').columns, axis=1, inplace=True)

    df = pd.merge(left=df,
                  right=df_env,
                  how='left',
                  on='Идентификатор среды',
                  indicator=True,
                  suffixes=('', '_y')).drop(['_merge'], axis=1).reset_index(drop=True).fillna('')
    df.drop(df.filter(regex='_y$').columns, axis=1, inplace=True)
    df = df[(df['Необходимость проектирования'] == 'ЗАМ.') | (df['Необходимость проектирования'] == 'НОВ.')]
    df.replace('', '-', inplace=True)

    # Сортировка позиций для опросных листов

    df = df.sort_values(['Компрессор', 'Позиция'], ascending=[True, True]) \
        .reset_index(drop=True)

    df.reset_index(drop=False, inplace=True)

    # Определение номера первого листа
    shift_first_list = (df.shape[0] - 50) // 54
    if (df.shape[0] - 50) % 54 != 0:
        shift_first_list += 1

    df['index'] = df['index'] + 1
    df['Номер листа'] = df['index'] + 5 + shift_first_list
    df['Изменения'] = ''
    df_table_list_positions = df[['Изменения', 'index', 'Позиция', 'Номер схемы', 'Тип сенсора', 'Номер листа']].copy()
    # Проверка наличия всех столбцов из шаблона
    templates_key = SETTINGS['template_temperature'].keys()
    col_name = df.columns.values
    if check_column_name(col_name, templates_key):
        return
    else:
        df_ol_table = df[list(SETTINGS['template_temperature'].keys())].copy()
        return df_table_list_positions, df_ol_table


def getPressureForOL():
    pp = connectiondef('Перечень приборов')
    env = connectiondef('Среда')
    pressure = connectiondef('Давление')

    df_pp = pd.DataFrame(pp[1:], columns=pp[0]).fillna('-')
    df_pp = df_pp[df_pp['Параметр'] == 'Давление']
    df_env = pd.DataFrame(env[1:], columns=env[0]).fillna('-')
    df_pressure = pd.DataFrame(pressure[1:], columns=pressure[0]).fillna('-')

    df = pd.merge(left=df_pp,
                  right=df_pressure,
                  how='left',
                  on='Позиция',
                  indicator=True,
                  suffixes=('', '_y')).drop(['_merge'], axis=1).reset_index(drop=True).fillna('')
    df['Примечание'] = df['Примечание'].astype('str') + ' ' + df['Примечание_y'].astype('str')
    df.replace('  ', '-', inplace=True)
    df.drop(df.filter(regex='_y$').columns, axis=1, inplace=True)

    df = pd.merge(left=df,
                  right=df_env,
                  how='left',
                  on='Идентификатор среды',
                  indicator=True,
                  suffixes=('', '_y')).drop(['_merge'], axis=1).reset_index(drop=True).fillna('')
    df.drop(df.filter(regex='_y$').columns, axis=1, inplace=True)
    df = df[(df['Необходимость проектирования'] == 'ЗАМ.') | (df['Необходимость проектирования'] == 'НОВ.')]
    df.replace('', '-', inplace=True)

    conditions = [
        df['Тип прибора'] == 'Манометр',
        df['Тип прибора'] == 'Датчик избыточного давления',
        df['Тип прибора'] == 'Датчик перепада давления',
    ]
    coices = [0, 1, 2]
    df['sorted'] = np.select(conditions, coices, default='-')

    # Сортировка позиций для опросных листов

    df = df.sort_values(['sorted', 'Компрессор', 'Позиция'], ascending=[True, True, True]) \
        .reset_index(drop=True)

    df.reset_index(drop=False, inplace=True)

    shift_first_list = (df.shape[0] - 50) // 54
    if (df.shape[0] - 50) % 54 != 0:
        shift_first_list += 1

    df['index'] = df['index'] + 1
    df['Номер листа'] = df['index'] + 5 + shift_first_list
    df['Изменения'] = ''
    df_table_list_positions = df[['Изменения', 'index', 'Позиция', 'Номер схемы', 'Тип прибора', 'Номер листа']].copy()
    # df_ol_table = df[SETTINGS['template_pressure'].keys()].copy()
    templates_key = SETTINGS['template_pressure'].keys()
    col_name = df.columns.values
    if check_column_name(col_name, templates_key):
        return
    else:
        df_ol_table = df[list(SETTINGS['template_pressure'].keys())].copy()
        return (df_table_list_positions, df_ol_table)


def getFlowForOL():
    pp = connectiondef('Перечень приборов')
    env = connectiondef('Среда')
    pressure = connectiondef('Расход')

    df_pp = pd.DataFrame(pp[1:], columns=pp[0]).fillna('')
    df_pp = df_pp[df_pp['Параметр'] == 'Расход']
    df_env = pd.DataFrame(env[1:], columns=env[0]).fillna('')
    df_pressure = pd.DataFrame(pressure[1:], columns=pressure[0]).fillna('')

    df = pd.merge(left=df_pp,
                  right=df_pressure,
                  how='left',
                  on='Позиция',
                  indicator=True,
                  suffixes=('', '_y')).drop(['_merge'], axis=1).reset_index(drop=True).fillna('')
    df['Примечание'] = df['Примечание'].astype('str') + ' ' + df['Примечание_y'].astype('str')
    df.replace('  ', '-', inplace=True)
    df.drop(df.filter(regex='_y$').columns, axis=1, inplace=True)

    df = pd.merge(left=df,
                  right=df_env,
                  how='left',
                  on='Идентификатор среды',
                  indicator=True,
                  suffixes=('', '_y')).drop(['_merge'], axis=1).reset_index(drop=True).fillna('')
    df.drop(df.filter(regex='_y$').columns, axis=1, inplace=True)
    df = df[(df['Необходимость проектирования'] == 'ЗАМ.') | (df['Необходимость проектирования'] == 'НОВ.')]
    df.replace('', '-', inplace=True)

    # Сортировка позиций для опросных листов

    df = df.sort_values(['Компрессор', 'Позиция'], ascending=[True, True]) \
        .reset_index(drop=True)

    df.reset_index(drop=False, inplace=True)

    shift_first_list = (df.shape[0] - 31) // 33
    if (df.shape[0] - 31) % 33 != 0:
        shift_first_list += 1

    df['index'] = df['index'] + 1
    df['Номер листа'] = df['index'] + 5 + shift_first_list
    df['Изменения'] = ''
    df_table_list_positions = df[
        ['Изменения', 'index', 'Позиция', 'Номер схемы', 'Метод измерения', 'Номер листа']].copy()
    # df_ol_table = df[SETTINGS['template_flow'].keys()].copy()

    # return (df_table_list_positions, df_ol_table)
    templates_key = SETTINGS['template_flow'].keys()
    col_name = df.columns.values
    if check_column_name(col_name, templates_key):
        return
    else:
        df_ol_table = df[list(SETTINGS['template_flow'].keys())].copy()
        return (df_table_list_positions, df_ol_table)


def getLevelForOL():
    pp = connectiondef('Перечень приборов')
    env = connectiondef('Среда')
    pressure = connectiondef('Уровень')

    df_pp = pd.DataFrame(pp[1:], columns=pp[0]).fillna('')
    df_pp = df_pp[df_pp['Параметр'] == 'Уровень']
    df_env = pd.DataFrame(env[1:], columns=env[0]).fillna('')
    df_pressure = pd.DataFrame(pressure[1:], columns=pressure[0]).fillna('')

    df = pd.merge(left=df_pp,
                  right=df_pressure,
                  how='left',
                  on='Позиция',
                  indicator=True,
                  suffixes=('', '_y')).drop(['_merge'], axis=1).reset_index(drop=True).fillna('')
    df['Примечание'] = df['Примечание'].astype('str') + ' ' + df['Примечание_y'].astype('str')
    df.replace('  ', '-', inplace=True)
    df.drop(df.filter(regex='_y$').columns, axis=1, inplace=True)
    df_env_old_collumns = df_env.columns
    df_env.columns = [df_env.columns[0]] + (list(map(lambda x: str(x) + ' верхней среды', df_env.columns[1:])))

    df = pd.merge(left=df,
                  right=df_env,
                  how='left',
                  left_on='Идентификатор верхней среды',
                  right_on='Идентификатор среды',
                  indicator=True,
                  suffixes=('', '_y')).drop(['_merge'], axis=1).reset_index(drop=True).fillna('')
    df.drop(df.filter(regex='_y$').columns, axis=1, inplace=True)

    df_env.columns = df_env_old_collumns
    df_env.columns = [df_env.columns[0]] + (list(map(lambda x: str(x) + ' нижней среды', df_env.columns[1:])))

    df = pd.merge(left=df,
                  right=df_env,
                  how='left',
                  left_on='Идентификатор нижней среды',
                  right_on='Идентификатор среды',
                  indicator=True,
                  suffixes=('', '_y')).drop(['_merge'], axis=1).reset_index(drop=True).fillna('')
    df.drop(df.filter(regex='_y$').columns, axis=1, inplace=True)
    df['Другие особые условия'] = df['Другие особые условия верхней среды'] + df['Другие особые условия нижней среды']
    df = df[(df['Необходимость проектирования'] == 'ЗАМ.') | (df['Необходимость проектирования'] == 'НОВ.')]
    df.replace('', '-', inplace=True)

    # Сортировка позиций для опросных листов

    df = df.sort_values(['Компрессор', 'Позиция'], ascending=[True, True]) \
        .reset_index(drop=True)

    df.reset_index(drop=False, inplace=True)

    shift_first_list = (df.shape[0] - 31) // 33
    if (df.shape[0] - 31) % 33 != 0:
        shift_first_list += 1

    df['index'] = df['index'] + 1
    df['Номер листа'] = df['index'] + 5 + shift_first_list
    df['Изменения'] = ''
    df_table_list_positions = df[
        ['Изменения', 'index', 'Позиция', 'Номер схемы', 'Тип прибора', 'Номер листа']].copy()
    # df_ol_table = df[SETTINGS['template_level'].keys()].copy()

    # return (df_table_list_positions, df_ol_table)
    templates_key = SETTINGS['template_level'].keys()
    col_name = df.columns.values
    if check_column_name(col_name, templates_key):
        return
    else:
        df_ol_table = df[list(SETTINGS['template_level'].keys())].copy()
        return (df_table_list_positions, df_ol_table)


""""
"Позиция" - ИО
"Номер схемы" - ПП
"Назначение сигнала" - ИО
"Тип сигнала" - ИО
"Взрывозащита" - ИО
"Напряжение питания" - ПП
"Единицы измерения" - из Температура, Давление, Расход, Уровень, Анализатор, Регулирующий клапан
"Сигнализация L" - ИО
"Блокировка LL" - ИО
"Блокировка HH" - ИО
"Перечень управляющих воздействий" - ИО
"Тип канала" - ИО
"Система" - ПП
"Уровень безопасности SIL" - из Температура, Давление, Расход, Уровень, Анализатор, Отсечной клапан
"Примечание" - ИО
"""


def func1(item1, item2):
    item1 = copy.copy(item1)
    item2 = copy.copy(item2)
    out = []
    for i, j  in zip(item1, item2):
        if i == '-' or i == '' or j == '-' or j == '':
            out.append('-')
            continue
        a = i
        b = j
        do_slesha = b[:b.find('/')]
        posle_slesha = b[b.find('/')+1:]
        str = a + ':' + do_slesha + '\n' + a + ':' + posle_slesha
        out.append(str)
    s = pd.Series(out)
    return s


def func2(item):
    s = copy.copy(item)
    first_number = []
    second_number = []
    for item in s:
        first_n = int(item[:item.find('A')])
        second_n = int(item[item.find('A')+1:])
        first_number.append(first_n)
        second_number.append(second_n)
    first_number = pd.Series(first_number)
    second_number = pd.Series(second_number)


    return first_number, second_number

# def create_element_clemma(df):
#     df = df
#     for index, row in df.iterrows():
#         index1 = index
#         row1 = row
#         print('')
#     print('')

def get_io():
    arrya_io = connectiondef('ИО')
    df_io = pd.DataFrame(arrya_io[1:], columns=arrya_io[0])[
        ["Позиция",
         "Тег сигнала",
         "Назначение сигнала",
         "Тип сигнала",
         "Взрывозащита",
         "Сигнализация L",
         "Сигнализация H",
         "Блокировка LL",
         "Блокировка HH",
         "Перечень управляющих воздействий",
         "Тип канала",
         "Примечание",
         "Шкаф",
         "Модуль",
         "Канал",
         'Элемент',
         'Клемма',
         "Тип сх.подкл."]].fillna('')

    df_io["Элемент:клемма"] = func1(df_io["Элемент"], df_io["Клемма"])
    # df_io["Элемент:клемма"] = create_element_clemma(df_io[["Элемент", "Клемма"]])
    df_io["Модуль_число1"],  df_io["Модуль_число2"] = func2(df_io["Модуль"])


    arrya_pp = connectiondef('Перечень приборов')
    df_pp = pd.DataFrame(arrya_pp[1:], columns=arrya_pp[0])[["Позиция",
                                                             "Номер схемы",
                                                             "Напряжение питания",
                                                             "Система"]].fillna('')

    arrya_t = connectiondef('Температура')
    df_t = pd.DataFrame(arrya_t[1:], columns=arrya_t[0])[["Позиция",
                                                          "Единицы измерения температуры",
                                                          "Уровень безопасности SIL",
                                                          "Шкала прибора"]].fillna('')
    df_t.columns = ['Позиция', 'Единицы измерения', 'Уровень безопасности SIL', 'Шкала']

    arrya_p = connectiondef('Давление')
    df_p = pd.DataFrame(arrya_p[1:], columns=arrya_p[0])[["Позиция",
                                                          "Единицы измерения давления",
                                                          "Уровень безопасности SIL",
                                                          "Шкала прибора"]].fillna('')
    df_p.columns = ['Позиция', 'Единицы измерения', 'Уровень безопасности SIL', 'Шкала']

    arrya_f = connectiondef('Расход')
    df_f = pd.DataFrame(arrya_f[1:], columns=arrya_f[0])[["Позиция",
                                                          "Единицы измерения расхода",
                                                          "Уровень безопасности SIL",
                                                          "Шкала прибора",
                                                          "Единицы измерения шкалы прибора"]].fillna('')
    df_f['Шкала'] = df_f["Шкала прибора"].astype(str) + ' ' + df_f["Единицы измерения шкалы прибора"].astype(str)
    df_f.rename({'Единицы измерения расхода': 'Единицы измерения'}, axis=1, inplace=True)
    df_f = df_f[['Позиция', 'Единицы измерения', 'Уровень безопасности SIL', 'Шкала']].copy()
    # df_f.columns = ['Позиция', 'Единицы измерения', 'Уровень безопасности SIL']

    arrya_l = connectiondef('Уровень')
    df_l = pd.DataFrame(arrya_l[1:], columns=arrya_l[0])[["Позиция",
                                                          "Единицы измерения уровня",
                                                          "Уровень безопасности SIL",
                                                          "Шкала прибора"]].fillna('')
    df_l.columns = ['Позиция', 'Единицы измерения', 'Уровень безопасности SIL', "Шкала"]

    arrya_a = connectiondef('Анализатор')
    df_a = pd.DataFrame(arrya_a[1:], columns=arrya_a[0])[["Позиция",
                                                          "Единицы измерения загазованности",
                                                          "Уровень безопасности SIL"]].fillna('')
    df_a.columns = ['Позиция', 'Единицы измерения', 'Уровень безопасности SIL']

    arrya_cv = connectiondef('Регулирующий клапан')
    df_cv = pd.DataFrame(arrya_cv[1:], columns=arrya_cv[0])[["Позиция",
                                                             "Единицы измерения диапазона регулирования"]].fillna('')
    df_cv.columns = ['Позиция', 'Единицы измерения']

    arrya_sov = connectiondef('Задвижка')
    df_sov = pd.DataFrame(arrya_sov[1:], columns=arrya_sov[0])[["Позиция",
                                                                "Уровень безопасности SIL"]].fillna('')
    df_sov.columns = ['Позиция', 'Единицы измерения']

    del (arrya_io, arrya_pp, arrya_t, arrya_p, arrya_f, arrya_l, arrya_a, arrya_cv, arrya_sov)

    all_device_df = pd.concat([df_t, df_p, df_f, df_l, df_a, df_cv, df_sov]).fillna('')

    all_device_df = all_device_df[all_device_df["Позиция"] != '']
    all_device_df.reset_index(drop=True, inplace=True)
    all_device_df.drop_duplicates(subset=["Позиция"], inplace=True)

    del (df_t, df_p, df_f, df_l, df_a, df_cv, df_sov)

    df_io = df_io.merge(
        df_pp,
        how='left',
        on='Позиция'
    ).merge(
        all_device_df,
        how='left',
        on='Позиция'
    ).fillna('')

    del all_device_df

    df_io["Канал"] = pd.to_numeric(
        df_io["Канал"],
        downcast='integer',
        errors='coerce'
    ).replace(np.NAN, 0)

    df_io.sort_values(by=['Шкаф', 'Модуль_число1', 'Модуль_число2', 'Канал'], ascending=[True, True, True, True], inplace=True)

    df_io = df_io[['Позиция',
                   'Назначение сигнала',
                   'Тип сигнала',
                   'Взрывозащита',
                   'Единицы измерения',
                   'Шкала',
                   'Блокировка LL',
                   'Сигнализация L',
                   'Сигнализация H',
                   'Блокировка HH',
                   'Тип канала',
                   'Шкаф',
                   'Модуль',
                   'Канал',
                   'Элемент:клемма',
                   'Тип сх.подкл.',
                   'Тег сигнала',
                   'Перечень управляющих воздействий',
                   'Примечание']].copy()

    # print('')


    # TODO: настроить правильную сортировку строк в ИО
    # TODO: добавить вставку строки на всю длину таблицы с обозначением шкафа
    return df_io


"""
Позиция
Наименование и тех характеристики
    Температура
        'Датчик температуры'
        'Тип сенсора: ' + 'Тип сенсора' + 'Градуировка НСХ' - Температура
        'Выходной сигнал: '
        'Степень защиты: '
        'Взрывозащита: '
        'Шкала: '
    Давление
        'Измеряемый параметр'
        'Выходной сигнал: '
        'Степень защиты: '
        'Взрывозащита: '
        'Шкала: '
        'Комплект'
    Расход
        'Метод измерения (тип датчика)'
        'Выходной сигнал: '
        'Степень защиты: '
        'Взрывозащита: '
        'Шкала: '
    Уровень
        'Тип прибора'
        'Выходной сигнал: '
        'Степень защиты: '
        'Взрывозащита: '
        'Шкала: '
    Анализатор
        'Параметр'
        'Выходной сигнал: '
        'Напряжение питания: '
        'Степень защиты: '
        'Взрывозащита: '
        'Диапазон измерения: '
        'Тип сенсора: '
    Регулирующий клапан
        
    Отсечной клапан
Номер опросного листа (Название документа из SETTINGS для данного типа)
Код продукции
Поставщик
Ед. измерения
Кол
Масса
Примечание - Перечень приборов
"""


def get_spec():
    arrya_pp = connectiondef('Перечень приборов')

    # Столбцы из Перечня приборов

    df_pp = pd.DataFrame(arrya_pp[1:], columns=arrya_pp[0])[[
        "Позиция",
        "Примечание",
        "Назначение"
    ]].fillna('')
    del arrya_pp
    df_pp.drop_duplicates(subset=["Позиция"])
    df_pp['Количество'] = '1'

    # Столбцы из ИО

    arrya_io = connectiondef('ИО')
    df_io = pd.DataFrame(arrya_io[1:], columns=arrya_io[0])[[
        "Позиция",
        "Тег сигнала",
        "Тип сигнала",
        "Взрывозащита",
        "Сигнал/питание"
    ]].fillna('')
    del arrya_io

    # Получили ИО_сигналы
    df_io_sig = df_io[df_io["Сигнал/питание"] == "Сигнал"][["Позиция", "Тип сигнала", "Взрывозащита"]]
    # df_io_sig.drop_duplicates(subset=["Позиция"], inplace=True)
    df_io_sig.groupby(by='Позиция').agg({"Тип сигнала": joinUniqu})

    # TODO: исправить получение информации о питании прибора
    # Получили ИО_питание
    df_io_power = df_io[df_io["Сигнал/питание"] == "Питание"][["Позиция", "Тип сигнала"]]
    df_io_power.columns = ["Позиция", "Питание"]
    df_io_power.drop_duplicates(subset=["Позиция"], inplace=True)
    # df_io_power.groupby(by='Позиция').agg({'Питание': joinUniqu})

    df_pp = df_pp.merge(
        df_io_sig,
        how="left",
        on="Позиция"
    ).merge(
        df_io_power,
        how="left",
        on="Позиция"
    ).fillna('')
    df_pp.rename({'Назначение': 'Наименование'}, inplace=True)

    del df_io, df_io_sig, df_io_power

    list_devices = ['Температура', 'Давление', 'Расход', 'Уровень']
    # list_devices = ['Температура', 'Давление', 'Расход', 'Уровень', 'Анализатор', 'Регулирующий клапан', 'Отсечной клапан']

    spec_dfs = []

    # Какие столбцы нужно вытащить из каждой вкладки приборов

    columns_for_device = {
        "Температура": [
            "Позиция",
            "Тип сенсора",
            "Градуировка НСХ",
            "Степень защиты",
            "Шкала прибора",
            "Единицы измерения температуры"
        ],
        "Давление": [
            "Позиция",
            "Измеряемый параметр",
            "Степень защиты",
            "Шкала прибора",
            "Единицы измерения давления",
            "Комплект монтажных частей"
        ],
        "Расход": [
            "Позиция",
            "Метод измерения",
            "Степень защиты",
            "Шкала прибора",
            "Единицы измерения расхода"
        ],
        "Уровень": [
            "Позиция",
            "Тип прибора",
            "Степень защиты",
            "Шкала прибора",
            "Единицы измерения уровня"
        ],
        # "Анализатор": [],
        # "Регулирующий клапан": [],
        # "Отсечной клапан": []
    }

    for device in list_devices:

        # Создать соответствующий df
        arrya = connectiondef(device)
        df = pd.DataFrame(arrya[1:], columns=arrya[0]).fillna('')
        del arrya

        df = df[columns_for_device[device]]
        df = df.merge(
            df_pp,
            how='left',
            on='Позиция'
        ).fillna('')

        if device == list_devices[0]:
            # Температура
            df['Техническая характеристика'] = 'Датчик температуры' + '\n' + \
                                               'Тип сенсора: ' + df['Тип сенсора'].astype(str) + ' ' + \
                                               df['Градуировка НСХ'].astype(str) + '\n' + \
                                               'Выходной сигнал: ' + df['Тип сигнала'].astype(str) + '\n' + \
                                               'Степень защиты: ' + df['Степень защиты'].astype(str) + '\n' + \
                                               'Взрывозащита: ' + df['Взрывозащита'].astype(str) + '\n' + \
                                               'Шкала: ' + df['Шкала прибора'].astype(str) + \
                                               df['Единицы измерения температуры'].astype(str) + '\n'

            df['Опросный лист'] = str(SETTINGS["file_name_temperature_ol"])
            df['sort_device_number'] = 0

        elif device == list_devices[1]:
            # Давление

            df['Техническая характеристика'] = df['Измеряемый параметр'].astype(str) + '\n' + \
                                               'Выходной сигнал: ' + df['Тип сигнала'].astype(str) + '\n' + \
                                               'Степень защиты: ' + df['Степень защиты'].astype(str) + '\n' + \
                                               'Взрывозащита: ' + df['Взрывозащита'].astype(str) + '\n' + \
                                               'Шкала: ' + df['Шкала прибора'].astype(str) + \
                                               df['Единицы измерения давления'].astype(str) + '\n' + \
                                               df['Комплект монтажных частей'].astype(str) + '\n'
            df['Опросный лист'] = str(SETTINGS["file_name_pressure_ol"])
            df['sort_device_number'] = 1

        elif device == list_devices[2]:
            # Расход

            df['Техническая характеристика'] = df['Метод измерения'].astype(str) + '\n' + \
                                               'Выходной сигнал: ' + df['Тип сигнала'].astype(str) + '\n' + \
                                               'Степень защиты: ' + df['Степень защиты'].astype(str) + '\n' + \
                                               'Взрывозащита: ' + df['Взрывозащита'].astype(str) + '\n' + \
                                               'Шкала: ' + df['Шкала прибора'].astype(str) + '\n'

            df['Опросный лист'] = str(SETTINGS["file_name_flow_ol"])
            df['sort_device_number'] = 2

        elif device == list_devices[3]:
            # Уровень

            df['Техническая характеристика'] = df['Тип прибора'].astype(str) + ' датчик уровня' + '\n' + \
                                               'Выходной сигнал: ' + df['Тип сигнала'].astype(str) + '\n' + \
                                               'Степень защиты: ' + df['Степень защиты'].astype(str) + '\n' + \
                                               'Взрывозащита: ' + df['Взрывозащита'].astype(str) + '\n' + \
                                               'Шкала: ' + df['Шкала прибора'].astype(str) + \
                                               df['Единицы измерения уровня'].astype(str) + '\n'

            df['Опросный лист'] = str(SETTINGS["file_name_level_ol"])
            df['sort_device_number'] = 3

        col = columns_for_device[device][:]
        col.remove('Позиция')
        df.drop(col, axis=1, inplace=True)
        spec_dfs.append(df)

    # print('')

    df = pd.concat(spec_dfs, ignore_index=True).reset_index(drop=True)
    df.drop(['Тип сигнала', 'Взрывозащита', 'Питание'], axis=1, inplace=True)
    df.reset_index(inplace=True)
    df_naz = df[['index', 'Назначение']].copy()
    df_naz.columns = ['index', 'Техническая характеристика']
    df_naz['sort_row'] = 0
    df.drop('Назначение', axis=1, inplace=True)
    df['sort_row'] = 1
    df = pd.concat([df, df_naz]).sort_values(by=['index', 'sort_row'], ascending=[True, True]).fillna('')
    del df_naz
    df[['Код продукции', 'Поставщик', 'Ед.измерения', 'Масса']] = ('', '', '', '')

    df = df[[
        'Позиция',
        'Техническая характеристика',
        'Опросный лист',
        'Код продукции',
        'Поставщик',
        'Ед.измерения',
        'Количество',
        'Масса',
        'Примечание'
    ]].copy().reset_index(drop=True)

    return df


def get_tsp():
    # Столбцы из Перечня приборов

    arrya_pp = connectiondef('Перечень приборов')
    df_pp = pd.DataFrame(arrya_pp[1:], columns=arrya_pp[0])[[
        "Позиция",
        "Назначение"
    ]].fillna('')
    df_pp = df_pp[df_pp['Позиция'] != '']
    df_pp.drop_duplicates(subset=['Позиция'], inplace=True)

    del arrya_pp

    # Столбцы из ТСП

    arrya_tsp = connectiondef('ТСП')
    df_tsp = pd.DataFrame(arrya_tsp[1:], columns=arrya_tsp[0])[[
        'Позиция',
        'Тег сигнала',
        'Клемма прибора',
        'Жила местного кабеля',
        'Кабель местный',
        'Соединительная коробка',
        'Кабельный ввод коробки',
        'Клемма коробки',
        'Жила кабеля магистрального',
        'Кабель магистральный',
        'Шкаф',
        'Клеммник шкафа',
        'Клемма',
        'Примечание'
    ]].fillna('')
    df_tsp = df_tsp[df_tsp['Позиция'] != '']
    # del arrya_tsp

    # Столбцы из ИО

    arrya_io = connectiondef('ИО')
    df_io = pd.DataFrame(arrya_io[1:], columns=arrya_io[0])[[
        "Позиция",
        "Тег сигнала",
        "Тип сигнала",
        "Взрывозащита"
    ]].fillna('')
    df_io = df_io[df_io['Тег сигнала'] != '']
    # df_io.drop_duplicates(subset=['Тег сигнала'], inplace=True)
    df_io = df_io.groupby(by=['Тег сигнала']).agg({
        # "Тег сигнала": joinUniqu,
        "Тип сигнала": joinUniqu,
        "Взрывозащита": joinUniqu
    }).reset_index()

    # del arrya_io

    df_tsp = df_pp.merge(
        df_tsp,
        how="left",
        on="Позиция"
    ).merge(
        df_io,
        how="left",
        on="Тег сигнала"
    ).fillna('')

    df_tsp['Клеммник:клемма шкафа'] = np.where((
            (df_tsp['Клеммник шкафа'] != '') & (df_tsp['Клемма'] != '')),
        df_tsp['Клеммник шкафа'].astype(str) + ':' + df_tsp['Клемма'].astype(str), '')
    df_tsp = df_tsp[[
        'Позиция',
        'Назначение',
        'Тип сигнала',
        'Взрывозащита',
        'Клемма прибора',
        'Жила местного кабеля',
        'Кабель местный',
        'Соединительная коробка',
        'Клемма коробки',
        'Жила кабеля магистрального',
        'Кабель магистральный',
        'Шкаф',
        'Примечание',
        'Клеммник:клемма шкафа'
    ]].copy()

    # df_tsp['Клеммник клемма шкафа'] = df_tsp['Клеммник шкафа'].astype(str) + ':' + df_tsp['Клемма'].astype(str)

    # del df_io

    # TODO: отсортировать ТСП в нужном порядке

    df_tsp.sort_values(
        by=['Шкаф', 'Соединительная коробка', 'Клемма коробки'],
        ascending=[True, True, True],
        inplace=True
    )

    return df_tsp


def get_kj():
    arrya_kj = connectiondef('КЖ')
    df_kj = pd.DataFrame(arrya_kj[1:], columns=arrya_kj[0])[[
        "Номер кабеля",
        # "Тип кабеля",
        "Марка кабеля",
        # "Диаметр кабеля",
        "Длина кабеля",
        "Труба",
        "Длина трубы",
        "Металлорукав",
        "Длина металлорукава",
        # "Список кабельных лотков",
        "Примечание"
    ]].fillna('')
    # del arrya_kj
    df_kj = df_kj[df_kj['Номер кабеля'] != '']
    df_kj.drop_duplicates(subset=['Номер кабеля'], inplace=True)

    arrya_tsp = connectiondef('ТСП')
    df_tsp = pd.DataFrame(arrya_tsp[1:], columns=arrya_tsp[0])[[
        'Позиция',
        'Кабель местный',
        'Соединительная коробка',
        'Кабель магистральный',
        'Шкаф'
    ]].fillna('')
    # del arrya_tsp

    df_tsp = df_tsp[df_tsp['Позиция'] != '']
    df_tsp.replace('-', '', inplace=True)
    df_tsp.drop_duplicates(subset=[
        'Позиция',
        'Кабель местный',
        'Соединительная коробка',
        'Кабель магистральный',
        'Шкаф'
    ], inplace=True)

    arrya_io = connectiondef('ИО')
    df_io = pd.DataFrame(arrya_io[1:], columns=arrya_io[0])[[
        "Позиция",
        "Тег сигнала",
        "Тип сигнала",
        "Взрывозащита"
    ]].fillna('')
    df_io = df_io[df_io['Тег сигнала'] != '']

    # Таблица соединений для местных кабелей [Позиция-кабель-коробка]
    df_mes_cab = df_tsp[
        # (df_tsp['Позиция'] != '') &
        (df_tsp['Кабель местный'] != '') &
        (df_tsp['Соединительная коробка'] != '')
        ][[
        'Позиция',
        'Кабель местный',
        'Соединительная коробка'
    ]].copy()
    df_mes_cab['Коробка'] = df_mes_cab['Соединительная коробка']

    df_mag_cab = df_tsp[
        (df_tsp['Соединительная коробка'] != '') &
        (df_tsp['Кабель магистральный'] != '') &
        (df_tsp['Шкаф'] != '')
        ][[
        'Соединительная коробка',
        'Кабель магистральный',
        'Шкаф'
    ]].copy()
    df_mag_cab['Коробка'] = df_mag_cab['Соединительная коробка']

    df_prm_cab_mes = df_tsp[
        # (df_tsp['Позиция'] != '') &
        (df_tsp['Кабель местный'] != '') &
        (df_tsp['Соединительная коробка'] == '') &
        (df_tsp['Шкаф'] != '')
        ][[
        'Позиция',
        'Кабель местный',
        'Шкаф',
        'Соединительная коробка'
    ]].copy()
    df_prm_cab_mes['Коробка'] = df_prm_cab_mes['Соединительная коробка']
    df_prm_cab_mes.drop('Соединительная коробка', axis=1, inplace=True)

    df_prm_cab_mag = df_tsp[
        # (df_tsp['Позиция'] != '') &
        (df_tsp['Кабель магистральный'] != '') &
        (df_tsp['Соединительная коробка'] == '') &
        (df_tsp['Шкаф'] != '')
        ][[
        'Позиция',
        'Кабель магистральный',
        'Шкаф',
        'Соединительная коробка'
    ]].copy()
    df_prm_cab_mag['Коробка'] = df_prm_cab_mag['Соединительная коробка']
    df_prm_cab_mag.drop('Соединительная коробка', axis=1, inplace=True)

    for df in [df_mes_cab, df_mag_cab, df_prm_cab_mes, df_prm_cab_mag]:
        df.columns = ['Откуда', 'Номер кабеля', 'Куда', 'Коробка']

    df_mes_cab['Порядок выгрузки'] = 0
    df_mag_cab['Порядок выгрузки'] = 1
    df_prm_cab_mes['Порядок выгрузки'] = 2
    df_prm_cab_mag['Порядок выгрузки'] = 3

    df = pd.concat([
        df_mes_cab,
        df_mag_cab,
        df_prm_cab_mes,
        df_prm_cab_mag
    ]).reset_index(drop=True)
    df.drop_duplicates(subset=['Номер кабеля'], inplace=True)
    # print('')

    # TODO: формирования второй таблицы для кж

    arrya_cab_desc = connectiondef('Кабель')
    df_cab_desc = pd.DataFrame(arrya_cab_desc[1:], columns=arrya_cab_desc[0])[[
        "Наименование",
        "Описание",
        "Марка",
        "Тип",
        "Количество групп",
        "Количество жил в группе",
        "Сечение жилы",
        "Наружный диаметр,мм ",
        "Окончание",
        "Примечание"
    ]].fillna('')
    del arrya_cab_desc
    df_cab_desc = df_cab_desc[df_cab_desc['Наименование'] != '']
    df_cab_desc.drop_duplicates(subset=['Наименование'], inplace=True)

    arrya_trub_desc = connectiondef('Труба')
    df_trub_desc = pd.DataFrame(arrya_trub_desc[1:], columns=arrya_trub_desc[0])[[
        "Марка",
        "Описание",
        "Диаметр",
        "Примечание"
    ]].fillna('')
    del arrya_trub_desc
    df_trub_desc = df_trub_desc[(df_trub_desc['Марка'] != '') & (df_trub_desc['Марка'] != '-')]
    df_trub_desc.drop_duplicates(subset=['Марка'], inplace=True)

    arrya_metal_desc = connectiondef('Металлорукав')
    df_metal_desc = pd.DataFrame(arrya_metal_desc[1:], columns=arrya_metal_desc[0])[[
        "Марка",
        "Описание",
        "Примечание"
    ]].fillna('')
    del arrya_metal_desc
    df_metal_desc = df_metal_desc[(df_metal_desc['Марка'] != '') & (df_metal_desc['Марка'] != '-')]
    df_metal_desc.drop_duplicates(subset=['Марка'], inplace=True)

    del df_mes_cab, df_mag_cab, df_prm_cab_mes, df_prm_cab_mag

    df = df.merge(
        df_kj,
        how="left",
        on='Номер кабеля'
    ).fillna('')

    df["Длина кабеля"] = pd.to_numeric(
        df["Длина кабеля"],
        downcast='integer',
        errors='coerce'
    )

    df["Длина трубы"] = pd.to_numeric(
        df["Длина трубы"],
        downcast='integer',
        errors='coerce'
    )

    df["Длина металлорукава"] = pd.to_numeric(
        df["Длина металлорукава"],
        downcast='integer',
        errors='coerce'
    )

    df[["Длина кабеля", "Длина трубы", "Длина металлорукава"]] = df[
        ["Длина кабеля", "Длина трубы", "Длина металлорукава"]].replace(np.NAN, 0)
    df[["Длина кабеля", "Длина трубы", "Длина металлорукава"]] = df[
        ["Длина кабеля", "Длина трубы", "Длина металлорукава"]].round(0).astype(int)

    df_out_list = df.copy()

    df_out_list['Порядок выгрузки прямыл кабелей'] = np.where((
            df_out_list['Коробка'] != ''), False, True)
    df_out_list = df_out_list.sort_values(
        by=['Порядок выгрузки прямыл кабелей', 'Коробка', 'Порядок выгрузки', 'Номер кабеля'],
        ascending=[True, True, True, True]).fillna('')
    df_out_list = df_out_list[[
        'Номер кабеля',
        'Откуда',
        'Куда',
        'Марка кабеля',
        'Длина кабеля',
        'Труба',
        'Длина трубы',
        'Металлорукав',
        'Длина металлорукава',
        'Примечание'
        ]].astype(str)
    # df_out_list = df_out_list.loc[:, :'Примечание']
    # print('')

    df_cab_length = df[df["Марка кабеля"] != ''][["Марка кабеля", "Длина кабеля"]].copy()
    df_trub_length = df[(df["Труба"] != '') & (df["Труба"] != '-')][["Труба", "Длина трубы"]].copy()
    df_metal_length = df[(df["Металлорукав"] != '') & (df["Металлорукав"] != '-')][
        ["Металлорукав", "Длина металлорукава"]].copy()

    df_cab_length.columns = ["Позиция", "Длина"]
    df_trub_length.columns = ["Позиция", "Длина"]
    df_metal_length.columns = ["Позиция", "Длина"]

    df_cab_length = df_cab_length.groupby(by=['Позиция']).agg({"Длина": 'sum'}).reset_index()
    df_trub_length = df_trub_length.groupby(by=['Позиция']).agg({"Длина": 'sum'}).reset_index()
    df_metal_length = df_metal_length.groupby(by=['Позиция']).agg({"Длина": 'sum'}).reset_index()

    # print(df_cab_length.columns.values)

    # df_cab_length.columns = df_cab_length.columns.droplevel(1)

    df_cab_length['Порядок выгрузки типа'] = 0
    df_trub_length['Порядок выгрузки типа'] = 1
    df_metal_length['Порядок выгрузки типа'] = 2

    # TODO: сгруппировать марки кабелей по описанию

    # К каждой таблице с длиной присоединить описание

    df_cab_length = df_cab_length.merge(
        df_cab_desc,
        how="left",
        left_on="Позиция",
        right_on="Наименование"
    ).fillna('')

    # Упорядочить по условию из описания и сопутствующих столбцов
    # df_cab_length.sort_values(by=[], ascending=[], inplace=True)

    # Сбросить индексы
    df_cab_length.reset_index(drop=True, inplace=True)
    # Сохранить индексы, для сортировки внутри одного типа
    df_cab_length['Сортировка внутри типа'] = df_cab_length.index

    # Избавиться от лишних столбцов
    # df_cab_length = df_cab_length[[
    #     'Позиция',
    #     'Длина',
    #     'Описание',
    #     'Примечание',
    #     'Порядок выгрузки типа',
    #     'Сортировка внутри типа'
    # ]]

    df_trub_length = df_trub_length.merge(
        df_trub_desc,
        how="left",
        left_on="Позиция",
        right_on="Марка"
    ).fillna('')
    # df_trub_length.sort_values(by=[], ascending=[], inplace=True)
    df_trub_length.reset_index(drop=True, inplace=True)
    df_trub_length['Сортировка внутри типа'] = df_trub_length.index

    df_metal_length = df_metal_length.merge(
        df_metal_desc,
        how="left",
        left_on="Позиция",
        right_on="Марка"
    ).fillna('')
    # df_trub_length.sort_values(by=[], ascending=[], inplace=True)
    df_metal_length.reset_index(drop=True, inplace=True)
    df_metal_length['Сортировка внутри типа'] = df_metal_length.index

    df_out = pd.concat([df_cab_length, df_trub_length, df_metal_length]).reset_index(drop=True)
    df_out = df_out[[
        'Позиция',
        'Длина',
        'Описание',
        'Примечание',
        'Порядок выгрузки типа',
        'Сортировка внутри типа'
    ]]

    # df_out['Сортировка глобальная'] = df_out.index
    df_out['Сортировка описания/позиция'] = 1

    df_cab_desc = df_out.copy()
    df_cab_desc['Позиция'] = df_cab_desc['Описание']
    df_cab_desc['Сортировка описания/позиция'] = 0

    df_out = pd.concat([df_out, df_cab_desc]).reset_index(drop=True)
    df_out.sort_values(by=[
        # 'Сортировка глобальная',
        'Порядок выгрузки типа',
        'Сортировка внутри типа',
        'Сортировка описания/позиция'
    ],
        ascending=[True, True, True],
        inplace=True)
    df_out.drop_duplicates(subset=['Позиция'], inplace=True)
    df_out['Пустой столбец'] = ''
    df_out = df_out[[
        'Пустой столбец',
        'Позиция',
        'Длина',
        'Примечание'
    ]]
    df_out = df_out.astype(str)
    #

    # Упорядочить по условию из описания и сопутствующих столбцов
    # Сбросить индексы, сохранить индексы, для сортировки внутри одного типа
    # Избавиться от лишних столбцов, создать столбец для сортировки описания/позиция
    # Сделать копию, заменить значения столбца Марка на описание
    # Сделать concate
    # Удалить повторяющиеся строки по столбцу Марка (Должны удалиться только повторные строки описания)
    # print('')
    return df_out_list, df_out


# a = get_tsp()
# b = get_io()
# print('')
