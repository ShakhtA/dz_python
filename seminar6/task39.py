'''
Даны два массива чисел. Требуется вывести те элементы
первого массива (в том порядке, в каком они идут в первом
массиве), которых нет во втором массиве. Пользователь вводит
число N - количество элементов в первом массиве, затем N
чисел - элементы массива. Затем число M - количество
элементов во втором массиве. Затем элементы второго массива
7 
3 1 3 4 2 4 12 
6
4 15 43 1 15 1 -> 3 3 2 12
'''

'''
size1 = int(input("Введите размер 1-го массива -"))
print("Введите 1-ый массив:")
'''
list_1 = [3, 1, 3, 4, 2, 4, 12]
'''
[int(input()) for i in range(size1)]
print(list_1)
'''
'''
size2 = int(input("Введите размер 2-го массива - "))
print("Введите 2-ой массив:")
'''
list_2 = [4, 15, 43, 1, 15, 1]
'''
[int(input()) for i in range(size2)]
print(list_2)
'''
list_3 = [i for i in list_1 if i not in list_2]


'''
list_3 = list()
for i in list_1:
    if i not in list_2:
        list_3.append(i)
'''
print(list_3)


