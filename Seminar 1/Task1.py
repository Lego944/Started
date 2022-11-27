# 1.Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.

# print('Программа принимает два числа и проверяте является ли одно число квадратом другого.')
# number1 = int(input('Введите первое число '))
# number2 = int(input('Введите второе число '))
#
# if number1 ** 2 == number2 or number2 ** 2 == number1:
#     print('Является')
# else:
#     print('Не является')


# 2.Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

# num = 0
# number = int(input('Введите число '))
# max_num = number
# while num < 4:
#     number = int(input('Введите число '))
#     if number > max_num:
#         max_num = number
#     num += 1
# print(max_num)

# sp = list()
# for i in range(5):
#     n = int(input('Введите число '))
#     sp.append(n)
# print(max(sp)


# 1.Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

# number_N = int(input('Введите число '))
# for i in range(-number_N, number_N + 1):
#     print(i, end=' ')


# 2.Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.

# number = input('Введите число ').split('.')
# print(number)
# print(number[1][0])


# number = float(input('Введите число '))
# print(int(number * 10) % 10)


# 3.Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

# number = int(input('Введите число '))
#
# if number % 30 != 0 and (number % 10 == 0 or number % 15 == 0):
#     print(True)
#
# else:
#     print(False)


# Дополнительная задача. Проверка числа на четность.

# number = int(input('Введите число '))
# if number % 2 == 0:
#     print('Четное')
# else:
#     print('Нечетное')

# Допольнительная задача. Из трехзначного числа вывести второй знак.

# number = int(input('Введите число '))
# print(number // 10 % 10)

