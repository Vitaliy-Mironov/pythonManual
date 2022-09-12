# https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/opredelit-tip-peremennoj-obekta/

# Для сравнения типов переменных/объектов со встроенными типами Python
# лучше всего использовать функцию isinstance()

class MyList(list):
    pass


lst = MyList('test')
print(lst)  # ['t', 'e', 's', 't']

if isinstance(lst, list):
    print('Это список')
else:
    print('Это НЕ список')


# Встроенный класс type() лучше использовать для прямого сравнения типа
# (идентичности) экземпляра объекта

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height


class Circle:
    def __init__(self, radius):
        self.radius = radius


c = Circle(2)
r = Rectangle(3, 4)

if type(r) is type(c):
    print("Типы объектов совпадают")
else:
    print("Типы объектов не совпадают")
