'''
Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

Пример:

5
    1 2 3 4 5
    6
    -> 5
'''

#======== Ввод данных =================================

number = (int(input("Введите количество элементов в массиве - ")))
massiv = []
for i in range(number):
    massiv.append(int(input(f'Введите {i+1}-ое число: ')))
tempMassiv = massiv.copy()

#=========== Блок вычислений ====================================
x = (int(input("Введите X - ")))
tempMassiv.append(x)
tempMassiv.sort()

idx = tempMassiv.index(x)
if (idx != len(tempMassiv) - 1) and (idx != 0) :
    if (tempMassiv[idx] - tempMassiv[idx - 1]) > (tempMassiv[idx + 1] - tempMassiv[idx]):
        near = tempMassiv[idx + 1]
    else:
        near = tempMassiv[idx - 1]
elif idx == 0:
    near = tempMassiv[idx + 1]
else:
    near = tempMassiv[idx - 1]

#========= Вывод результата ==========================
print('Размер массива = ', number)
print(*massiv)
print("Число = ", x)
print(f'Ближайшим к числу {x} является {near}')