'''
Задача 36:
Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента,
как, например, у операции умножения.

*Пример:*

**Ввод:** `print_operation_table(lambda x, y: x * y) ` 
**Вывод:**
1 2 3 4 5 6
2 4 6 8 10 12
3 6 9 12 15 18
4 8 12 16 20 24
5 10 15 20 25 30
6 12 18 24 30 36
'''

def f(operation, x, y, num_rows = 6, num_columns = 6):
    head_line = [f'{(x + 1):3}' for x in range(num_columns)]
    #head_line = [f'{(x + 1):4}' for x in range(num_columns)]
    print(*head_line)
    for i in range(2, num_rows + 1):        
        tmp_list = [' ',i]
        #tmp_list = ['  ',i]
        for j in range(2, num_rows + 1):
            tmp_list.append(f'{operation(j, i):3}')
            #tmp_list.append(f'{operation(j, i):4.1f}')
        print(*tmp_list)   


f(lambda x, y: x + y, 6, 6)

'''
для вывода дробного результата при lambda x, y: x / y
заменить 23, 27 и 30 строчки на 24, 28, и 31 соответственно
'''
