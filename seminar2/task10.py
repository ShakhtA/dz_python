import random

# Проверка корректности ввода данных
while True:
    try:
        n = int(input ("Введите количество монеток - "))
        if (type(n) == int) and (n > 0):
            break
        else:
            print("Число должно быть натуральным.")
    except:
        print("Ошибка ввода!")

# Ввод данных при помощи генератора случайных чисел: 0 - орел, 1 - решка
count0 = 0
count1 = 0
for i in range(n):
    number = random.randrange(2)
    print(number, end = ' ')
    if number == 0: count0 +=1
    else: count1 += 1

# Вывод результата
print()
print('count0 =', count0)
print('count1 =', count1)
if count0 > count1:
    print(f'Необходимо перевернуть {count1} монет')
else:
    print(f'Необходимо перевернуть {count0} монет')