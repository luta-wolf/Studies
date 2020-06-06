import re
text = open('only_one_word.txt').read() #Объект строка
text = re.sub(r'[\W\d]', ' ', text)
words = sorted(text.lower().split())
print(len(words))
print(len(sorted(set(words))))
words = "\n".join(sorted(set(words)))
file = open('only_one_word.txt2', 'w')  #Объект файл
file.write(words)
file.close()