# https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-str-tekstovye-stroki/

# строки - str() - НЕизменяемые последовательности Юникода

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

# Тип str - текстовые строки можно создать посредством:
#           класса str()
#           одинарных кавычек ''
#           двойных кавычек ""трёх одинарных кавычек ''' '''
#           трёх двойных кавычек """ """
# Текстовые строки в тройных кавычках могут занимать несколько строк -
# все связанные пробелы будут включены в итоговую строку.
ex_str = str()
ex_str1 = 'Привет мир!'
ex_str2 = "Привет мир!"
ex_str3 = '''Привет мир!'''
ex_str4 = """Привет
мир!"""
print(ex_str4)

# обрезка последнего символа:
print(ex_str3[:-1])  # 'Привет мир'
# обрезка первого символа:
print(ex_str3[1:])  # 'ривет мир!'

# Строки, которые являются частью одного выражения и имеют только
# пробелы между собой, будут неявно преобразованы в одну строку.
str = ("hello" "world")
print(str)  # 'helloworld'
# Эту функцию можно использовать для уменьшения необходимого
# количества обратных слэшей при форматировании строки.

# Функция str.format() /!\ Функцию format() см. в файле format_.py /!\
# https://docs-python.ru/tutorial/operatsii-tekstovymi-strokami-str-python/metod-str-format/

# Синтаксис:
# str.format(*args, **kwargs)

# Параметры:
# *args - позиционные аргументы
# **kwargs - ключевые аргументы

# Возвращаемое значение:
# str, копия форматированной строки

# Строки str метода str.format() содержат "замещающие поля",
# заключенные в фигурные скобки {}. Все, что не содержится в фигурных скобках,
# считается буквальным текстом, который копируется без изменений
# в выходные данные. Каждое замещающее поле {} содержит либо числовой индекс
# позиционного аргумента, либо имя ключевого аргумента.

# {" [ field_name] [ "!" conversion] [ ":" format_spec] "}
# - field_name - это *args и(или) **kwargs
# - conversion - это 'r' или 's' или 'a'
# - format_spec - это Спецификация формата Mini-Language

# Поле замены {...} может начинаться с field_name, указывающего объект,
# значение которого должно быть отформатировано и вставлено в выходные данные.
# За полем field_name, необязательно должны следовать поля:
# conversion, которому предшествует восклицательный знак '!',
# и format_spec, которому предшествует двоеточие ':'.
# Они задают формат замены, отличный от формата по умолчанию.

# Поле field_name

# Оно является либо числом, либо ключевым словом.
# Если это число, то оно ссылается на позиционный аргумент,
# а если ключевое слово, то на именованный аргумент ключевого слова.

a = 'something'
b = 'anything'
# ПОЗИЦИОННЫЕ АРГУМЕНТЫ
print('text {0} text {1} text'.format(a, b))
# числа позиционных аргументов можно не указывать, если они следуют подряд
print('text {} text {} text'.format(a, b))
# числа позиционных аргументов нужно указывать, если они следуют не по порядку
print('text {1} text {0} text {1}'.format(a, b))
# КЛЮЧЕВЫЕ АРГУМЕНТЫ
# имена ключевых аргументов указываются всегда
print('text {one} text {two} text {two}'.format(one=a, two=b))

# Поле conversion

# Поле conversion вызывает приведение типа перед форматированием.
# Обычно задание форматирования значения выполняется методом __format__()
# самого значения. Однако в некоторых случаях желательно
# принудительно форматировать тип в виде строки, переопределяя
# его собственное определение форматирования.
# При преобразовании значения в строку перед вызовом __format__()
# обычная логика форматирования игнорируется.

# Поддерживаются три флага преобразования:
# '!s' - вызывает str() по значению
# '!r' - вызывает repr()
# '!a' - вызывает ascii()

# Поле format_spec

# Содержит спецификацию формата "Mini-Language" (см. файл format_.py),
# т.е. определяет, как должно быть представлено значение, включая такие детали,
# как ширина поля, выравнивание, заполнение, десятичная точность и так далее.

# Примеры:

print('{0}, {1}, {2}'.format('a', 'b', 'c'))  # 'a, b, c'
print('{}, {}, {}'.format('a', 'b', 'c'))  # 'a, b, c'
print('{2}, {1}, {0}'.format('a', 'b', 'c'))  # 'c, b, a'
# распаковка позиционных аргументов
print('{2}, {1}, {0}'.format(*'abc'))  # 'c, b, a'
# индексы аргументов могут повторятся
print('{0}{1}{0}'.format('abra', 'cad'))  # 'abracadabra'
# использование строки, как шаблона
tpl = '{0}{1}{0}'
print(tpl.format('abra', 'cad'))  # 'abracadabra'

# Вывод значений, заданных ключевыми аргументами:
print('Coordinates: {latitude}, {longitude}'
      .format(latitude='37.24N', longitude='-115.81W'))
# 'Coordinates: 37.24N, -115.81W'

# распаковка ключевых аргументов
coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
print('Coordinates: {latitude}, {longitude}'.format(**coord))
# 'Coordinates: 37.24N, -115.81W'

# Доступ к атрибутам аргументов:
c = (3 - 5j)
print(('The complex number {0} is formed from the real part {0.real}'
       'and the imaginary part {0.imag}.').format(c))
# 'The complex number (3-5j) is formed from the real part 3.0 and the imaginary part -5.0.'

# Доступ к элементам аргументов:
coord = (3, 5)
print('X: {0[0]};  Y: {0[1]}'.format(coord))  # 'X: 3;  Y: 5'

# Использование фигурных скобок в строке/шаблоне:
print("Строка №{0} с {{{1}-мя фигурными скобками}}".format(1, 2))
# 'Строка №1 с {2-мя фигурными скобками}'

# Приведение типа перед форматированием на примере !r и !s:
print(
    "repr() shows quotes: {!r}, str() doesn't: {!s}".format('test1', 'test2'))
# "repr() shows quotes: 'test1', str() doesn't: test2"

# Выравнивание текста и указание ширины при помощи разметки Mini-Language:
print('{:<20}'.format('left'))       # 'left                '
print('{:>20}'.format('right'))      # '               right'
print('{:^20}'.format('centered'))   # '      centered      '
# используем '.' как символ-заполнитель
print('{:.^20}'.format('centered'))  # '......centered......'

# Форматируем число со знаком:
print('{:+f}; {:+f}'.format(3.14, -3.14))  # '+3.140000; -3.140000'
# покажем пробел для положительных чисел
print('{: f}; {: f}'.format(3.14, -3.14))  # ' 3.140000; -3.140000'
# покажем только минус - то же, что и '{: f}; {: f}'
print('{:-f}; {:-f}'.format(3.14, -3.14))  # '3.140000; -3.140000'

# Замена %x и %o и преобразование значения в разные счисления:
print("int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42))
# 'int: 42;  hex: 2a;  oct: 52;  bin: 101010'
# теперь с префиксами 0x, 0o или 0b:
print("int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(42))
# 'int: 42;  hex: 0x2a;  oct: 0o52;  bin: 0b101010'

# Использование запятой в качестве разделителя тысяч:
print('{:,}'.format(1234567890))  # '1,234,567,890'

# Выводим процент:
points = 19
total = 22
print('{:.2%}'.format(points / total))  # '86.36%'

# Использование форматирования, зависящего от типа передаваемых данных:
import datetime

d = datetime.datetime(2021, 7, 3, 11, 13, 13)
print('{:%Y-%m-%d %H:%M:%S}'.format(d))  # '2021-07-03 11:13:13'
