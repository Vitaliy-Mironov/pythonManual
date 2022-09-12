# https://docs-python.ru/tutorial/opredelenie-funktsij-python/anonimnye-funktsii-lambda-vyrazhenija/


# обычная функция
def func(a, b):
    return a + b


# равноценная замена
fn = lambda a, b: a + b

a = 5
b = 4
print(func(a, b))  # 9
print(fn(a, b))  # 9

# примеры использования lambda:

# 1.1 для сортировки вложенного списка
arr_list = [[1, 4], [8, 13], [5, 7]]
arr_list.sort(key=lambda x: x[1])
print(arr_list)  # [[1, 4], [5, 7], [8, 13]]

# 1.2 для сортировки словаря
d = {'a': 10, 'b': 15, 'c': 4}
list_d = list(d.items())
list_d.sort(key=lambda i: i[1])
print(list_d)  # [('c', 4), ('a', 10), ('b', 15)]

# 2. в качестве списка lambda-выражений
doit = [(lambda x, y: x + y), (lambda x, y: x - y),
        (lambda x, y: x * y), (lambda x, y: x / y)]
print(doit[0](5, 8))  # 13
print(doit[1](5, 8))  # -3
print(doit[2](5, 8))  # 40
print(doit[3](5, 8))  # 0.625
