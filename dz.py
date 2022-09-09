# a = ['hello', 'python', 'love0', 'i' ]
# a.remove('i')
# print(a.index('love0')

# names = ['aktan', 'kanykey', 'kanat', 'egdira', 'rimura', 'bael', 'nik',]
# print(names[:len(names)//2])
# print(names.index('kanat'))
# a = list(range(0,100,4))
# print(a.extend(a))

# lst = ['nurdik', 'alisher', 'eliza', 'agil', 'azamat', 'dair', 'nazgul', 'tajibay', 'bekmamat', 'aidai', 'dias', 'olga', 'husan']
          #0           #1        #2        #3        #4         #5           #6             #7          #8         #9      #10       #11       #12                            
# a = [1,2,3,4,5,6,7,8,9,10]
# start stop step
# print(lst[:])
# print(lst[0:6:1])
# print(a[4:])
# print(a[:3])
# print(a[0:5])
# print(a[1:8:2])                               #-2           #-1
# print(a[0:7:2])
# print(a[::2])
# print(a[:-5:-1])
# print(a[2], a[6], a[-6])
# print(a[2:7])
# a = 'Hello python'
# print(a[:])

# str1 = ['hello', 'python', 'love', 'i']
# print(str1[0], str1[3], str1[2], str1[1])



# a = ['azat', 'alex', 'bakai', 'john', 'akyl','akyl','akyl','akyl',]

# a.append('beka')#добавляет элемент в конец списка
# a.append('bob')
# a.append('nik')
# a.append('abrakadabra')
# name = input('Введи имя: ')
# a.append(name)
# print(a)

# a = ['azat', 'alex', 'bakai', 'john', 'akyl','akyl','akyl','akyl']
# a.pop(4)
# # print(a)
# a.remove('akyl') # удаляет элемент по названию
# print(a)
# a.pop(2)#удаляет элемент по индексу
# print(a)
# print(a.index('akyl'))
# print(a)

# b = a.count('akyl')# cчитает заданные элементы
# print(a.count('akyl'))

# a = 'asdasdasdasd'
# print(a.count('a'))


# lst1 = ['bael', 'bael','bael','bael','bael','bael','bael']

# lst2 = ['aktan', 'kanykei', 'kanat', 'egdira', 'rimuru','nik']


# lst1.extend(lst2)#обьеденяет два списка
# print(lst1)

# print(len(lst1)) # возвращает длину списка

# len1 = len(lst2)
# l = len1 // 2
# # print(l)
# mid = lst2[0:l]
# print(mid)


# names = []
# name1 = input('Enter name 1: ')
# name2 = input('Enter name 2: ')
# name3 = input('Enter name 3: ')
# name4 = input('Enter name 4: ')
# name5 = input('Enter name 5: ')

# names.append((name1, name2, name3,name4,name5))
# names.extend([name1,name2,name3,name4,name5])
# print(names)

# names = ['nurdik', 'alisher', 'eliza', 'agil', 'dair']
# print(names)

# name = input('Введите имя для удаления: ')
# if name in names:
#     names.remove(name)
# else:
#     print(f'В списке нету имени: {name}')
# print(names)


# names = [('Maga', 40), ('Sultan', 18)]

# name = input('Введите имя: ')
# age = int(input('Введите возраст: '))
# names.append((name,age))
# print(names)



# names = ['aktan', 'kanykei', 'kanat', 'egdira', 'rimuru', 'bael', 'nik']
# text = '123455678'
# text = list(text)
# # print(text)
# # name = len(names) // 2
# # print(names[:name])
# # print(names[:len(names)//2])
# # print(names.index('kanat'))
# # print(names[-2:-5:-1])
# # print(a)
# # a = [1,2,3,4,5,6,7,8,9,10]
# # a.reverse()#разворачивает наш список
# # print(a)
# # a = list(range(0, 100, 4))
# # print(a[24], a[19], a[14], a[9], a[4])
# # a = 'хакеры слили в сеть данные пакистанской энергетической компании k-Electric'
# # print(a.startswith("х"))
# # print(a.endswith("c"))
# # print(a.title())
# # print(a.upper())
# # print(a.lower())
# # print(a.replace("а", "3"))
# # print('привет ' * 10)
# # a = []
# # a1 = input('Enter your name: ')
# # a2 = input('Enter your name: ')
# # a3 = input('Enter your name: ')
# # a4 = input('Enter your name: ')
# # a5 = input('Enter your name: ')
# # b = a.append([a2, a1, a3, a4,])
# # print(b)

# # a = list(range(0, 100, 4))
# # # print(a[24], a[19], a[14], a[9], a[4])

# # a = [('fd'), ('fd'), ('df'), ('dh'), ('eh')]
# # print(a)

# # a = ('g', 'b', 'c')
# # print(a[0])
# # print(a[1])
# # print(a[2])

# a = []
# b = ['abc']
# c = [123]
# d = [True]
# e = [3.14]
# h = [('lst1')]
# a.extend(b)
# a.extend(c)
# a.extend(d)
# a.extend(e)
# a.extend(h)
# print(a)

# a = ['aman','baha','gabar', 'mihail', 'bogdan']
# b = []
# print(b.join(a))

# a = ['Jack', 'Jimmy', 'Jackson']
# b = ['Jhon', 'Jackson', 'Jhon']
# b.extend(a)
# print(b)

# a = ['Jack', 'Jimmy', 'Jackson', 'Jhon', 'Jackson', 'Jhon',  'Jimmy', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon',]
# print(a.count('Jack'))

# a = []
# a.append('Dair')
# a.append('18')
# a.append('python')
# print(a)

# a = ["int", "str", "bool", "if", "else", "elif", "loop"]
# a.pop(6)
# print(a)

a  = [123, 321, 2, 543, 64, 463, 234, 867, 6234, 63246, 3, 43]
print(a[0] * a[1] * a[2] * a[3] * a[4] * a[5] * a[6] * a[7] * a[8] * a[9] * a[10] * a[11])

# a = ["int", "str", "bool", "if", "else", "elif", "loop"]
# print(a[1:3:])

# a = ['oskar','Jack', 'Jimmy', 'Jackson', 'Jhon', 'Jackson', 'Jhon',  'Jimmy', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon',]
# a.remove('oskar')
# print(a)


# numbers = []
# letters = []

# a = []
# a.append('dair')
# a.append('123')
# a.append('True')
# print(a)