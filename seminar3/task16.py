'''
Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

Пример:
5
1 2 3 4 5
3
-> 1
'''
import random

number = (int(input("Введите количество элементов в массиве - ")))
massiv = []
for i in range(number):
    massiv.append(int(input(f'Введите {i+1}-ое число: ')))

x = (int(input("Введите X - ")))
cnt = 0
cnt = massiv.count(x)

print(*massiv)
print(x)
print(f'-> {cnt}')