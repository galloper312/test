# Циклы - for while
# a = ['dias', 'nazgul', 'nurdik']
# for i in a:
#     if i == 'dias':
#         print('Ok')
#     else:
#         print('дальше другие имена')

# for i in range(1,10):
    # print(i)

a = []
b = int(input('Введите число: '))
for i in range(b):
    a.append(i)
print(a)


# count = 0
# a = [1,2,3,4,5,5,5,5,5,5,5,5,5,5,5,5,6,7,8,9]
# for i in a:
#     if i == 5:
#         count += 1
# print(count)

# count = 0
# for i in a:
#     if i ==4:
#         print('Наша i хранит в себе 4')
#     else:
#         count +=1
# print(count)

# for i in range(1,11):
#     b = 5
#     c = b * i
#     print(f'{b} * {i} = {c}')

# for i in range(10,1,-1):
#     print(i)

# a = ['bishkek', 'kant', 'tokmok', 'osh']
# b = int(input('Введите число: '))
# for i in range(len(a)):
#     if b == i:
#         print(a[i])

# a = ['bishkek', 'kant', 'tokmok', 'osh']
# for i in a:
#     if i == 'kant':
#         a.remove(i)
# print(a)

# i = 100
# while i < 1000:
#     print(i)
#     i /= 1

# count = 0
# a = int(input('Введи число: '))
# while a != 1:1
#     print('Repeat')
#     count += 1
#     a = int(inout('введите число: '))
# print(f'Вы потратили {count} попыток')

# a = [1,2,3]*5
# print(a)
# while 3 in a:
#     a.remove(3)
#     print(a)

# for i in range(1,10):
#     if i == 5:
#         break
#     print(i)


# lst = ['alice', 'alex', 'bob', 'carl', 'dave']
# x = 'chris'
# i = 2
# lst[i] = x
# print(lst)

# for i in 'Hello python':
#     print(i*2, end=',')

# lst = ['alice', 'alex', 'bob', 'carl', 'dave']
# a = tuple(lst)
# print(a) # конвертация список в тюпл

# for i in 'hello world':
#     if i =='w':
#         continue # игнорирует заданную символ
#     print(i, end='')

# a = 0
# while a < 5:
#     a += 1
#     if a == 3:
#         break
#     print(a)


# while True:
#     print('Бесконечный цикл')

# while True:
#     a = int(input('n= '))
#     if len(str(a)) != 3:
#         print('No')
#     else:
#         print('Yes')
#         break

# b = 'hello world'
# for i in enumerate(b): # нумирует каждый символ
#     print(i)

# guess = input('Enter password: ')
# password = 'qwerty'
# count = 0
# while guess != password:
#     count += 1
#     print('Wrong password')
#     guess = input('enter password: ')
# print(f'Вы потратили {count} попыток')

# a = []
# b = input("Добавь имя")

# for _ in range(10):
#     a.append(b)
# print(a)


# a = ['Jack', 'Jimmy', 'Jackson', 'Jhon', 'Jackson', 'Jhon',  'Jimmy', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon',123, 321, 2, 543, 64, 463, 234, 867, 6234, 63246, 3, 43]
# numbers = []
# leters = []
# for i in a:
#     if type(i) == str:
#         leters.append(i)
#     else:
#         numbers.append(i)
# print(leters)
# print(numbers)

# while i in a == str:
#     leters.append(a)
# print(numbers)

# a = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# b = 'Rust'
# if b in a:
#     print('this languages is in list')
# else:
#     print('')

# a = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# a = 0
# while a != 'php':
#     a += a[1]
#     if a == 'php':
#         break

# a = 7
# print(7 ** 5)

# b =  ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# for i in enumerate(b): 
#     print(i)

# a = list(range(1,20))
# for i in a:
#     if i > 9:
#         a.reverse()
#     print(i, end= ' ')





# a = []
# for i in range(1,11):
#     print(i,end='')
# while i in range(10,0):
#     print(i,end='')

# a = ('Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан',)
# print(a[0::2])


# a = ('Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан',)
# print(a[0::2])

# a = int(input('Введите число: '))
# if a > 99:
#     print('это число трехзначное')
# elif a % 2 == 0:
#     print('число четное')
# elif a % 31 == 0:
#     print ('Это число делится на 31 без остатка')
# elif a > 100 and a % 17 == 0:
#     print('это число делится на 17 без остатка и больше 100')
# elif a > 150 and a == 13 ** 2:
#     print(a)


# a = list(range(-100,100))
# for i in a % 13 == 0:
#     if i % 2 == 0:
#         print(i ** 2)
# if a ([-100:100:7])

