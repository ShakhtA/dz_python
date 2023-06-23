'''
Напишите такое лямбда-выражение transformation,
чтобы transformed_values получилсякопией values.

Input:
    values = [1, 2]
    transformed_values = list(map(transformation, values))
    if values == transformid_values:
        print("OK")
    else:
        print('fail')

Output: OK
'''
values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
transformed_value = list(map(lambda x: x, values))

if values == transformed_value:
    print('Ok')
else:
    print('fail')
