# Введение в операторы Python
# Зашифрованный ответ Google
a = '\u0050\u0075\u007a\u006c\u0065\u0073\u0020' \
    '\u0061\u0072\u0065\u0020\u0066\u0075\u006e\u002e' \
    '\u0020\u0053\u0065\u0061\u0072\u0063\u0068\u0020\u006f\u006e\u002e'
print(a)  # Puzles are fun. Search on.
print('-' * 20)

'''
Присваивания (Создание ссылок) a, b = 'good', 'bad'
Вызовы и другие выражения (Выполнение функций) log.write("spam, ham")
Вызовы print (Вывод объектов) print ('The Killer', joke)
if/elif/else (Выбор действий) if "python" in text: 
                                  print(text)
for/else (Итерация) for x in mylist: 
                        print(x)
while/else (Универсальные циклы) while X > Y: 
                                     print('hello')
pass (Пустой заполнитель) while True: 
                              pass
break (Выход из цикла) while True:
                         if exittest(): break
continue (Продолжение цикла) while True:
                               if skiptest () : continue
def (Функции и методы) def f(a, b, c=1, *d) :
                           print(a+b+c+d[0])
return (Результаты функций) def f (a, b, c=l, *d):
                                return a+b+c+d[0]
yield (Генераторные функции) def gen(n):
                                 for i in n: yield i*2
global (Пространства имен) х = 'old'
                           def function():
                               global x, у; x = 'new'
nonlocal (Пространства имен) def outer():
                                 x = 'old'
                                 def function():
                                     nonlocal x; x = 'new'
import (Доступ к модулям) import sys
from (Доступ к атрибутам) from sys import stdin
class (Построение объектов) class Subclass(Superclass):
                                staticData = []
                                def method (self) : pass
try/except/finally (Перехват исключений) try:
                                             action()
                                         except:
                                             print('action error')
raise (Генерация исключений) raise EndSearch(location)
assert (Отладочные проверки) assert X > Y, 'X too small’
with/as (Диспетчеры контекста) with open ('data') asmyfile:
                                   process(myfile)
del (Удаление ссылок) del data[k]
                      del data[i:j]
                      del obj.attr
                      del variable
'''
print(input.__doc__)
print('-' * 20)
import string

print(string.ascii_letters)  # выводит все буквы в нижнем и вержнем регистре
print(string.ascii_lowercase)  # Содержит все символы нижнего регистра ASCII:
print(string.ascii_uppercase)  # Содержит все символы ASCII в верхнем регистре:
print(string.digits)  # Содержит все десятичные цифры:
print(string.hexdigits)  # Содержит все шестнадцатеричные символы:
print(string.punctuation)  # Содержит все символы , которые считаются знаки препинания в C локали:
print(string.whitespace)  # Содержит все символы ASCII, которые считаются пробелами:
print('-' * 20)
# Специальные правила для операторов
a = 1; b = 2; print(a + b)  # Три оператора в одной строке
#вы можете разнести одиночный оператор на множество строк.
mylist = [1111,
          2222,
          3333]
A = 1; B =2; C = 3; D = 4
X = (A + B +
     C + D)
if (A == 1 and
    B == 2 and
    C == 3):
    print('spam' * 3)
x = A + B + \
    C + D # Подверженная ошибкам более старая альтернатива
y = 3
if x > y: print(x)
'''while True:
    reply = input('Enter text: ')
    if reply == 'stop': break
    print(reply.upper())
while True:
    reply = input('Enter text: ')
    if reply == 'stop': break
    print(int(reply) ** 2)
print('Bye')'''
# Обработка ошибок путем проверки ввода
s = '123';
t = 'xxx'
print(s.isdigit(), t.isdigit())
'''
while True:
    reply = input('Enter text: ')
    if reply == 'stop':
        break
    elif not reply.isdigit():
        print('Bad!' * 8)
    else:
        print(int(reply) ** 2)
print('Bye!')
print('=' * 20)

# Обработка ошибок с помощью оператора try
while True:
    reply = input('Enter text: ')
    if reply == 'stop':
        break
    try:
        num = int(reply)
    except:
        print('Bad!' * 8)
    else:
        print(num ** 2)
print('Bye!')
print('=' * 20)

# Вложение кода на три уровня в глубину
while True:
    reply = input('Enter text: ')
    if reply == 'stop':
        break
    elif not reply.isdigit():
        print('Bad!' * 8)
    else:
        num = int(reply)
        if num < 20:
            print('low')
        else:
            print(num ** 2)
print('Bye!')
print('=' * 20)

while True:
    reply = input('Enter text: ')
    if reply == 'stop':
        break
    try:
        print(int(reply) ** 2)
    except:
        print('Bad!' * 8)
print('Bye!')
print('=' * 20)'''
#  Поддержка чисел с плавающей точкой
while True:
    reply = input('Enter text: ')
    if reply == 'stop':
        break
    try:
        print(float(reply) ** 2)
    except:
        print('Bad!' * 8)
print('Bye!')
print('=' * 20)
