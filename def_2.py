# def kvad(x, n=2):
#     return x ** n

# print(kvad(12, 3))


# def login(name, age=20):
#     return f'Ваше имя {name}, Ваш возраст {age}'
# print(login('alex', 30))

# def zaglushka():
#     pass

# def func(*args):
#     return f'{args} {type(args)}'

# print(func(1,2,3,4,5,6,7))

# def func(**kwargs):
#     return f'{kwargs} {type(kwargs)}'
# print(func(key = 'value', name = 'azat'))


# def whi(x):
#     if x % 2 == 0:
#         return f'{x} - четное'
#     return f'{x} - не четное'

# for i in range(20):
#     print(whi(i))


# def cet(x): 
#     if x % 2 == 0:
#         return True
#     return False

# for i in range(20):
#     if cet(i):
#         print(f'{i} - cet')
#     else:
#         print(f'{i} - necet')




# def gen():
#     from random import choice
#     num = '0444'
#     for _ in range(6):
#         num += choice('145790')
#     return num
# print(gen())

# for i in range(10):
#     print(i+1 f'Ваш номер телефона {gen()}')

# 0444441104



# def add(a, b):
#     return a + b
# def substract(a, b):
#     return a - b
# def multiply(a, b):
#     return a * b
# def divide(a, b):
#     return a / b
# print(f'Сложения - {add(10, 2)}, Вычитание - {substract(10,2)}, Умножение - {multiply(10,2)}, Деление - {divide(10,2)}')



# def jwhjf():
#     count = 0
#     a = input('веди слово: ')
#     for i in a:
#         count += 1
#     print(count)
# jwhjf()



# dict1 = {'key':'value'}
# dict2 = {'value': 'key'}
# print(dict1.extend(dict2))
# print(dict1)

# def hgis(dict1, dict2):
#     dict1 = {'key': 'value'}
#     dict2 = {'value': 'key'}
#     return dict1.update(dict2)


# print(hgis())




# def merge(D1,D2):
#     py={**D1,**D2}
#     return py
# D1 = {"loginID":"xyz","country":"USA"}
# D2 = {"firstname":"justin","lastname":"lambert"}
# D3 =(merge(D1,D2))
# print(D3)


# def file():
#     with open

# def file():
#     with open ('menu.txt', 'w') as f:
#         food = input('Что хотите заказать?: ')
#         drink = input('Выпить что желаете?: ')
#         f.write(f'Вы заказали {food}, и {drink}')
# file()


# from asyncore import write


# def file():
#     a = input('Введи слово: ')
#     with open(a, 'w')as f:
#         f.write(f'тут')
# file()

# def print1():
#     print('Главная функция')
#     def print2():
#         print('Вложенная функция')
#     print2()
# print1()





# a = int(input('Введи число: '))
# k = 0
# for i in range(2, a//2+1):
#     if (a%i == 0):
#         k = k+1
# if (k <= 0):
#     print('Простое число')
# else:
#     print('Число не является простым')        


# def text():
#     a = int(input('Введи число: '))
#     return  

# def imya(a, b=5000):
#     print(f'{a} - {b}')


# imya('dair')

# def chislo():
#     n = int(input('Введи число N: '))




# def gen():
#     n = int(input('Введи число N: '))
#     from random import choice
#     for _ in range(n):

# print(gen())



# def n(b, diapazon):
#     a = []
#     for i in range(diapazon):
#         b = input('>>>>')
#         a.append(b)
#     return a

# diapazon = int(input('введи диапазон'))

# print(n(diapazon))

dict1 = {
    'afhj': 'dfaskln0',
    'dljah': 'dkja',
    'hkafb': 'kjs',
}

tuple2() = tuple(dict1.keys)
tuple1() = tuple(dict1.values)
print(tuple1())
print(tuple2)