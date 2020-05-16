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
print(type(L))