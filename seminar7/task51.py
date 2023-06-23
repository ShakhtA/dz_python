'''
Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое значение
некоторой характеристики, и возвращают True, если это так. Если значение характеристики для разных объектов
отличается - то False. Для пустого набора объектов, функция должна возвращать True. Аргумент characteristic - это
функция, которая принимает объект и вычисляет его характеристику.
Input:
values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')
'''
values = [0, 2, 4, 7]
def same_by(characteristic, objects):
    #bool_list = list(map(characteristic, objects))
    if sum(map(characteristic, objects)) == len(objects) or sum(map(characteristic, objects)) == 0:
        return True
    else: return False


    for i in range(1, len(objects)):
        if characteristic(objects[0] == characteristic(objects[i])):
            continue
        else: return False
        
    return True 


if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')
print(sum(values))