import re
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
print('-' * 20)

'''Задачка
В Индии используются PAN номера для налоговой идентификации вместо SSN номеров в США. 
Основной критерий действительности PAN — все буквы должны быть заглавными, 
а символы должны располагаться в следующем порядке:
<char><char><char><char><char><digit><digit><digit><digit><char>
Вопрос:
‘ABcDE1234L’ — действительный PAN?
'''
match=re.search(r'[A-Z]{5}[0–9]{4}[A-Z]','ABcDE1234L')
if match:
    print(True)
else:
    print(False)
print('-' * 20)

#Задачка найти доменные имена
string = '''
<div class="reflist" style="list-style-type: decimal;">
<ol class="references">
<li id="cite_note-1"><span class="mw-cite-backlink"><b>^ ["Train (noun)"](http://www.askoxford.com/concise_oed/train?view=uk). <i>(definition – Compact OED)</i>. Oxford University Press<span class="reference-accessdate">. Retrieved 2008-03-18</span>.</span><span title="ctx_ver=Z39.88-2004&rfr_id=info%3Asid%2Fen.wikipedia.org%3ATrain&rft.atitle=Train+%28noun%29&rft.genre=article&rft_id=http%3A%2F%2Fwww.askoxford.com%2Fconcise_oed%2Ftrain%3Fview%3Duk&rft.jtitle=%28definition+%E2%80%93+Compact+OED%29&rft.pub=Oxford+University+Press&rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal" class="Z3988"><span style="display:none;"> </span></span></span></li>
<li id="cite_note-2"><span class="mw-cite-backlink"><b>^</b></span> <span class="reference-text"><span class="citation book">Atchison, Topeka and Santa Fe Railway (1948). <i>Rules: Operating Department</i>. p. 7.</span><span title="ctx_ver=Z39.88-2004&rfr_id=info%3Asid%2Fen.wikipedia.org%3ATrain&rft.au=Atchison%2C+Topeka+and+Santa+Fe+Railway&rft.aulast=Atchison%2C+Topeka+and+Santa+Fe+Railway&rft.btitle=Rules%3A+Operating+Department&rft.date=1948&rft.genre=book&rft.pages=7&rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook" class="Z3988"><span style="display:none;"> </span></span></span></li>
<li id="cite_note-3"><span class="mw-cite-backlink"><b>^ [Hydrogen trains](http://www.hydrogencarsnow.com/blog2/index.php/hydrogen-vehicles/i-hear-the-hydrogen-train-a-comin-its-rolling-round-the-bend/)</span></li>
<li id="cite_note-4"><span class="mw-cite-backlink"><b>^ [Vehicle Projects Inc. Fuel cell locomotive](http://www.bnsf.com/media/news/articles/2008/01/2008-01-09a.html)</span></li>
<li id="cite_note-5"><span class="mw-cite-backlink"><b>^</b></span> <span class="reference-text"><span class="citation book">Central Japan Railway (2006). <i>Central Japan Railway Data Book 2006</i>. p. 16.</span><span title="ctx_ver=Z39.88-2004&rfr_id=info%3Asid%2Fen.wikipedia.org%3ATrain&rft.au=Central+Japan+Railway&rft.aulast=Central+Japan+Railway&rft.btitle=Central+Japan+Railway+Data+Book+2006&rft.date=2006&rft.genre=book&rft.pages=16&rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook" class="Z3988"><span style="display:none;"> </span></span></span></li>
<li id="cite_note-6"><span class="mw-cite-backlink"><b>^ ["Overview Of the existing Mumbai Suburban Railway"](http://web.archive.org/web/20080620033027/http://www.mrvc.indianrail.gov.in/overview.htm). _Official webpage of Mumbai Railway Vikas Corporation_. Archived from [the original](http://www.mrvc.indianrail.gov.in/overview.htm) on 2008-06-20<span class="reference-accessdate">. Retrieved 2008-12-11</span>.</span><span title="ctx_ver=Z39.88-2004&rfr_id=info%3Asid%2Fen.wikipedia.org%3ATrain&rft.atitle=Overview+Of+the+existing+Mumbai+Suburban+Railway&rft.genre=article&rft_id=http%3A%2F%2Fwww.mrvc.indianrail.gov.in%2Foverview.htm&rft.jtitle=Official+webpage+of+Mumbai+Railway+Vikas+Corporation&rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal" class="Z3988"><span style="display:none;"> </span></span></span></li>
</ol>
</div>
'''
#Найти все основные домены в тексте
# askoxford.com; bnsf.com; hydrogencarsnow.com; mrvc.indianrail.gov.in; web.archive.org

