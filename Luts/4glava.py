# Числа
import sys
print(sys.path)

import math
import random

print(2 ** 100)
# print(len(str(2**1000000)))
print(4 * 1.5)
print(3.1415 * 2)

print(math.sqrt(85))
print(math.pi)
print('-' * 30)

print(random.random())
print(random.choice([1, 2, 3, 4, 5]))
print('-' * 30)
#Строки
#Операции над последовательностями
s = 'Spam'
print(s)
print(s[:])
print(s[1])
print(s[::2])
print(s[1::2])
print(s[::1])
print(s[::-1])
print(s[::-2])
print(s[-1])
print(s[3])
print(s[len(s)-1])

for i in s:
    print(i, end=' ')
print()

s = 'z' + s[1:]
print(s)
print('-' * 30)
#Строковые методы
s = 'Spam'
print(s.find('pa'))
print(s.replace('pa', 'XYZ'))
line = 'aaa,bbb,ccccc,dd'
print(line)
print(line.split(','))
print(s.upper())
print(s.isalpha())
line = 'aaa,bbb,ccccc,dd\n'
print(line.rstrip())
print('-' * 30)
a = 'shrubbery'
l = list(a)
print(a)
print(l)
l[1] = 'c'
print(l)
b = ''.join(l)
print(b)
print('-' * 30)

#Фооматирование строк
print('%s, eggs, and %s' % ('spam', 'SPAM!'))
print('{0}, eggs, and {1}'.format('spam', 'SPAM!'))
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d} {3:10d}'.format(x, x*x, x*x*x, x+x))
s = 'spam'
print(dir(s))
print(dir(4))
print(help(s.replace))
print('-' * 30)

print('5A\nB\tC')

msg = ''' aaaaaaaaaaaaa
bbb’’’bbbbbbbbbb””bbbbbbb’bbbb
cccccccccccccc'''
print(msg)
print('-' * 30)

#Unicode
print('sp\xc4m')
print(u'sp\u00c4m')
print('spam')          # Символы могут занимать 1, 2 или 4 байта в памяти
print('spam'.encode('utf8'))    # В UTF-8 кодируется как 4 байта в файлах
print('spam'.encode('utf16'))      # Но в UTF-16 кодируется как 10 байтов
print('spLLLam'.encode('utf8'))
print('sp\xc5\u00c4\U000000c4m')
print('-' * 30)

print('0 \x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f')
print('1 \x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f')
print('2 \x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f')
print('3 \x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f')
print('4 \x40\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f')
print('5 \x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f')
print('6 \x60\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f')
print('7 \x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f')
print('8 \x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f')
print('9 \x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f')
print('a \xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf')
print('b \xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf')
print('c \xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf')
print('d \xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf')
print('e \xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef')
print('f \xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff')
print('-' * 30)
print('2\xb2 * 3\xbd  \xf7')
a = r'f \xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff'
b = a.replace('f', 'a')
print(b)
print('-' * 30)

print('doesn\'t')
print('"Yes," they said.')
print('"Isn\'t," they said.')
print('First line.\nSecond line.')
print('C:\some\name')
print(r'C:\some\name') # r экранирует знак '\'
print('''
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+ ''')

import re
match = re.match('Hello[ \t]*(.*)world', 'Hello Python world')
print(match.group(1))
match = re.match('/(.*)/(.*)/(.*)', '/usr/home/lumberjack')
print(match.groups())
print('-' * 30)

# Списки Lists
L = [123, 'spam', 1.23] # Список из трех объектов разных типов
print(len(L))
print(L[0])
print(L[:-1])
s = L + [4, 5, 6]
print(s)
print(L)
L.append('NI')
print(L)
L.pop(2)
print(L)
M = ['bb', 'aa', 'cc']
print(M)
M.sort()
print(M)
M.reverse()
print(M)
M = [[1, 2, 3], # Матрица 3 x 3 в виде вложенных списков
     [4, 5, 6], # Выражение в квадратных скобках может
     [7, 8, 9]] # занимать несколько строк
print(M)
print(M[1])
print(M[1][1])
col2 = [row[1] for row in M] # Выбирает элементы второго столбца
print(col2)
col2 = [row[1] + 1 for row in M] # Добавить 1 к каждому элементу в столбце 2
print(col2)
col2 = [row[1] for row in M if row[1] % 2 == 0] # отфильтровать нечетные значения
print(col2)
diag = [M[i][i] for i in [0, 1, 2]] # Выборка элементов диагонали матрицы
print(diag)
doubles = [c * 2 for c in 'spam'] # Дублирование символов в строке
print(doubles)
print(list (range (10))) # Создает список
print(list (range (-6,7,2))) # Создает список
print('-' * 20)
print([[х ** 2, х ** 3] for х in range(4)]) # Множество значений,
print([[x, x / 2, x * 2] for x in range(-6, 7, 2) if x > 0]) # фильтры if

