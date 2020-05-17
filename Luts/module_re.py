'''
Он широко используется в естественной обработке языка, веб-приложениях,
требующих проверки ввода текста (например, адреса электронной почты)
и почти во всех проектах в области анализа данных, которые включают в себя
интеллектуальную обработку текста.
'''
import re

# re.match(pattern, string):
#Этот метод ищет по заданному шаблону в начале строки.
#Метод group() - чтобы вывести содержимое искомой подстроки

result = re.match(r'AV', 'AV Analytics Vidhya AV')
print (result)
print(result.group())
result = re.match(r'Analytics', 'Analytics Vidhya AV')
print (result)
print(result.group())
result = re.match(r'Analytics', 'AV Analytics Vidhya AV')
print (result)
print('-' * 20)

# start() и end() для того, чтобы узнать начальную и конечную позицию найденной строки.
result = re.match(r'AV', 'AV Analytics Vidhya AV')
print(result.start())
print(result.end())
print('-' * 20)

# re.search(pattern, string):
# Этот метод похож на match(), но он ищет не только в начале строки. Возвращает
# первое найденное совпадение. Возвращает объект.
result = re.search(r'Analytics', 'AV Analytics Vidhya AV')
print (result)
print(result.group())
result = re.search(r'AV', 'AV Analytics Vidhya AV')
print (result)
print(result.group())

a = 'ff\nfffffffffff'
b = r'ff\nfffffffffff'
print(a)
print(b)
print('-' * 20)

# re.findall(pattern, string):
# Этот метод возвращает список всех найденных совпадений. У метода findall() нет
# ограничений на поиск в начале или конце строки.
result = re.findall(r'AV', 'AV Analytics Vidhya AV')
print(result)
print('-' * 20)

# re.split(pattern, string, [maxsplit=0]):
# Этот метод разделяет строку по заданному шаблону.
result = re.split(r'y', 'Analytics')
print(result)
result = re.split(r'i', 'Analytics Vidhya')
print(result)
result = re.split(r'i', 'Analytics Vidhya', maxsplit=1)
print(result)
print('-' * 20)

# re.sub(pattern, repl, string):
#Этот метод ищет шаблон в строке и заменяет его на указанную подстроку.
# Если шаблон не найден, строка остается неизменной.
result = re.sub(r'India', 'The World', 'AV is largest Analytics community of India')
print(result)
print('-' * 20)

# re.compile(pattern, repl, string):
#Мы можем собрать регулярное выражение в отдельный объект, который может быть
# использован для поиска. Это также избавляет от переписывания одного и того же выражения.
pattern = re.compile('AV')
result = pattern.findall('AV Analytics Vidhya AV')
print(result)
print('-' * 20)

# Специальные символы регулярных выражений (операторы)
'''
.	Один любой символ, кроме новой строки \n.
?	0 или 1 вхождение шаблона слева
+	1 и более вхождений шаблона слева
*	0 и более вхождений шаблона слева
\w	Любая цифра или буква (\W — все, кроме буквы или цифры)  эквивалентен [a-zA-Z0–9_].
\d	Любая цифра [0-9] (\D — все, кроме цифры)
\s	Любой пробельный символ (\S — любой непробельный символ)
\b	Граница слова
[..]	Один из символов в скобках ([^..] — любой символ, кроме тех, что в скобках)
\	Экранирование специальных символов (\. означает точку или \+ — знак «плюс»)
^ и $	Начало и конец строки соответственно
{n,m}	От n до m вхождений ({,m} — от 0 до m)
a|b	Соответствует a или b
()	Группирует выражение и возвращает найденный текст
\t, \n, \r	Символ табуляции, новой строки и возврата каретки соответственно
'''

# Задача 1: Вернуть первое слово из строки
result = re.findall(r'.', 'AV is largest Analytics community of India')
print(result)
result = re.findall(r'\w', 'AV is largest Analytics community of India')
print(result)
result = re.findall(r'\w*', 'AV is largest Analytics community of India')
print(result)
text = r'AV is largest Analytics community of India'
result = re.findall(r'\w+', text)
print(result)
print('-' * 20)

#Задача посчитать количество знаков препинания в конкретном куске текста.
string = "It was the best of times, it was the worst of times, " \
         "it was the age of wisdom, it was the age of foolishness, " \
         "it was the epoch of belief, it was the epoch of incredulity, " \
         "it was the season of Light, it was the season of Darkness, " \
         "it was the spring of hope, it was the winter of despair, " \
         "we had everything before us, we had nothing before us, " \
         "we were all going direct to Heaven, we were all going direct " \
         "the other way – in short, the period was so far like the " \
         "present period, that some of its noisiest authorities insisted " \
         "on its being received, for good or for evil, in the superlative " \
         "degree of comparison only."
#Первый способ
target = [';','.',',','–']
num_puncts = 0
for punct in target:
    if punct in string:
        num_puncts+=string.count(punct)
print(num_puncts)
# С помощью модуля re
pattern = r'[,;.,–]'
punct = re.findall(pattern,string)
print(len(punct))

pattern = re.compile(r'[,;.,–]')
punct = pattern.findall(string)
print(len(punct))

#Находит в строке подстроки длиной в 6 знаков, начинающиеся с
# “D” или “d” и заканчивающиеся маленькой “e”
pattern = r'[dD]....e'
text = re.findall(pattern,string)
print(text)