match=re.findall(r'http(s:|:)\/\/(www.|ww2.|)([0-9a-z.A-Z-]*\.\w{2,3})',string)
for elem in match:
    print(elem)

# Это регулярное выражение ищет адресс электронной почты
match=re.findall(r'([\w0-9-._]+@[\w0-9-.]+[\w0-9]{2,3})',string)
print('-' * 20)

# Задача 1: Вернуть первое/последнее слово из строки
string = r'AV is largest Analytics community of India'
result = re.findall(r'.', string)
print(result)
result = re.findall(r'\w', string)
print(result)
result = re.findall(r'\w*', string)
print(result)
result = re.findall(r'\w+', string)
print(result)
result = re.findall(r'^\w+', string)
print(result)
result = re.findall(r'\w+$', string)
print(result)
print('-' * 20)

#Задача 2: Вернуть первые два символа каждого слова
string = 'AV is largest Analytics community of India'
result = re.findall(r'\w{2}', string)
print(result)
result = re.findall(r'\w\w', string)
print(result)
result = re.findall(r'\b\w\w', string)
print(result)
result = re.findall(r'\b\w.', string)
print(result)
print('-' * 20)

#Задача 3: вернуть список доменов из списка адресов электронной почты
string = 'abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz'
result = re.findall(r'@\w+[.]\w+', string)
print(result)
result = re.findall(r'@\w*.\w*', string)
print(result)
result = re.findall(r'@(\w+\.\w+)', string)
print(result)
result = re.findall(r'@\w+.(\w+)', string)
print(result)
print('-' * 20)

#Задача 4: Извлечь дату из строки/год
string = 'Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009'
result = re.findall(r'\d+-\d+-\d+', string)
print(result)
result = re.findall(r'\d{2}-\d{2}-\d{4}', string)
print(result)
result = re.findall(r'\d{2}-\d{2}-(\d{4})', string)
print(result)
print('-' * 20)

#Задача 5: Извлечь все слова, начинающиеся на гласную/на согласную
string = 'AV is largest Analytics community of India'
result = re.findall(r'\w+', string)
print(result)
result = re.findall(r'[aeiouAEIOU]\w+', string)
print(result)
result = re.findall(r'\b[aeiouAEIOU]\w+', string)
print(result)
result = re.findall(r'\b[^aeiouAEIOU]\w+', string)
print(result)
result = re.findall(r'\b[^aeiouAEIOU ]\w+', string)
print(result)
print('-' * 20)

#Задача 6: Проверить телефонный номер (номер должен быть длиной 10 знаков и начинаться с 8 или 9)
li = ['9999999999', '999999-999', '99999x9999', '8990978900', '8999993333333']
for i in li:
    if re.match(r'[89]{1}\d{9}', i) and len(i) == 10:
        print('yes')
    else:
        print('no')
print('-' * 20)

#Задача 7: Разбить строку по нескольким разделителям
line = 'asdf fjdk;afed,fjek,asdf,foo' # String has multiple delimiters (";",","," ").
result = re.split(r'[; ,]', line)
result2 = re.sub(r'[;,]', ' ', line)
print(result)
print(result2)
print('-' * 20)

