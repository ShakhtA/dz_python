'''
Задача 32:
Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону
(т.е. не меньше заданного минимума и не больше заданного максимума)
'''
import random
size = int(input("Ведите размер массива - "))
array = []
for i in range(size):
    array.append(random.randint(-100, 100))
print(array)

intMax = int(input("Введите максимальное число - "))
intMin = int(input("Введите минимальное число - "))

indexArray = []
for i in range(size):
    if intMin < array[i] < intMax: indexArray.append(i)

print(indexArray)