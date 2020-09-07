your_tuple = (2, 3, [4, 5])
your_tuple[2].append(6)
your_tuple[2].extend([7, 8, 9])
your_tuple[2].__iadd__([111])
your_tuple[2][2] = 666
print(your_tuple)
# your_tuple[2]+=[10,11,12]

found_coins = 20
magic_coins = 70
stolen_coins = 3
coins = 0
for week in range(1, 53):
    coins = coins + magic_coins - stolen_coins
    print('Неделя %s = %s' % (week, coins))
print('-' * 20)
print(print.__doc__)  # Docstring-это то, что вы найдете в верхней части функции, например:
# или Ctrl и нажать мышкой на функцию

import sys

print(sys.getsizeof(your_tuple))

l = [1, 4, 55]
print(max(l))
print(1 + float('inf'))  # inf — infinity — Бесконечность

# Объединение словарей
d1 = {4: 150, 'b': 'Hello ', 3: 100}
d2 = {1: 50, 'b': 'world', 3: 100}
d = d1.copy()
for k, v in d2.items():
    d[k] = d.get(k, 0) + v
print(d)

dict1 = {1: 'spam', 'a': 1}
dict2 = {'a': 1, 'b': 2, 'c': 3}
dict3 = dict1.update(dict2)
print(dict3)

import datetime

t = "01:50:47".split(":")
print(t)
print(datetime.timedelta(hours=int(t[0]), minutes=int(t[1]), seconds=int(t[2])).total_seconds())

print(set([1, 3, 5, 7]) - set([1, 2, 4, 5, 6]))
print(set([1, 2, 4, 5, 6]) - set([1, 3, 5, 7]))
print('-' * 20)

print(False == False in [False])
a = 2, 3
print(a)
print(type(1/ 2))

a = [1,2,4]
b = [3,5,6]
print([a,b])
print(a + b)

a = '<lastmod>2020-07-23T19:14:21+06:00</lastmod>, <lastmod>2020-07-23T19:15:09+06:00</lastmod>, ' \
    '<lastmod>2020-07-23T16:54:26+06:00</lastmod>, <lastmod>2020-07-23T16:52:07+06:00</lastmod>'
b = a.split(',')
print(b)

a = 'storage;'
d = a.rstrip(';')
print(d)

a = 5.96
print(a.real)



