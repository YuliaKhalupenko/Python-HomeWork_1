#Напишите программу, которая по заданному номеру четверти, 
#показывает диапазон возможных координат точек в этой четверти (x и y).

quarter = float(input('Введите номер четверти = '))

if (quarter == 1): 
    print('Диапазон точек в 1 четверти x > 0, y > 0')
elif (quarter == 2):
    print('Диапазон точек в 2 четверти x < 0, y > 0')
elif (quarter == 3):
    print('Диапазон точек в 3 четверти x < 0, y < 0')
elif (quarter == 4):
    print('Диапазон точек в 4 четверти x > 0, y < 0')
elif (quarter > 4) or (1 < quarter):
    print('Четверть не существует')