# re - библиотека для работы с регулярными выражениями
import re

pattern = r'spam'
string = 'eggspamspamspam'

# функция .match() ищет совпадение В НАЧАЛЕ строки
print('\nПример работы .match():')
if re.match(pattern, string):
    print('Match')
else:
    print('No match')

# функция .search() ищет совпадение В ЛЮБОМ МЕСТЕ строки
print('\nПример работы .search():')
if re.search(pattern, string):
    print('Match')
else:
    print('No match')

# функция .findall() возвращает список всех подстрок, которые совпадают
# с искомым набором символов
print('\nПример работы .findall():')
print(re.findall(pattern, string))

# функция .finditer() делает то же самое, что и .findall()
# за исключением того, что она возвращает итератор, а не список
print('\nПример работы .finditer():')
print(re.finditer(pattern, string))

# Простые метасимволы:
# '.' - любой символ, исключая символ новой строки
pattern = r"gr.y"  # обработает и gray и grey
# '^' - начало строки
# '$' - конец строки
pattern = r"^gr.y$"
# '*' - ноль или более упоминаний объекта поиска (т.е. того,
#       что указан в () или [] перед этим символом
# '+' - одно или более упоминаний объекта поиска
# '?' - ноль или одно упоминание объекта поиска
# '|' - или
pattern = r"^gr(a|e)y$"
# {} - для указания числа упоминаний:
# {3} - строго указанное число упоминаний
# {2,12} - кол-во упоминаний от указанного в первом числе
#          до указанного во втором числе ({0,1} == '?')
# {,8} - если первое число пропущено, то поиск от 0
# {5,} - если второе число пропущено, то поиск до бесконечности

# Классы метасимволов:
# для поисков конкретного символа или набора символов, указывается в []
# [0-9] - любая цифра
pattern = r"[1-5][0-9]"  # любое двузначное число от 10 до 59
# [a-z] - любая латинская строчная буква
# [A-Z] - любая латинская заглавная буква
# [а-яё] - любая русская строчная буква
# [А-ЯЁ] - любая русская заглавная буква
# '^' - в начале класса (после '[') инвертирует класс,
#       например [^aeiou] - любая не прописная гласная буква лат.алфавита

# Группы:
# Группы создаются путём заключения части регулярного выражения в ()
# Группа может быть задана в качестве аргумента метасимволам '*', '+', '?'
pattern = r"egg(spam)*"
# функция .group() - для получения содержания групп
# .group() == .group(0) - все совпадения
# .group(n), где n>0, вернёт n-ю группу, считая слева
# .groups() возвращает все группы, начиная с первой
pattern = r"a(bc)(de)(f(g)h)i"
test = re.search(pattern, "abcdefghijklmnop")
if test:
    print('\nПример работы .group():')
    print(test.group())  # abcdefghi
    print(test.group(0))  # abcdefghi
    print(test.group(1))  # bc
    print(test.group(4))  # g
    print(test.groups())  # ('bc', 'de', 'fgh', 'g')

# Именованные группы:
# (?P<name>content)
# Их можно получить как по номеру, так и с помощью метода group(name)
# "Незахватывающие" группы:
# (?:content)
# Их нельзя получить по методу группы, по этому их можно добавлять
# в регулярное выражение не нарушая нумерацию
pattern = r"(?P<first>abc)(?:def)(ghi)"
test = re.search(pattern, "abcdefghi")
if test:
    print('\nПример работы именованных и незахватывающих групп:')
    print(test.group("first"))  # abc
    print(test.groups())  # ('abc', 'ghi')

# Специальные последовательности:
# \1 - число от 1 до 99 - такая последовательность соответствует
#                         выражению группы с таким же числом
print('\nПример работы специальной последовательности \\1:')

pattern = r"(.*) \1"

test = re.match(pattern, "word word")
if test:
    print("Match 1")  # Match 1

test = re.match(pattern, "?! ?!")
if test:
    print("Match 2")  # Match 2

test = re.match(pattern, "abc cde")  # .match()
if test:
    print("Match 3")  # нет вывода

test = re.search(pattern, "abc cde")  # .search()
if test:
    print("Match 4")  # Match 4

# \d - цифра (от лат. digit)
# \D - любой символ, кроме цифр
# \s - пробел (от лат. space)
# \S - любой символ, кроме пробела
# \w - символы слов (от лат. word characters).
#      В режиме ASCII им соответствуют [0-9], [\t\n\r\f\v], [a-zA-Z0-9_]
# \W - противоположное \w
# \A - начало строки
# \Z - конец строки
# \b - "словораздел" - пустая строка между символами \w и \W,
#      или символами \w и началом или концом строки
# \B - пустая строка в любом другом месте

print("\nПример для поиска хештегов:")
pattern = r"[#]\S+"
result = re.findall(pattern, "#Coding is #awesome !!!")
for i in result:
    print(i)

print("\nПример для поиска e-mail адресов:")
pattern = r"([\w\.\-_]+)@([\w\.\-_]+)(\.[\w\.]+)"
result = re.search(pattern, "Contact 4mironov@gmail.com for more info")
if result:
    print(result.group())

print("\nПример 2 для поиска e-mail адресов (с именованием группы):")
pattern = r"(?P<email>(([\w\.\-_]+)@([\w\.\-_]+)(\.[\w\.]+)))"
result = re.search(pattern, "Contact 4mironov@gmail.com for more info")
if result:
    print(result.group('email'))
