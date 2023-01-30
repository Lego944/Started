# list = [(i, (i ** 2)) for i in (1, 2, 3, 5, 8, 15, 23, 38) if i % 2 == 0]
# print(list)


# li = [x for x in range(1, 20)]
# li = list(map(lambda x:x+10, li))
# print(li)


# data = list(map(int,input().split()))
# print(data)


# def where(f, col):
#     return [x for x in col if f(x)]

# решение без where с помощью filter
# data = '1 2 3 5 8 15 23 38'.split()
#
# res = map(int, data)
# res = filter(lambda x: not x % 2, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)

#
# data = [x for x in range(10)]
#
# res = list(filter(lambda x: not x % 2, data))
# print(res)


# zip позволяет соединять списки по порядку.
# Максимальная длина соединненных списков равна длине минимального списка
# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111, 222, 333]
#
# data = list(zip(users, ids, salary))
# print(data)


# enumerate нумерует список начиная с 0
# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111, 222, 333]
#
# data = list(enumerate(users))
# print(data)
