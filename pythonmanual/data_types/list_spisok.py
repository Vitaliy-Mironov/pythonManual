# https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-list-spisok/

# списки - list() - изменяемый тип последовательности

# Поддерживают общие операции с последовательностями:
# 'x in sequences' - проверка существования значения в последовательности
# 'sequence1 + sequence2' - конкатенация (сложение) последовательностей
# 'sequence * n' - увеличение последовательности в N раз
# 'sequence[i]' - получение значения элемента по индексу
# 'sequence[i:j]' - получение среза
# 'sequence[i:j:k]' - получение среза с заданным шагом
# 'len(sequence)' - вычисление длины последовательности
# 'min(sequence)' / 'max(sequence)' - наименьшее / наибольшее значение
# 'sequence.index(x)' - метод последовательности index() - позволяет узнать
#                       индекс первого вхождения элемента x
#                       в последовательность sequence.
#                       Вызывает ValueError, когда элемент x не найден.
# 'sequence.count(x)' - метод последовательности count() - позволяет узнать
#                       сколько раз указанный элемент появился
#                       в последовательности sequence.

# создание пустого списка
ex_list = []

# создание непустого списка
ex_list1 = ['Hello', 'World']

# list.append(х) - добавление элемента в конец списка
ex_list1.append("!")

# list.extend(iterable) - расширение списка, добавлением всех элементов из
#                         последовательности которая поддерживает итерацию
ex_list.extend(range(5))
print(ex_list)  # [0, 1, 2, 3, 4]

# list.insert(i, x) - добавление элемента по индексу
ex_list1.insert(1, 'old')
print(ex_list1)  # ['Hello', 'old', 'World', '!']

# замена элемента по индексу
ex_list1[1] = 'new'
print(ex_list1)  # ['Hello', 'new', 'World', '!']

# list.remove(x) - удаление из списка первого элемента, равноно 'x'
#                  Поднимает ValueError, если такого элемента нет
ex_list1.remove('World')
print(ex_list1)  # ['Hello', 'new', '!']

# list.pop(i) - возвращает элемент в указанной позиции
#               и удаляет этот элемент из списка.
#               Если индекс не указан list.pop(), то удаляет
#               и возвращает последний элемент из списка.
print(ex_list1.pop(1))  # new
print(ex_list1)  # ['Hello', '!']

# list.clear() - удаляет все элементы из списка
ex_list1.clear()
print(ex_list1)  # []

# list.reverse() - меняет местами элементы списка, переворачивает список
ex_list2 = [1,2,3,4,5]
ex_list2.reverse()
print(ex_list2)  # [5, 4, 3, 2, 1]

# list.copy() - возвращает мелкую копию списка, эквивалент list[:]
list1 = [1,2,3,4,5]
list2 = list1.copy()
list2[2] = 100
print(list1)  # [1, 2, 3, 4, 5]
print(list2)  # [1, 2, 100, 4, 5]
# отличие copy() от присваивания:
list_old = [11, 22, 33, 44, 55]
list_new = list_old  # при присваивании создаётся ССЫЛКА, а не копия
print(list_old)  # [11, 22, 33, 44, 55]
list_new[2] = 100
print(list_old)  # [11, 22, 100, 44, 55]
print(list_new)  # [11, 22, 100, 44, 55]

# list.sort(key=None, reverse=False) - сортировка элементов списка на месте
a = [4, 8, 3, 0, 3, 15, 6]
a.sort()  # [0, 3, 3, 4, 6, 8, 15]
# обратная сортировка
a.sort(reverse=True)  # [15, 8, 6, 4, 3, 3, 0]
# сортировка по длине строки
b = ['a', 'dddd', 'сс', 'bbb']
b.sort(key=len)  # ['a', 'сс', 'bbb', 'dddd']
# обычная (лексикографическая) сортировка чисел в качестве строк
с = ['55', '11', '25', '15', '9']
с.sort()  # ['11', '15', '25', '55', '9']
# применив в качестве ключевой функции для сравнения класс int()
# для преобразования строк в целые числа, получаем упорядоченную
# последовательность строк, как будто это список чисел.
с1 = ['55', '11', '25', '15', '9']
с1.sort(key=int)  # ['9', '11', '15', '25', '55']

# Преобразование строки str в список тип list:
list('Mironov')  # ['M', 'i', 'r', 'o', 'n', 'o', 'v']