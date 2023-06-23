my_list = []
number = int(input("Введите размер массива - "))
print("Введите элеметны массива: ")
for i in range(number):
    my_list.append(int(input()))

count = 0
for i in range(1, len(my_list)-1):
    if my_list[i - 1] < my_list[i]  > my_list[i + 1]: count +=1

print (count)