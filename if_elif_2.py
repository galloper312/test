# '''
# transport = input('какой вид транспорта вы выбираете: самолет, поезд, автобус:')
# if transport == 'Самолет':
#     tiket_type = input('Каким классом вы хотите лететь: ')
#     if tiket_type == 'эконом'
#         place = input('Где вы хотите лететь: у окна, в проходе: ')
#     else:
#         place = 'у вас свой зал'

password = int(input('Введите пароль: '))
if password == 321:
    print('правильно')
else:
    print('Не правильно повторите попытку')
    exit()
food = input('Что закажете: шаурма, самса, пирожок: ')

if food == 'шаурма':
    sostav1 = input('С какой начинкой вы хотите?: мясо, курица: ')
    if sostav1 == 'мясо':  
        nom1 = int(input('Сколько шт хотите?: '))
        warm = input('Нужно ли разогреть: да, нет: ')
        drink = input('Что будете пить: чай, кофе, кола, минералка: ')
        if drink == 'чай' or 'кофе' or 'кола' or 'минералка':
            print('Вы заказали', food, sostav1, nom1, 'шт', 'вы взяли', drink)
        else:
            print('Вы заказали', food, sostav1, nom1, 'шт', 'клиент не взял напиток')

    elif sostav1 == 'курица':
        nom1 = int(input('Сколько хотите?: '))
        warm = input('Нужно ли разогреть: да, нет: ')
        drink = input('Что будете пить: чай, кофе, кола, минералка: ')
        if drink == 'чай' or 'кофе' or 'кола' or 'минералка':
            print('Вы заказали', food, sostav1, nom1, 'шт', 'вы взяли', drink)
        else:
            print('Вы заказали', food, sostav1, nom1, 'шт', 'клиент не взял напиток')

elif food == 'самса':
    sostav1 = input('Какую начинку вы хотите: мясо, курица, сыр: ')
    if sostav1 == 'мясо':  
        nom1 = int(input('Сколько хотите?: '))
        warm = input('Нужно ли разогреть: да, нет: ')
        drink = input('Что будете пить: чай, кофе, кола, минералка: ')
        if drink == 'чай' or 'кофе' or 'кола' or 'минералка':
            print('Вы заказали', food, sostav1, nom1, 'шт', 'вы взяли', drink)
        else:
            print('Вы заказали', food, sostav1, nom1, 'шт', 'клиент не взял напиток')

    elif sostav1 == 'курица':
        nom1 = int(input('Сколько хотите?: '))
        warm = input('Нужно ли разогреть: да, нет: ')
        drink = input('Что будете пить: чай, кофе, кола, минералка: ')
        if drink == 'чай' or 'кофе' or 'кола' or 'минералка':
            print('Вы заказали', food, sostav1, nom1, 'шт', 'вы взяли', drink)
        else:
            print('Вы заказали', food, sostav1, nom1, 'шт', 'клиент не взял напиток')



    elif sostav1 == 'сыр':
        a = input('самсы с сыро закончилиь, будете ждать: да, нет: ')
        if a == 'да': 
            nom1 = int(input('Сколько хотите?: '))
            warm = input('Нужно ли разогреть: да, нет: ')
            drink = input('Что будете пить: чай, кофе, кола, минералка: ')
            if drink == 'чай' or 'кофе' or 'кола' or  'минералка':
                print('Вы заказали', food, sostav1, nom1, 'шт', 'вы взяли', drink)
            else:
                print('Вы заказали', food, sostav1, nom1, 'шт', 'клиент не взял напиток')

        elif a == 'нет':
            print('желаете что нибудь еще заказать?' )


elif food == 'пирожок':
    sostav1 = input('Какую начинку вы хотите: картошка, капуста: ')
    if sostav1 == 'картошка':  
        nom1 = int(input('Сколько хотите?: '))
        warm = input('Нужно ли разогреть: да, нет: ')
        drink = input('Что будете пить: чай, кофе, кола, минералка: ')
        if drink == 'чай' or 'кофе' or 'кола' or 'минералка':
            print('Вы заказали', food, sostav1, nom1, 'шт', 'вы взяли', drink)
        else:
            print('Вы заказали', food, sostav1, nom1, 'шт', 'клиент не взял напиток')


    
    
    elif sostav1 == 'капуста':  
        nom1 = int(input('Сколько хотите?: '))
        warm = input('Нужно ли разогреть: да, нет: ')
        drink = input('Что будете пить: чай, кофе, кола, минералка: ')
        if drink == 'чай' or 'кофе' or 'кола' or 'минералка':
            print('Вы заказали', food, sostav1, nom1, 'шт', 'вы взяли', drink)
        else:
            print('Вы заказали', food, sostav1, nom1, 'шт', 'клиент не взял напиток')


else:
    print('К сожалению такого блюда нет, желаете что нибудь другое заказать?')
