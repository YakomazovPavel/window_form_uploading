# print('Привет, Марина!')

# name1 = 'Марина! и '
# name2 = 'Паша!'

# # print('Привет,', name)

# def ptint_hello(p1, p2):
#     print('Hello,', p1 + p2)

# ptint_hello(name1, name2)

# import os

# path = os.path.split("/Users/pavelakomazov/Desktop/Python_Project/window_form_uploading/Doc1.docx")
# print(path)
# print(type(path[0]))
# path = os.path.split(path[0])
# print(type(path))
# print(path)




def wrapper(func):
	def inner(*args, **kwargs):
		print('after')
		func(*args, **kwargs)
		print('befor')
	return inner

@wrapper
def print_hello(name=''):
	print(f'Hello, {name}!')


print_hello()
print('')
print_hello('Yakomazov Pavel')