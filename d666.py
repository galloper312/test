# 1 задача # a = int(input('Введи 1 число: '))
# b = int(input('Введи 2 число: '))
# c = input('Выбери функцию */-+: ')
# if c == '*':
#     print(a*b)
# elif c == '/':
#     print(a/b)
# elif c == '-':
#     print(a-b)
# elif c == '+':
#     print(a+b)
# else:
#     print('Такой функции нет!')

# 3 задача# print('Регистрация')
# c = []
# a = input('Введи логин: ')
# b = int(input('Введи пароль: '))
# c.append(a)
# c.append(b)
# print('Войти')
# login = input('Введи логин: ')
# password = int(input('Введи пароль: '))
# if login == a:
#     print('Добро пожаловать!!')
# elif password == b:
#      print('Добро пожаловать!!')   
# else:
#     print('Не проавельный логин и пароль')


# 2/2

#  Напишите код, который выведет на экран список языков с нумерацией.
#             languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
#             Вывод:
#             0 go
#             1 java
#             2 php
#             3 python
#             4 javascript
#             5 ruby





# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# for i in languages:
#     a = i.index()
#     print(a+1, i)

# a = []
# for i in range(1,1000):
#     if i % 5 == 0:
#         a.append(i)
#     elif i % 3 == 0:
#         a.append(i)
# print(sum(a))



# print(4+7+2+9+4+6+1+0+8+4)

# # a = {}
# year = int(input('Введи год: '))
# month = int(input('Введи месяц: '))
# day = int(input('Введи день: '))
# # time = float(input('Введи время : '))
# date1 = datetime.date(year,month,day)
# # a['year'] = year
# # a['month'] = month
# # a['day'] = day
# # a['time'] = time
# # print(a)


# a = int(input('Введи дату'))
# print(a)

# a = int(input('Введите данные через -: '))
# s = a.split("-")
# # print(s)


# year,month,day = map(int, date_entry.split('-'))
# date1 = datetime.date(year,month,day)





city = ['Bishkek', 'Osh', 'Batken', 'NewYork']

commands = input('''Выберите действие:
1. Добавить 
2. Отобразить
3. Заменить город
4. Удалить город
5. Выход \n>>> ''').lower()
if commands == 'добавить':
    new_city = input('Введите название города: ')
    if new_city in city:
        print('Такой город уже есть')
    else:
        city.append(new_city)
        print(city)
elif commands == 'отобразить':
    print(city)
elif commands == 'заменить':
    print(city)
    zam = input('какой город хотите заменить?: ')
    zamna = input('На какой город хотите заменить?: ')
    d = city.index(zam)
    if zam in city:
        city.insert(d, zamna)
        city.pop(d + 1)
        print(city)
    elif zam not in city:
        print('такого города нет')
elif commands == 'удалить':
    print(city)
    try:
        a = input('Какой город хотите удалить?: ')
        d = city.index(a)
        if a in city:
            city.pop(d)
            print(city)
    except ValueError:
        print('Такого города нет!!')
elif commands == 'выход':
    print('Вы вышли))')
    exit()