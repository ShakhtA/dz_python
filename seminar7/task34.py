'''
Задача 34:
Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает,
Вам стоит написать программу.
Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”,если с ритмом все не в порядке.

*Пример:*

**Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
**Вывод:** Парам пам-пам  
'''

def count_letters(text, letters_set):
    count = 0
    for letter in text:
        if letter in letters_set: count +=1
    return count
    
text = input("Введите фразу: ")
text_list = text.split(' ')
letters_set = {'а', 'е', 'и', 'о', 'у', 'э', 'ю', 'я'}
count_list = []
for el in text_list:
    count_list.append(count_letters(el, letters_set))

rythm = True
for el in count_list[1:]:
    if count_list[0] != el:
        rythm = False
        break
if rythm: print("Парам пам-пам")
else: print("Парам пам")
