'''
Задача 22.
Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
Затем пользователь вводит сами элементы множеств.
'''

list1 = []
list2 = []
sizeList1 = int(input("Введите количество элементов первого набора - "))
print("Введите числа первого набора")
for i in range(sizeList1):
    list1.append(int(input()))
print(list1)

sizeList2 = int(input("Введите количество элементов второго набора - "))
print("Введите числа второго набора")
for i in range(sizeList2):
    list2.append(int(input()))
print(list2)

list1.extend(list2)
list1.sort()
print(set(list1))
