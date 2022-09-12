# https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/brief-description/

# множество - set() - изменяемое
# содержимое может быть изменено с помощью методов set.add() и ser.remove()
ex_set1 = set()  # создание пустого множества (вид {} создает пустой СЛОВАРЬ!)
ex_set2 = {'a', 'b', 'c', 'd'}
ex_set2.add('e')  # {'c', 'a', 'e', 'd', 'b'}
ex_set2.remove('c')  # {'a', 'b', 'e', 'd'}
# При преобразовании последовательности в множество
# удаляются дубликаты элементов
lst = ['a', 'b', 'c', 'd', 'a', 'b', 'c', 'd']
ex_set3 = set(lst)  # {'a', 'b', 'c', 'd'}

# множество - frozenset() - неизменяемое
ex_fset1 = frozenset()
# Преобразование в неизменяемое множество:
lst = [0, 1, 2, 3, 4, 0, 1, 2, 3, 4]
ex_fset2 = frozenset(lst)  # frozenset({0, 1, 2, 3, 4})
