# with open('users.txt', 'a') as f:
#     login = input("Введите логин: ")
#     password = input("Введите пароль: ")
#     f.write(f'Логин: {login} \n Пароль: {password}')
# print('Успешно создан файл с логином')


# a = open('users.txt', 'w') as f:
#     for i in a:
#         i == 'w':
#         print('Да, в тексте есть w')






# ls -R > all.txt запись всех файлов  в текст # для первого задачи

# with open('/home/dair/directories.txt', 'r')as f:
#     a = (f.read())

# with open('text_666.txt', 'w')as f:
#     f.write(a)


# with open('pythin.txt', 'r')as f:
#     a = f.read()
# count_t = 0
# count_tt = 0
# for i in a:
#     if i == 't':
#         count_t += 1
#     elif i == 'T':
#         count_tt += 1
# print(count_t)
# print(count_tt)


# for i in a:
#     i == 't'
# print(i)



# import math
# r = int(input('Введите радиус круга: '))
# s = math.pi*r*r
# print('площадь круга ', s)



#     print(key) показывает только ключи

# print(a['2132323']) # показывает значении выбранного ключа

# for value in a['2132323'].values():
#     print(value)     # показывает значение вложенной значении

# print(a['2342345']['name']) #показывает выбранную значение

# for value in a.values():
#     for i,j in value.items():
#         print(f'{i} : {j}')