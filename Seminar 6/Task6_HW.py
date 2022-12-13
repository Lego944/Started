# 1.Наибольший общий делитель

# from math import gcd
#
# print('Вводите число и нажимите Enter, чтобы каждое новое значение было с новой строки.')
# print('Для остановки режима ввода и чтобы узнать НОД, нажмите просто Enter.')
# sp = []
# print('Введите число: ')
#
# while True:
#     num = input()
#     if num == '':
#         break
#     else:
#         sp.append(int(num))
#
# while len(sp) >= 2:
#     sp[0] = gcd(sp[0], sp[1])
#     del sp[1]
#
# print('НОД для введенного списка чисел =', *sp)



# 2.Орел и решка


# s = 'ООООРРРРОРОРРРРРРРРООРОРОРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРР'
# Eagl = []
# count = 0
# print('Исходный текст: ', s)
#
# for i in range(0, len(s) - 1):
#     if s[i] == s[i + 1]:
#         count += 1
#     elif s[i] != s[i + 1]:
#         count += 1
#         Eagl.append(count)
#         Eagl.append(s[i])
#         count = 0
#     if i == (len(s) - 2) and s[-2] != s[-1]:
#         Eagl.append(1)
#         Eagl.append(s[i])
#     elif i == (len(s) - 2) and s[-2] == s[-1]:
#         count += 1
#         Eagl.append(count)
#         Eagl.append(s[i])
#
# print(Eagl)
# max = 0
# for i in range(len(Eagl)):
#     if Eagl[i] == 'Р' and Eagl[i - 1] > max:
#         max = Eagl[i - 1]
#
# if max > 0:
#     print('Наибольшее количество подряд выпавших Решек -', max)
# else:
#     print(0)



# 3.Задача
# Измените код одной-двух решенных ранее задач (с прошлых семинаров или домашних работ),
# применив лямбды, filter, map, zip, enumerate, списочные выражения.


# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

#[1.1, 1.2, 3.1, 5.03, 10.01] => 0.19

# numb_list = [1.1, 1.2, 3.1, 5.03, 10.01]
#
# dr = list(map(lambda x: (int(x * 100 % 100)), numb_list))
# max_dr = max(dr)
# min_dr = min(dr)
#
# print(numb_list)
# print((max_dr - min_dr) / 100)

