'''
Задача 30:
Заполните массив элементами арифметической прогрессии.
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
'''

first_number = int(input("Введите первый элемент прогрессии - "))
diff = int(input("Введите разность прогрессии - "))
count = int(input("Введите количество элементов прогрессии - "))

progr_list = [first_number]
for i in range(1, count):
    res = first_number + i * diff
    progr_list.append(res)

print(* progr_list)