# 1.Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


# with open("words.txt", encoding='utf_8') as fin:
#     for line in fin:
#         words = line.split()
#         for word in words:
#             if 'абв' in word:
#                 words.remove(word)
#         sentence = " ".join(words)
#         print(sentence)
#


# 2.Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"


# i = 100
# while i > 0:
#     a = int(input('Игрок 1 введите количество конфет '))
#     if a > 28 or a < 0:
#         raise ValueError('Играй по правилам')
#     elif a < 29 and a > 0:
#         if i - a == 0:
#             print('Победил 1 игрок')
#             break
#         elif i - a <= 0:
#             raise ValueError('Неверный ход')
#         else:
#             i = i - a
#             print(f'Осталось {i} конфет')
#     b = int(input('Игрок 2 введите количество конфет '))
#     if b > 28 or b < 0:
#         raise ValueError('Играй по правилам')
#     elif a < 29 and a >= 0:
#         if i - b == 0:
#             print('Победил 2 игрок')
#             break
#         elif i - b <= 0:
#             raise ValueError('Неверный ход')
#         else:
#             i = i - b
#             print(f'Осталось {i} конфет')


# a) Добавьте игру против бота

# from random import randint
#
#
# i = 100
# while i > 0:
#     a = int(input('Игрок 1 введите количество конфет '))
#     if a > 28 or a < 0:
#         raise ValueError('Играй по правилам')
#     elif a < 29 and a > 0:
#         if i - a == 0:
#             print('Победил 1 игрок')
#             break
#         elif i - a <= 0:
#             raise ValueError('Неверный ход')
#         else:
#             i = i - a
#             print(f'Осталось {i} конфет')
#     if i > 28:
#         b = randint(1,28)
#         i = i - b
#         print(f'Бот Арсений забрал {b} конфет')
#         print(f'Осталось {i} конфет')
#     elif i - b == 0:
#         print('Победил 2 игрок')
#         break
#     elif i < 28:
#         b = randint(1,i)
#         print(f'Бот Арсений забрал {b} конфет')
#         i = i - b
#         print(f'Осталось {i} конфет')
#     elif i - b <= 0:
#         raise ValueError('Неверный ход')
#     else:
#         i = i - b
#         print(f'Осталось {i} конфет')

# # b) Подумайте как наделить бота ""интеллектом""
#
# from random import randint
#
#
# i = 100
# print(f'Всего {i} конфет')
# while i > 0:
#     a = int(input('Игрок 1 введите количество конфет '))
#     if a > 28 or a < 0:
#         raise ValueError('Играй по правилам')
#     elif a < 29 and a > 0:
#         if i - a == 0:
#             print('Победил 1 игрок')
#             break
#         elif i - a <= 0:
#             raise ValueError('Неверный ход')
#         else:
#             i = i - a
#             print(f'Осталось {i} конфет')
#     if i > 56:
#         b = randint(1,29)
#         i = i - b
#         print(f'Бот Арсений забрал {b} конфет')
#         print(f'Осталось {i} конфет')
#     elif i < 55:
#         b = i % 29
#         i = i - b
#         print(f'Бот Арсений забрал {b} конфет')
#         print(f'Осталось {i} конфет')
#     elif i < 28:
#         b = i
#         i = i - b
#         print(f'Бот Арсений забрал {b} конфет')
#         print(f'Осталось {i} конфет')
#         if i - b == 0:
#             print('Победил Бот Арсений')
#             break
#
#
# candies = 150
# print(f'{candies} всего конфет')
# count = randint(1, 2)
# while candies > 0:
#     count += 1
#     if count % 2 == 0:
#         if count == 2:
#             print('ходит бот')
#             quantity = 20
#             print(f'конфет изымаете бот {quantity}')
#         else:
#             print('ходит бот')
#             quantity = 29 - quantity
#             print(f'конфет изымаете бот {quantity}')
#     else:
#         print('ходит игрок')
#         quantity = int(input('Введите число конфет которое изымаете - '))
#     if 0 < quantity < 29:
#         candies -= quantity
#         print(f'конфет осталось - {candies}')
#     else:
#         print('Вы ввели некоректное кол-во конфет, введите число от 1 до 28')
#         count -= 1
#
# if count % 2 == 0:
#     print('победил бот')
# else:
#     print('победил игрок')



# 3.Создайте программу для игры в "Крестики-нолики".

#
# doska = list(range(1,10))
#
# def draw_board(board):
#
#  for i in range(3):
#      print ("|", doska[0+i*3], "|", doska[1+i*3], "|",doska[2+i*3], "|")
#
# def stavim_hod(hod):
#  valid = False
#  while not valid:
#      otvet = input("Введите номер клетки куда поставить значение " + hod+"? ")
#      otv = int(otvet)
#      if otv >= 1 and otv <= 9:
#          if (str(doska[otv-1]) not in "XO"):
#              doska[otv-1] = hod
#              valid = True
#          else:
#              print ("Эта клетка занята")
# def kto_viigral(doska):
#  pobeda = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
#  for x in pobeda:
#      if doska[x[0]] == doska[x[1]] == doska[x[2]]:
#          return doska[x[0]]
#  return False
#
# def igra(doska):
#  count = 0
#  win = False
#  while not win:
#      draw_board(doska)
#      if count % 2 == 0:
#          stavim_hod("X")
#      else:
#          stavim_hod("O")
#      count += 1
#      if count > 4:
#          m = kto_viigral(doska)
#          if m:
#              print (m, "Победил!")
#              win = True
#              break
#      if count == 9:
#          print ("Победила дружба!")
#          break
#  draw_board(doska)
#
# igra(doska)


# 4.Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.


with open('code.txt', 'r') as code:
    code = code.read()

def coding(txt):
    count = 1
    res = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
    return res

def decoding(txt):
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ''
    return res


s = code
print(f"Текст после кодировки: {coding(s)}")
print(f"Текст после дешифровки: {decoding(coding(s))}")
