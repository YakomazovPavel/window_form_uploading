from connections import connectiondef
import pandas as pd
import numpy as np

templates = {
    'Температура': {
        'Позиция': (0, 4),
        'Назначение': (1, 4),
        'Место установки': (2, 4),
        'Размер трубопровода': (3, 4),
        # 'Материал трубопровода': (4, 4),
        'Среда': (4, 4),
        'Агрегатное состояние': (5, 4),
        'T min': (6, 4),
        'T max': (7, 4),
        'T раб': (8, 4),
        'Единицы измерения температуры': (8, 5),
        'P min': (9, 4),
        'P max': (10, 4),
        'P раб': (11, 4),
        'Единицы измерения давления': (11, 5),
        'Плотность': (12, 4),
        'Единицы измерения плотности': (12, 5),
        'Вязкость': (13, 4),
        'Единицы измерения вязкости': (13, 5),
        'Агрессивность': (14, 4),
        'Другие особые условия': (15, 4),
        'Тип сенсора': (16, 4),
        'Градуировка НСХ': (17, 4),
        'Диаметр ЧЭ': (18, 4),
        'Длина сенсора': (19, 4),
        'Соединение с процессом чувствительного элемента': (20, 4),
        'Температурная вставка (удлинитель)': (21, 4),
        'Шкала прибора': (22, 4),
        'Тип сигналов*': (23, 4),
        'Напряжение питания': (24, 4),
        'Схема подключения (сигнал)': (25, 4),
        'Погрешность измерения': (26, 4),
        'Взрывозащита*': (27, 4),
        'Уровень безопасности SIL': (28, 4),
        'Степень защиты': (29, 4),
        'Тип корпуса': (30, 4),
        'Материал корпуса': (31, 4),
        'Тип защитной гильзы': (32, 4),
        'Тип резьбы гильзы': (33, 4),
        'Длина погружаемой части гильзы': (34, 4),
        'Маркировка защитной гильзы': (35, 4),
        'Местный индикатор': (36, 4),
        'Кабельный ввод': (37, 4),
        'Марка кабеля': (38, 4),
        'Изготовитель': (39, 4),
        'Модель': (40, 4),
        'Примечание': (41, 4),
    },
    'Давление': {
        'Позиция': (0, 4),
        'Назначение': (1, 4),
        'Место установки': (2, 4),
        'Среда': (3, 4),
        'Агрегатное состояние': (4, 4),
        'T min': (5, 4),
        'T max': (6, 4),
        'T раб': (7, 4),
        'Единицы измерения температуры': (7, 5),
        'P min': (8, 4),
        'P max': (9, 4),
        'P раб': (10, 4),
        'P стат': (11, 4),
        'Перепад давления': (12, 4),
        'Единицы измерения давления': (12, 5),
        'Плотность': (13, 4),
        'Единицы измерения плотности': (13, 5),
        'Вязкость': (14, 4),
        'Единицы измерения вязкости': (14, 5),
        'Агрессивность': (15, 4),
        'Другие особые условия': (16, 4),
        'Измеряемый параметр': (17, 4),
        'Шкала прибора': (18, 4),
        'Тип сигналов*': (19, 4),
        'Напряжение питания': (20, 4),
        'Схема подключения (сигнал)': (21, 4),
        'Погрешность измерения': (22, 4),
        'Взрывозащита*': (23, 4),
        'Степень защиты': (24, 4),
        'Уровень безопасности SIL': (25, 4),
        'Материал корпуса': (26, 4),
        'Соединение с процессом': (27, 4),
        'Мембранный разделитель': (28, 4),
        'Подвод импульсных трубок': (29, 4),
        'Сторона высокого давления': (30, 4),
        'Тип вентильного блока': (31, 4),
        'Тип резьбы вентильного блока для подключения импульсных линий / датчика': (32, 4),
        'Тип дренажного соединения вентильного блока': (33, 4),
        'Ниппель для присоединения импульсных линий': (34, 4),
        'Местный индикатор': (35, 4),
        'Комплект монтажных частей': (36, 4),
        'Кабельный ввод': (37, 4),
        'Марка кабеля': (38, 4),
        'Изготовитель': (39, 4),
        'Модель': (40, 4),
        'Примечание': (41, 4),
    },
    'Расход': {
        'Позиция': (0, 4),
        'Назначение': (1, 4),
        'Место установки': (2, 4),
        'Размер трубопровода': (3, 4),
        'Материал трубопровода': (4, 4),
        'Среда': (5, 4),
        'Агрегатное состояние': (6, 4),
        'Q min': (7, 4),
        'Q max': (8, 4),
        'Q раб': (9, 4),
        'Единицы измерения расхода': (9, 5),
        'T min': (10, 4),
        'T max': (11, 4),
        'T раб': (12, 4),
        'Единицы измерения температуры': (12, 5),
        'P min': (13, 4),
        'P max': (14, 4),
        'P расч': (15, 4),
        'P раб': (16, 4),
        'Единицы измерения давления': (16, 5),
        'Плотность': (17, 4),
        'Единицы измерения плотности': (17, 5),
        'Вязкость': (18, 4),
        'Единицы измерения вязкости': (18, 5),
        'Агрессивность': (19, 4),
        'Другие особые условия': (20, 4),
        'Метод измерения': (21, 4),
        'Шкала прибора': (22, 4),
        'Единицы измерения шкалы приборв': (22, 5),
        'Погрешность': (23, 4),
        'Тип сигналов*': (24, 4),
        'Напряжение питания': (25, 4),
        'Схема подключения (сигнал)': (26, 4),
        'Местный индикатор': (27, 4),
        'Кабельный ввод': (28, 4),
        'Марка кабеля': (29, 4),
        'Взрывозащита*': (30, 4),
        'Степень защиты': (31, 4),
        'Уровень безопасности SIL': (32, 4),
        'Тип диафрагмы': (33, 4),
        'Номер исполнения': (34, 4),
        'Материал диафрагмы': (35, 4),
        'Способ отбора давления': (36, 4),
        'Тип фланцев': (37, 4),
        'DN фланцев': (38, 4),
        'PN фланцев, кгс/см2': (39, 4),
        'Разделительные сосуды/мембраны/вентильные блоки': (40, 4),
        'Комплект монтажных частей': (41, 4),
        'Изготовитель': (42, 4),
        'Модель': (43, 4),
        'Примечание': (44, 4)
    },
    'Уровень': {
        'Позиция': (0, 4),
        'Назначение': (1, 4),
        'Место установки': (2, 4),
        'Тип прибора': (3, 4),
        'Тип аппарата': (4, 4),
        'Диаметр (длина) /Ширина /Высота аппарата': (5, 4),
        'Выносная камера (штуцер) на аппарате': (6, 4),
        'Длина камеры (штуцера) на аппарате': (7, 4),
        'Диаметр камеры (штуцера) на аппарате': (8, 4),
        'Среда верхней среды': (9, 4),
        'Среда нижней среды': (10, 4),
        'T min': (11, 4),
        'T max': (12, 4),
        'T раб': (13, 4),
        'Единицы измерения температуры': (13, 6),
        'P min': (14, 4),
        'P max': (15, 4),
        'P раб': (16, 4),
        'Единицы измерения давления': (16, 6),
        'Плотность верхней среды': (17, 4),
        'Плотность нижней среды': (18, 4),
        'Единицы измерения плотности верхней среды': (18, 6),
        'Вязкость верхней среды': (19, 4),
        'Вязкость нижней среды': (20, 4),
        'Единицы измерения вязкости верхней среды': (20, 6),
        'Агрессивность верхней среды': (21, 4),
        'Агрессивность нижней среды': (22, 4),
        'Другие особые условия верхней среды': (23, 4),
        'L min': (24, 4),
        'L max': (25, 4),
        'Единицы измерения уровня': (25, 6),
        'Длина чувствительного элемента': (26, 4),
        'Подвод импульсных трубок': (27, 4),
        'Сторона высокого давления': (28, 4),
        'Тип фланцев / резьбы': (29, 4),
        'DN фланцев': (30, 4),
        'PN фланцев': (31, 4),
        'Выносная камера в комплекте с прибором': (32, 4),
        'Тип фланцев выносной камеры': (33, 4),
        'DN фланцев выносной камеры': (34, 4),
        'PN фланцев выносной камеры': (35, 4),
        'Измеряемый параметр': (36, 4),
        'Шкала прибора': (37, 4),
        'Тип сигналов*': (38, 4),
        'Напряжение питания': (39, 4),
        'Схема подключения (сигнал)': (40, 4),
        'Погрешность измерения': (41, 4),
        'Взрывозащита*': (42, 4),
        'Уровень безопасности SIL': (43, 4),
        'Степень защиты': (44, 4),
        'Материал корпуса': (45, 4),
        'Ответный фланец / бобышка в комплекте': (46, 4),
        'Тип вентильного блока': (47, 4),
        'Тип резьбы вентильного блока под импульсные линии/датчик': (48, 4),
        'Тип дренажного соединения вентильного блока': (49, 4),
        'Ниппель для присоединения импульсных линий': (50, 4),
        'Местный индикатор': (51, 4),
        'Комплект монтажных частей': (52, 4),
        'Кабельный ввод': (53, 4),
        'Марка кабеля': (54, 4),
        'Изготовитель': (55, 4),
        'Модель': (56, 4),
        'Примечание': (57, 4),
    },
    # 'Регулирующий клапан': {
    #     'Позиция': (0, 4),
    #     'Назначение': (1, 4),
    #     'Место установки': (2, 4),
    #     'Размер трубопровода': (3, 4),
    #     'Материал трубопровода': (4, 4),
    #     'Среда': (5, 4),
    #     'Агрегатное состояние': (6, 4),
    #     'Q min': (7, 4),
    #     'Q max': (8, 4),
    #     'Q раб': (9, 4),
    #     'Единицы измерения расхода': (9, 5),
    #     'T min': (10, 4),
    #     'T max': (11, 4),
    #     'T раб': (12, 4),
    #     'Единицы измерения температуры': (12, 5),
    #     'P min': (13, 4),
    #     'P max': (14, 4),
    #     'P раб': (15, 4),
    #     'P расч': (16, 4),
    #     'Падение давления на клапане (макс)': (17, 4),
    #     'Единицы измерения давления': (17, 5),
    #     'Рабочий диапазон регулирования': (18, 4),
    #     'Единицы измерения диапазона регулирования': (18, 5),
    #     'Плотность': (19, 4),
    #     'Единицы измерения плотности': (19, 5),
    #     'Вязкость': (20, 4),
    #     'Единицы измерения вязкости': (20, 5),
    #     'Агрессивность': (21, 4),
    #     'Другие особые условия': (22, 4),
    #     'Направление потока': (23, 4),
    #     'Тип привода': (24, 4),
    #     'Класс герметичности': (25, 4),
    #     'Пропускная характеристика': (26, 4),
    #     'Направление действия': (27, 4),
    #     'Давление питающего воздуха': (28, 4),
    #     'Положение при отсутствии воздуха/электропитания': (29, 4),
    #     'Тип позиционера': (30, 4),
    #     'Напряжение питания позиционера': (31, 4),
    #     'Выходной сигнал позиционера': (32, 4),
    #     'Взрывозащита позиционера': (33, 4),
    #     'Степень защиты позиционера': (34, 4),
    #     'Манометр позиционера': (35, 4),
    #     'Кабельный ввод позиционера': (36, 4),
    #     'Марка кабеля позиционера': (37, 4),
    #     'Соединение с процессом': (38, 4),
    #     'Тип фланцев': (39, 4),
    #     'DN фланцев': (40, 4),
    #     'PN фланцев': (41, 4),
    #     'DN существующего клапана': (42, 4),
    #     'PN существующего клапана': (43, 4),
    #     'Изготовитель': (44, 4),
    #     'Модель': (45, 4),
    #     'Примечание': (46, 4)
    # },
    # 'Задвижка': {
    #     'Позиция': (0, 4),
    #     'Назначение': (1, 4),
    #     'Место установки': (2, 4),
    #     'Размер трубопровода': (3, 4),
    #     'Материал трубопровода': (4, 4),
    #     'Среда': (5, 4),
    #     'Агрегатное состояние': (6, 4),
    #     'Q min': (7, 4),
    #     'Q max': (8, 4),
    #     'Q раб': (9, 4),
    #     'Единицы измерения расхода': (9, 5),
    #     'T min': (10, 4),
    #     'T max': (11, 4),
    #     'T раб': (12, 4),
    #     'Единицы измерения температуры': (12, 5),
    #     'P min': (13, 4),
    #     'P max': (14, 4),
    #     'P раб': (15, 4),
    #     'P расч': (16, 4),
    #     'Падение давления на клапане (макс)': (17, 4),
    #     'Единицы измерения давления': (17, 5),
    #     'Плотность': (18, 4),
    #     'Единицы измерения плотности': (18, 5),
    #     'Вязкость': (19, 4),
    #     'Единицы измерения вязкости': (19, 5),
    #     'Агрессивность': (20, 4),
    #     'Другие особые условия': (21, 4),
    #     'Направление потока': (22, 4),
    #     'Класс герметичности': (23, 4),
    #     'Тип привода': (24, 4),
    #     'Давление питающего воздуха': (25, 4),
    #     'Положение при отсутствии воздуха / электропитания': (26, 4),
    #     'Время открытия / закрытия': (27, 4),
    #     'Ручное управление': (28, 4),
    #     'Уровень безопасности SIL': (29, 4),
    #     'Напряжение питания': (30, 4),
    #     'Взрывозащита': (31, 4),
    #     'Степень защиты': (32, 4),
    #     'Кабельный ввод (сигнал)': (33, 4),
    #     'Марка кабеля (сигнал)': (34, 4),
    #     'Тип конечного выключателя': (35, 4),
    #     'Положение конечного выключателя': (36, 4),
    #     'Взрывозащита конечного выключателя': (37, 4),
    #     'Степень защиты конечного выключателя': (38, 4),
    #     'Соединительная коробка конечного выключателя': (39, 4),
    #     'Кабельный ввод конечного выключателя': (40, 4),
    #     'Марка кабеля конечного выключателя': (41, 4),
    #     'Соединение с процессом': (42, 4),
    #     'Тип фланцев': (43, 4),
    #     'DN фланцев': (44, 4),
    #     'PN фланцев': (45, 4),
    #     'DN существующего клапана': (46, 4),
    #     'PN существующего клапана': (47, 4),
    #     'Изготовитель': (48, 4),
    #     'Модель': (49, 4),
    #     'Примечание': (50, 4)
    # }
}


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

    shift_first_list = (df.shape[0] - 50) // 54
    if (df.shape[0] - 50) % 54 != 0:
        shift_first_list += 1

    df['index'] = df['index'] + 1
    df['Номер листа'] = df['index'] + 5 + shift_first_list
    df['Изменения'] = ''
    df_table_list_positions = df[['Изменения', 'index', 'Позиция', 'Номер схемы', 'Тип сенсора', 'Номер листа']].copy()
    df_ol_table = df[templates['Температура'].keys()].copy()

    return (df_table_list_positions, df_ol_table)


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
    df_ol_table = df[templates['Давление'].keys()].copy()

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
    df_ol_table = df[templates['Расход'].keys()].copy()

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
    df_ol_table = df[templates['Уровень'].keys()].copy()

    return (df_table_list_positions, df_ol_table)

# getPressureForOL()