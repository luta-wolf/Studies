import re
text = open('only_one_word.txt').read() #Объект строка

text = re.findall(r'\w*[Аа]', text)
#words = sorted(text.lower().split())
print(len(text))
print(len(sorted(set(text))))
words = "\n".join(sorted(set(text)))
file = open('only_one_word.txt2', 'w')  #Объект файл
file.write(words)
file.close()
print(dir(text)) #Объект строка:
print(dir(file)) #Объект файл