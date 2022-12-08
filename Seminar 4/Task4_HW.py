# 1.Вычислить число c заданной точностью d
#
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$


# from cmath import pi
# d = int(input('Введите точность числа после запятой: '))
# print(f'Число заданной точностью {d} = {round(pi,d)}')



# 2.Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.


# num = int(input("Введите число: "))
# i = 2
# lst = []
# old = num
# while i <= num:
#     if num % i == 0:
#         lst.append(i)
#         num //= i
#         i = 2
#     else:
#         i += 1
# print(f"Простые множители числа {old} приведены в списке: {lst}")



# 3.Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.


# from random import randint
#
# N = int(input('Введите число определяющее диапазон: '))
# lst = []
# for i in range(1, N + 1):
#     a = randint(-N, N + 1)
#     lst.append(a)
# print(lst)
#
# newlist = []
# for i in lst:
#     if i not in newlist:
#         newlist.append(i)
# print(newlist)



# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
#
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


# from random import randint
#
# k = int(input("Введите степень k: "))
#
# factor = []
# for i in range(1, k +2):
#     factor.append(randint(1, 101))
#
# result = []
# for i in range(len(factor)):
#     if k == 1:
#         result.append(f'{factor[i]}*x')
#     elif k == 0:
#         result.append(f'{factor[i]}')
#     else:
#         result.append(f'{factor[i]}*x^{k}')
#     signs = randint(0, 1)
#     if signs == 1:
#         result.append('+')
#     elif signs == 0:
#         result.append('-')
#     k -= 1
#
# result.pop(-1)
# result.append('=0')
#
# record = open('data.txt', 'w')
# record.write(''.join(result))
# record.close()



# 5.Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.


with open('Text_1.txt', 'w', encoding='utf-8') as file:
    file.write('2*x^2 + 5*x^5')
with open('Text_2.txt', 'w', encoding='utf-8') as file:
    file.write('23*x^4 + 9*x^6')

with open('Text_1.txt', 'r') as file:
    Text_1 = file.readline()
    list_of_text_1 = Text_1.split()
with open('Text_2.txt', 'r') as file:
    Text_2 = file.readline()
    list_of_text_2 = Text_2.split()

print(f'{list_of_text_1} + {list_of_text_2}')
sum_Text = list_of_text_1 + list_of_text_2

with open('sum_Text.txt', 'w', encoding='utf-8') as file:
    file.write(f'{list_of_text_1} + {list_of_text_2}')