# Генераторы
G = (sum(row) for row in M) # Генератор, возвращающий суммы элементов строк
print(G)
print(next(G))
print(sum(M[0]))
print(next(G))
print(sum(M[1]))
print(next(G))
print(sum(M[2]))
print(list(map(sum, M))) # Отобразить sum на элементы в M
print(list)
print({sum(row) for row in M}) # Создать множество сумм элементов в строках
print({i : sum(M[i]) for i in range (3)})# Создать таблицу ключей/значений сумм элементов в строках
print('-' * 20)


#Функция map() применяет функцию к каждому элементу последовательности и возвращает итератор с результатами.
# Привести все строки в верхний регистр
list_of_words = ['one', 'two', 'list', '', 'dict']
print(list_of_words)
print(map(str.upper, list_of_words))
print(list(map(str.upper, list_of_words)))
print('-' * 20)

# BEGIN YIELD_DELEGATE_FIX
def f():
    def do_yield(n):
        yield n
    x = 0
    while True:
        x += 1
        yield from do_yield(x)
# END YIELD_DELEGATE_FIX

if __name__ == '__main__':
    print('Invoking f() now produces a generator')
    g = f()
    print(next(g))
    print(next(g))
    print(next(g))

print('-' * 20)

# function version
def fibon(n):
    a = b = 1
    result = []
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result