'''
Задача 8: Извлечь информацию из html-файла
Допустим, нам надо извлечь информацию из html-файла, заключенную между <td> и </td>, 
кроме первого столбца с номером. Также будем считать, что html-код содержится в строке.
'''
test_str = '1NoahEmma2LiamOlivia3MasonSophia4JacobIsabella5WilliamAva6EthanMia7MichaelEmily'
result = re.findall(r'\d([A-Z][A-Za-z]+)([A-Z][A-Za-z]+)', test_str)
print(result)
print('-' * 20)
'''
Задача 01. Регистрационные знаки транспортных средств
В России применяются регистрационные знаки нескольких видов.
Общего в них то, что они состоят из цифр и букв. Причём используются только 12 букв кириллицы, 
имеющие графические аналоги в латинском алфавите — А, В, Е, К, М, Н, О, Р, С, Т, У и Х.
У частных легковых автомобилях номера — это буква, три цифры, две буквы, затем две или 
три цифры с кодом региона. У такси — две буквы, три цифры, затем две или три цифры с кодом региона. 

Вам потребуется определить, является ли последовательность букв корректным номером указанных 
двух типов, и если является, то каким.
На вход даются строки, которые претендуют на то, чтобы быть номером. Определите тип номера. 
Буквы в номерах — заглавные русские. Маленькие и английские для простоты можно игнорировать.
'''
def number(string):
    pattern_private = r'[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}'
    pattern_taxi = r'[АВЕКМНОРСТУХ]{2}\d{5,6}'
    if re.match(pattern_private, string) == True:
        print('Private')
    elif re.match(pattern_taxi, string) == True:
        print('Taxi')
    else:
        print('False')

#tests
number('С227НА777')
number('КУ22777')
number('Т22В7477')
number('М227К19У9')
number(' С227НА777')

'''
Задача 04. Замена времени
Вовочка подготовил одно очень важное письмо, но везде указал неправильное время.
Поэтому нужно заменить все вхождения времени на строку (TBD). Время — это строка 
вида HH:MM:SS или HH:MM, в которой HH — число от 00 до 23, а MM и SS — число от 00 до 59.
'''
string = '''Уважаемые! Если вы к 09:00 не вернёте 
чемодан, то уже в 09:00:01 я за себя не отвечаю. 
PS. С отношением 25:50 всё нормально!'''
pattern = r'[012]\d(?:[:][012345]\d){1,2}'
print(re.sub(pattern, '(TBD)', string))
print('-' * 20)

'''
Задачка
Есть последовательность из 10 цифр , нужно первую цифру заменить на 8.
Вход: 5952869134
Выход: 8952869134
'''
def phone_number2(number):
    replace_number = re.sub('\d+', '8', number)
    return print(replace_number + number[1:])

def phone_number(number):
    replace_number = re.sub('^\d{1}', '8', number)
    return print (replace_number)



#tests
phone_number('5952869134')
phone_number('7952869134')
phone_number('8952869134')
phone_number('4952869134')

string = '101100010000'
zerro = re.findall(r'[0]+\b', string)
print(len(''.join(zerro)))
print('-' * 20)
'''
Задача 07. Шифровка
Владимиру потребовалось срочно запутать финансовую документацию. Но так, чтобы это 
было обратимо.Он не придумал ничего лучше, чем заменить каждое целое число 
(последовательность цифр) на его куб. Помогите ему.
'''
string = 'Было закуплено 12 единиц техники по 410.37 рублей.'
encryption = re.findall(r'\d+', string)
print(encryption)

#Задача убрать из текста всю строку, если в ней находится определенное слово
song = "It was the best of times, it was the worst of times,\n " \
         "it was the age of wisdom, it was the age of foolishness,\n " \
         "it was the epoch of belief, it was the epoch of incredulity,\n " \
         "it was the season of Light, it was the season of Darkness,\n " \
         "it was the spring of hope, it was the winter of despair,\n " \
         "we had everything before us, we had nothing before us,\n " \
         "we were all going direct to Heaven, we were all going direct\n " \
         "the other way – in short, the period was so far like the\n " \
         "present period, that some of its noisiest authorities insisted\n " \
         "on its being received, for good or for evil, in the superlative\n " \
         "degree of comparison only.\n"
new_song = []
for line in song.split('\n'):
    if 'degree' not in line:
        new_song.append(line)
song = '\n'.join(new_song)