'''
Задача 2: Найдите сумму цифр трехзначного числа.

123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) 
'''

num = int(input("Введите трехзначное число - "))
temp = num
sum = 0

while temp >= 1:
    sum += temp % 10
    temp //= 10

print(f'Сумм цифр числа {num} -> {sum}')