# generator version
def fibon2(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


print(fibon(10))
for x in fibon2(10):
    print(x, end=' ')
print()

def createGenerator() :
    mylist = range(3)
    for i in mylist :
        yield i*i

mygenerator = createGenerator() # создаём генератор
print(mygenerator) # mygenerator является объектом!

for i in mygenerator:
    print(i)
print('-' * 20)

#Словари
a = {1:'True', 2 : [1,'False']}
print(a)
print(type(a))
print(dir(a))
D = {'food': 'spam', 'quantity': 4, 'color': 'pink'}
print(D)
print(D['food']) # Извлечь значение, связанное с ключом 'food'
D['quantity'] += 1 # Добавить 1 к значению, связанному с ключом 'quantity'
D['food'] *= 2
print(D)
# Создание словаря
D = {}
D['name'] = 'Denis'
D['job'] = 'Developer'
D['age'] = 43
print(D)
print(D['name'])
# Создание словаря
den1 = dict(name = 'Denis', job = 'dev', age = 43) # Ключевые слова
print(den1)
den2 = dict(zip(['name', 'job', 'age'], ['Denis', 'dev', 43])) # Связывание вместе
print(den2)
print('-' * 20)
rec = {'name':{'first':'Denis', 'last':'Skrynnikov'}, 'job':['developer', 'saler'], 'age': 43}
print(rec)
print(rec['name']) # ’name' - вложенный словарь
print(rec['name']['last']) # Индексация во вложенном словаре
print(rec['job'])  # 'jobs' - вложенный список
print(rec['job'][0]) # Индексация во вложенном списке
rec['job'].append('janitor') # Расширение списка названий должностей на месте
print(rec)
#вложение позволяет строить сложные информационные структуры непосредственно и легко.
гес = 0 # Теперь область памяти, занимаемая объектом, восстановлена
D = {'a': 1, 'c': 3, 'b': 2}
D['e'] = 99
print(D)
print(D['c']) # Присваивание новому ключу увеличивает словари
# print(D['f'])  Ссылка на несуществующий ключ приводит к ошибке
print('f' in D) # Проверяем наличие ключа 'f' в словаре
if not 'f' in D:
     print('missing')
     print('no, really...')  # Блоки операторов вводятся с отступом
value = D.get('x', 0) # Индекс со стандартным вариантом
print(value)
value = D['x'] if 'x' in D else 0 # Форма выражения if/else
print(value)
print(D.keys())
print(D.values())
ks = list(D.keys()) # Неупорядоченный список ключей
print(ks)
ks.sort() # Отсортированный список ключей
print(ks)
for key in ks: # проход по отсортированным ключам
    print(key, ' => ', D[key])

c = 'spam'
c.upper()
print(c)
print(c.upper())
for i in 'spam':
    print(i.upper())
print('-' * 20)

#Кортежи
tpl = (1, 2, 3, 4, 5, 6)
lst = [1, 2, 3, 4, 5, 6]
print(tpl.__sizeof__())
print(lst.__sizeof__())
a = ('hello, world!')
b = tuple('hello, world!')
print(a)
print(b)

T = (1, 2, 3, 4) # Кортеж из 4 элементов
print(len(T))
print(T + (5, 6)) # Конкатенация
print(T[0]) # Индексация, нарезание и т.д.
print(T.index (4)) # Методы кортежей: 4 обнаруживается по смещению 3
print(T.count(4)) # 4 обнаруживается один раз
T = (2,) + T[1:] # Создает новый кортеж для нового значения
print(T)
T = 'spam', 3.0, [11, 22, 33]
print(T[1])
print(T[2][1])
print('-' * 20)

# Файлы
f = open('data.txt', 'w')  # Создать новый файл в режиме записи ('w')
f.write('Hello\n')
f.write('world\n')
f.close() # Закрыть для сбрасывания буферов вывода на диск
f = open('data.txt') # 'r' (чтение) - стандартный режим обработки
text = f.read() # Прочитать все содержимое файла в строку
print(text)  # print интерпретирует управляющие символы
print(text.split()) # Содержимое файла - всегда строка
'''
лучший способ чтения файла в наше время — вообще его не читать,
поскольку файлы предлагают итератор, который автоматически производит чтение
строка за строкой в циклах for и других контекстах'''
for line in open('data.txt'): print(line)
print(type(T))
print(type(f))
print(dir(f))
print(help(f.seek))
print('-' * 20)

# узнаем абсолютный путь к файлу
import os
pit = os.path.abspath('data.txt ')
print(pit)

#Бинарные файлы / байтовые строки
import struct
packed = struct.pack('>i4sh', 7, b'spam', 8) # Создать упакованные двоичные данные
print(packed) #выдаст: 10 байтов, не объекты и не текст
file = open ('data.bin', 'wb') # Открыть двоичный файл для записи
file.write(packed) # Записать упакованные двоичные данные
file.close()

data = open('data.bin' , 'rb').read() # Открыть/прочитать двоичный файл данных
print(data) #10 байтов, неизмененные
print(data[4:8]) # Нарезать байты в середине
print(list(list(data))) # Последовательность 8-битных байтов
print(struct.unpack('>i4sh', data)) # Снова распаковать в объекты


# Адрес в памяти запрашивается функцией id()
string = 'Hello'
print(id(string))
string += ', world!'
print(id(string)) #  печатаем адрес (id) получившегося строкового объекта
print(string)

bi = b'Hello' # Литерал b для объявления байтовой строки
bi2 = b'\xd0\x9f\xd1\x80...'
print(bi)
print(type(bi))
print(type(bi2))
for letter in bi:
    print(letter)

# example_byte = b'привет' # выдаст ошибку: bytes can only contain ASCII literal characters.
# print(example_byte)      # (используются русские буквы)
example_string = 'привет'
print(type(example_string))
print(example_string)
encoded_string = example_string.encode(encoding='utf-8') #  кодируем строку в байты
print(encoded_string)
print(type(encoded_string))
print('\xd0\xbf\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82')
decoded_string = encoded_string.decode() # декодируем байты в строку
print(decoded_string)
print('-' * 20)

# Файлы с текстом Unicode
print('Файлы с текстом Unicode')
S = 'sp\xc4m' # Текст Unicode, отличающийся от ASCII
print(S)
print(S[2]) # Последовательность символов
file = open('unidata.txt', 'w', encoding='utf-8') # Записать/закодировать текст UTF-8
file.write(S) #Записано 4 символа
file.close()
text = open('unidata.txt', encoding='utf-8').read() # Прочитать/декодировать текст UTF-8
print(text)
print(len(text)) # 4 символа (кодовые точки)
raw = open('unidata.txt', 'rb').read() # Читать закодированные байты
print(raw)
print(len(raw)) # 5 байтов в кодировке UTF-8
print('-' * 20)

print(text.encode('utf-8')) # Вручную кодировать в байты
print(raw.decode('utf-8')) # Вручную кодировать в строку
print('-' * 10)

print(text.encode('latin-1')) # Байты отличаются от других
print(text.encode('utf-16'))

print(len(text.encode('latin-1')), len(text.encode('utf-16')))
print(b'\xff\xfes\x00p\x00\xc4\x00m\x00'.decode('utf-16')) # Но декодируются в ту же самую строку

# Множества

