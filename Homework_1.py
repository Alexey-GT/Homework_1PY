#Задача№1
""" a = int(input('Введите цифру обозначающую день недели: '))
if 1 <= a <= 5:
    print('Не выходной день')
elif 5 < a < 8: 
    print('Выходной день')  
else: 
    print('Введенная цифра не обозначает ни один из дней недели') """

#Задача№2
""" for x in [True,False]:
    for y in [True,False]:
        for z in [True,False]:
            print(not (x or y or z) == (not x) and (not y) and (not z)) """ 

#Задача№3
""" x = int(input('Введите координату Х:'))
y = int(input('Введите координату Y:'))
if x == 0 or y == 0:
    print("Error")
if x > 0 and y > 0:
    print('Первая четверть')
elif x < 0 and y > 0:
    print('Вторая четверть')
elif x < 0 and y < 0: 
    print('Третья четверть')
elif x > 0 and y < 0:
    print('Четвертая четверть') """
        
#Задача№4
""" n = int(input('Введите номер четверти:'))
if n in [1,2,3,4]:
    if n == 1: 
        print('X > 0, Y > 0')
    if n == 2:
        print('X < 0, Y > 0') 
    if n == 3:
        print('X < 0, Y < 0') 
    if n == 4:
        print('X > 0, Y < 0')
else:      
    print('Введите другую цифру!!!') """


#Задача№5
""" import math
x1 = int(input('Введите координату X первой точки:'))
y1 = int(input('Введите координату Y первой точки:'))
x2 = int(input('Введите координату X второй точки:'))
y2 = int(input('Введите координату Y второй точки:'))
l = round(math.sqrt((x2 - x1)**2 + (y2 - y1)**2),2)
print(l) """


