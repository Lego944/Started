# 1.Напишите программу, которая принимает на вход вещественное число и
# показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0.56 -> 11


# d = float(input('Введите вещественное число: '))
# d = str(d).replace('.', '')
# out = sum(map(int, d))
# print(out)



# 2.Напишите программу, которая принимает на вход число N и
# выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


# n = int(input('Введите число N: '))
# f = 1
# for i in range(n):
#     i = i + 1
#     f = i * f
#     print(f, end=" ")



# 3.Задайте список из n чисел последовательности
#  (1 + 1/n) ** n выведите на экран их сумму.


# n = int(input('Введите количество чисел в списке: '))
# def numbers(n):
#     sum = 0
#     for i in range(n):
#         a = int(input(f'Введи число {i + 1} '))
#         a = (1+1/a)**a
#         sum = a + sum
#         i += 1
#     return sum
# print('Сумма чисел =',round((numbers(n)), 2))


# 4.Задайте числами список из N элементов, заполненных из
# промежутка [-N, N]. Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.
#
#
# from random import Random, randint
#
# N = int(input('Введите число: '))
# numbers = []
# for i in range(N):
#     numbers.append(randint(-N, N + 1))
# print(numbers)
#
# f = open('file.txt', 'w')
# while True:
#     s = input('Укажите индекс для вычисления - ')
#     print('Если указали все индексы введите stop')
#     if s == "stop":
#         break
#     f.write(s + "\n")
# f.close()
#
# result = 1
# f = open('file.txt', 'r')
# for line in f:
#     if line == "stop":
#         break
#     result *= numbers[int(line)]
# f.close()
# print('Результат вычислений =', result)



# 5.Реализуйте алгоритм перемешивания списка
# (shuffle использовать нельзя, другие методы из библиотеки random - можно).


# from random import Random, randint
#
# N = int(input('Введите число: '))
# numbers = []
# for i in range(N):
#     numbers.append(randint(-N,N+1))
# print(numbers)
#
# def smes(numbers):
#     list = numbers[:]
#     numbers_length = len(list)
#     for i in range(numbers_length):
#         index = randint(0, numbers_length - 1)
#         temp = list[i]
#         list[i] = list[index]
#         list[index] = temp
#     return list
# print(smes(numbers))