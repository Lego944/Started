# 1.Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.
#
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

# number = int(input('Введите число '))
# if 1 > number or number > 7:
#     print('В недели всего 7 дней!')
# elif number > 5 and number < 8:
#     print('Да')
# else:
#     print('Нет')


# 2.Напишите программу для. проверки истинности
# утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
#
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             print(not (x or y or z) == (not x and not y and not z))
#             print(x, y, z)


# 3.Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).
#
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3


# 4.Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

# numCor = int(input('Введите номер координатной четверти '))
# if numCor < 5 and numCor >0:
#     if numCor == 1:
#         print('X > 0 и Y > 0')
#     if numCor == 2:
#         print('X < 0 и Y > 0')
#     if numCor == 3:
#         print('X < 0 и Y < 0')
#     if numCor == 4:
#         print('X > 0 и Y < 0')
# else:
#     print('Введено число больше диапазона четверти или отрицательное!')


# 5.Напишите программу, которая принимает на вход координаты двух точек и
# находит расстояние между ними в 2D пространстве.
#
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

# from math import sqrt
# xa = int(input('Введите координату точки A по X '))
# ya = int(input('Введите координату точки A по Y '))
# xb = int(input('Введите координату точки B по X '))
# yb = int(input('Введите координату точки B по Y '))
#
# res = sqrt((xa - xb)**2 + (ya - yb)**2)
# print(round(res, 2))
