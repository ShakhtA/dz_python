
'''
Задача 26
Напишите программу, которая на вход принимает два числа A и B,
и возводит число А в целую степень B с помощью рекурсии.

Пример:

A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8 
'''

a = int(input('Введите основание степени - '))
b = int(input('Введите показатель степени - '))

def pow(a, b):
    if b == 0: return 1
    if b > 0:
        if b == 1:
            return a
        else:
            return a * pow(a, b - 1)
    else:
        if b == -1:
            return 1/a
        else:
            return 1/a * pow(a, b + 1)
        
print(f'A = {a}; B = {b} -> {pow(a, b)}')