n = 1000

def sum_del(number):
    summ = 1
    for i in range (2, number // 2 + 1):
        if number % i == 0:
            summ +=i
    return summ

for i in range(1, n):
    #print(i, sum_del(i))
    tmp = sum_del(i)
    if i == sum_del(tmp):
        print (i, tmp)
 