'''
Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
В случае с английским алфавитом очки распределяются так:
A, E, I, O, U, L, N, S, T, R – 1 очко;
D, G – 2 очка; B, C, M, P – 3 очка;
F, H, V, W, Y – 4 очка;
K – 5 очков; J, X – 8 очков; Q, Z – 10 очков.
А русские буквы оцениваются так: 
А, В, Е, И, Н, О, Р, С, Т – 1 очко;
Д, К, Л, М, П, У – 2 очка;
Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков.
Напишите программу, которая вычисляет стоимость введенного пользователем слова.
Будем считать, что на вход подается только одно слово, которое содержит либо только английские,
либо только русские буквы.

Пример:

ноутбук
12
'''

listOnePoint = ["A", "E", "I", "O", "U", "L", "N", "S", "T", "R", "А", "В", "Е", "И", "Н", "О", "Р", "С", "Т"]
dict_listOnePoint = dict.fromkeys(listOnePoint, 1)
listTwoPoint = ["D", "G", "Д", "К", "Л", "М", "П", "У"]
dict_listTwoPoint = dict.fromkeys(listTwoPoint, 2)
listThreePoint = ["B", "C", "M", "P", "Б", "Г", "Ё", "Ь", "Я"]
dict_listThreePoint = dict.fromkeys(listThreePoint, 3)
listFourPoint = ["F", "H", "V", "W", "Y", "Й","Ы"]
dict_listFourPoint = dict.fromkeys(listFourPoint, 4)
listFivePoint = ["K", "Ж", "З", "Х", "Ц", "Ч"]
dict_listFivePoint = dict.fromkeys(listFivePoint, 5)
listEightPoint = ["X", "Ш", "Э", "Ю"]
dict_listEightPoint = dict.fromkeys(listEightPoint, 8)
listTenPoint = ["Q", "Z", "Ф", "Щ", "Ъ"]
dict_listTenPoint = dict.fromkeys(listTenPoint, 10)

generalDict = dict_listOnePoint.copy()
generalDict.update(dict_listTwoPoint)
generalDict.update(dict_listThreePoint)
generalDict.update(dict_listFourPoint)
generalDict.update(dict_listFivePoint)
generalDict.update(dict_listEightPoint)
generalDict.update(dict_listTenPoint)

word = input("Введите слово: ")
result = 0

for i in word:
    result += generalDict[str.upper(i)]

print(result)