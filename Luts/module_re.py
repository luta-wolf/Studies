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

print('match()')
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
print('start() и end()')
result = re.match(r'AV', 'AV Analytics Vidhya AV')
print(result.start())
print(result.end())
print('-' * 20)

# re.search(pattern, string):
# Этот метод похож на match(), но он ищет не только в начале строки. Возвращает
# первое найденное совпадение. Возвращает объект.
print('search()')
result = re.search(r'Analytics', 'AV Analytics Vidhya AV')
print (result)
print(result.group())
result = re.search(r'AV', 'AV Analytics Vidhya AV')
print (result)
print(result.group())
print('-' * 20)

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
если REGEXP — шаблон, то (?:REGEXP) — эквивалентный ему шаблон
---------------------------------------------------------------
MAC-адрес сетевого устройства обычно записывается как шесть групп из двух шестнадцатиричных цифр, 
разделённых символами - или :. Например, 01:23:45:67:89:ab. Каждый отдельный символ 
можно задать как [0-9a-fA-F], и можно весь шаблон записать так:
[0-9a-fA-F]{2}[:-][0-9a-fA-F]{2}[:-][0-9a-fA-F]{2}[:-][0-9a-fA-F]{2}[:-][0-9a-fA-F]{2}[:-][0-9a-fA-F]{2}
Или с помощью (?:...) вот так:
[0-9a-fA-F]{2}(?:[:-][0-9a-fA-F]{2}){5}

Шаблон для поиска телефонных номеров:
(?:\+7|8)(?:-\d{2,3}){4}	
+7-926-123-12-12, 8-926-123-12-12
Шаблон для поиска телефонных emeil:
[\w'._+-]{1,64}@[\w'._+-]{1,255}
'''

#Пример использования всех основных функций
match = re.search(r'\d\d\D\d\d', r'Телефон 123-12-12')
print(match[0] if match else 'Not found')
# -> 23-12
match = re.search(r'\d\d\D\d\d', r'Телефон 1231212')
print(match[0] if match else 'Not found')
# -> Not found

match = re.fullmatch(r'\d\d\D\d\d', r'12-12')
print('YES' if match else 'NO')
# -> YES
match = re.fullmatch(r'\d\d\D\d\d', r'Т. 12-12')
print('YES' if match else 'NO')
# -> NO

print(re.split(r'\W+', 'Где, скажите мне, мои очки??!'))
# -> ['Где', 'скажите', 'мне', 'мои', 'очки', '']

print(re.findall(r'\d\d\.\d\d\.\d{4}',
                 r'Эта строка написана 19.01.2018, а могла бы и 01.09.2017'))
# -> ['19.01.2018', '01.09.2017']

for m in re.finditer(r'\d\d\.\d\d\.\d{4}', r'Эта строка написана 19.01.2018, а могла бы и 01.09.2017'):
    print('Дата', m[0], 'начинается с позиции', m.start())
# -> Дата 19.01.2018 начинается с позиции 20
# -> Дата 01.09.2017 начинается с позиции 45

print(re.sub(r'\d\d\.\d\d\.\d{4}',
             r'DD.MM.YYYY',
             r'Эта строка написана 19.01.2018, а могла бы и 01.09.2017'))
# -> Эта строка написана DD.MM.YYYY, а могла бы и DD.MM.YYYY