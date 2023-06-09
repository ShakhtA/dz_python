'''
Задача 6: Вы пользуетесь общественным транспортом?
Вероятно, вы расплачивались за проезд и получали билет с номером.
Счастливым билетом называют такой билет с шестизначным номером,
где сумма первых трех цифр равна сумме последних трех.
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
Вам требуется написать программу, которая проверяет счастливость билета.

385916 -> yes
123456 -> no
'''

number = input("Введите шестизначный номер билета - ")
intNum = int(number)
sum1 = 0
sum2 = 0

for i in range(6):
    if i < 3:
        sum1 +=intNum % 10
        intNum //= 10
    else:
        sum2 +=intNum % 10
        intNum //= 10

if sum1 == sum2:
    print(number + "-> Yes")
else:
    print(number + "-> No")
    