# # print('Привет, Марина!')
#
# # name1 = 'Марина! и '
# # name2 = 'Паша!'
#
# # # print('Привет,', name)
#
# # def ptint_hello(p1, p2):
# #     print('Hello,', p1 + p2)
#
# # ptint_hello(name1, name2)
#
# # import os
#
# # path = os.path.split("/Users/pavelakomazov/Desktop/Python_Project/window_form_uploading/Doc1.docx")
# # print(path)
# # print(type(path[0]))
# # path = os.path.split(path[0])
# # print(type(path))
# # print(path)
#
# from multiprocessing import Process
# import os
#
#
# def wrapper(func):
#     def inner(*args, **kwargs):
#         print('after')
#         func(*args, **kwargs)
#         print('befor')
#
#     return inner
#
#
# @wrapper
# def print_hello(name=''):
#     print(f'Hello, {name}!')
#
# def print_hello_2():
#     print(f'Hello,!!')
#
#
# def create_process(func):
#     process = Process(target=func)
#     # process.daemon = True
#     process.daemon = False
#     process.start()
#
#
# def deamon_start_process(func, *args, **kwargs):
#     process = Process(target=func, args=args, kwargs=kwargs)
#     process.daemon = False
#     process.start()
#
#
# # @start_process
# def func_0(name, age, year, none=None,):
#     print_hello(f'Yakomazov {name}, {age}, {year}, {none}')
#     print('parent process:', os.getppid())
#     print('process id:', os.getpid())
#
#
# if __name__ == '__main__':
#     # deamon_start_process(func_0, 'Miha', age=22.5, year=2028)
#     deamon_start_process(print_hello_2)
#
#     # print_hello(name='Pavel')
# # print_hello()
# # print('')
# # print_hello('Yakomazov Pavel')

# import subprocess
import os

# from webbrowser import open
# from paths import SETTINGS
# path = os.path.abspath(SETTINGS["dir_shared_save_directory"])
# subprocess.Popen(fr'explorer "{path}"', shell=True)
# open('https://docs.google.com/spreadsheets/d/1zz7GVckuuoLFdDCAu8aqRtGZcPSZE4mfZzeyAgltGpY/edit#gid=1199393205',
#      new=2)

# 'https://docs.google.com/spreadsheets/d/1_BLHqOV_s9Vq-4nN6lfwY_DsyJJNKtzqDRtwJDPFo6A/edit#gid=0'
# BASE_DIR = os.getcwd()
# path = os.path.join(base_dir, 'Выгрузка_2_2', 'JK')
# print(os.path.split(path)[0])
# path = r'C:\Users\PavelYa\PycharmProjects\window_form_uploading\Выгрузка_2_2\ОЛ'
# if not os.path.exists(path):
#     os.makedirs(path)

# paths = [
#     os.path.join(BASE_DIR, 'Выгрузка'),
#     os.path.join(BASE_DIR, 'Выгрузка', 'Опросные листы'),
#     os.path.join(BASE_DIR, 'Шаблоны')
# ]
#
# for path in paths:
#     if not os.path.exists(path):
#         os.makedirs(path)

d = {
    "a": 1,
    "b": 1,
}

# d.pop("a")
d.update({"c": 0})
print()
