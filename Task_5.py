#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
#Пример:
#- A (3,6); B (2,1) -> 5,09
#- A (7,-5); B (1,-1) -> 7,21

ax = float(input('Введите Ах = '))
ay = float(input('Введите Ау = '))
bx = float(input('Введите Вх = '))
by = float(input('Введите Ву = '))
 
from math import sqrt
distance = round(sqrt(pow(bx - ax, 2) + pow(by - ay, 2)), 2)

print('Расстояние между А и В = ', distance)

