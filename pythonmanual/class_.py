# Магические методы:
# __init__ - инициализация

# перегрузка операторов:
# __add__ - '+'
# __sub__ - '-'
# __mul__ - '*'
# __truediv__ - '/'
# __floordiv__ - '//'
# __mod__ - '%'
# __pow__ - '**'
# __and__ - '&'
# __xor__ - '^'
# __or__ - '|'
# __lt__ - '<'
# __le__ - '<='
# __eq__ - '=='
# __ne__ - '!='
# __gt__ - '>'
# __ge__ - '>='

# __len__ - len()
# __getitem__ - для индексации
# __setitem__ - для присвоения значения индексированному элементу
# __delitem__ - для удаления индексированных элементов
# __iter__ - для перебора объектов (например в цикле for)
# __contains__ - для in

class Human:  # суперкласс
    def __init__(self, name, age, cash):
        self.name = name
        self._age = age
        self.__cash = cash

    def speak(self):
        print('Hi!')

    @classmethod
    def life_off(cls, life_age):
        return cls(100 - life_age)

class Russian(Human):  # подкласс
    def speak(self):  # переопределение метода суперкласса
        print('Привет!')


test = Russian('Антон', 25, 1000)
print(test.name)
print(test._age)  # доступ к слабо приватному атрибуту
print(test._Human__cash)  # доступ к строго приватному атрибуту
test.speak()
