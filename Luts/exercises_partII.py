# Проверьте свои знания: упражнения для части II
# 1. Основы.
print(2 ** 16)
S = "ham"
print(S[:0])
L = [1, 2, 3] + [4, 5, 6]
print(L, L[-2:], L[2:4])
print([L[2], L[3]])
revers = L.reverse()
print(revers)
print(L.sort())
print(L.index(4))
D = {'x': 1, 'y': 2, 'z': 3}
D['w'] = 5
print(D['x'] + D['w'])
D[(1, 2, 3)] = 4
print(D)
print(list(D.keys()), list(D.values()), (1, 2, 3) in D)
print('-' * 20)
# 2. Индексация и нарезание.
L = [0, 1, 2, 3]
print(L[-1000:100])
print(L[3: 1])
L[3:1] = ['?']
print(L)
# 3. Индексация, нарезание и оператор del.
L = [0, 1, 2, 3]
L[2] = []
print(L)
del L[0]
print(L)
del L[1:]
print(L)
L = [0, 1, 2, 3]
# L[1: 2] =1
print('-' * 20)
# 4. Присваивание кортежам,.
X = 'spam'
Y = 'eggs'
X, Y = Y, X
print(X, Y)
print('-' * 20)
# 5. Ключи словарей.
D = {}
D[1] = 'a'
D[2] = 'b'
D[(1, 2, 3)] = 'c'
print(D)
print('-' * 20)
# 6. Индексация словарей.
D = {'a': 1, 'b': 2, 'c': 3}
# print(D['d']) # KeyError: 'd'
D['d'] = 'spam'
print(D)
print('-' * 20)
# 7. Универсальные операции.
# print('spam' + [5]) # TypeError: must be str, not list
# print((1,2) + [5]) # TypeError: can only concatenate tuple (not "list") to tuple
# print({1:'spam', 'c': 3} | {'a': 1, 'b': 2})
dict1 = {1: 'spam', 'a': 1}
dict2 = {'a': 1, 'b': 2, 'c': 3}
dict1.update(dict2)
print(dict1)

dict = {'Имя': 'AndreyEx', 'Возраст': 18}
dict2 = {'Пол': 'Мужской'}
dict.update(dict2)
print("обновление словаря : ", dict)
print('-' * 10)
# 8. Индексация строк
S = "spam"
print(S[0][0][0][0][0])
# 9. Неизменяемые типы.
S = "spam"
results = S[:1] + 'l' + S[2:]
results2 = S[0] + 'l' + S[2:]
print(results, results2)
# 10. Вложение.
data = {'name': ['Denis', 'Alekseevich', 'Skrynnikov'],'age': 43, 'job': ['taxidriver', 'menager'],'adres': 'Murmashi',
        'email': 'lutawolf@yandex.ru', 'phone': 89062874040}
print(data['job'])
print(data['name'])
print(data['name'][2])
print('-' * 20)
# 11. Файлы.
file = open('myfile.txt', 'w')
file.write('Hello file world!')
file.close()
f = open('myfile.txt').read()
print(f)


