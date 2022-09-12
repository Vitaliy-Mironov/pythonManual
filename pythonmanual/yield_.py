# такая конструкция позволяет обрабатывать данные постепенно
# (например подгружать данные на сайт)
# и не загружать память сразу всем объёмом данных

# yield как return возвращает данные
# следующая итерация вызывается функцией next()
def test():
    for i in range(3):
        yield i


a = test()
print(next(a))  # 0
print(next(a))  # 1
print(next(a))  # 2
# print(next(a))  # exception StopIteration


for i in test():
    print(i)
# 0
# 1
# 2

print('-')


def test2():
    yield from [1, 4, 9]


for i in test2():
    print(i)
# 1
# 4
# 9
print('--')


def test2a():
    yield from [x for x in range(5)]


for i in test2a():
    print(i)
# 0
# 1
# 2
# 3
# 4

print('---')


# в функции может быть сколько угодно yield
# через next() они будут вызываться по очереди
def test3():
    print('started')
    while True:
        yield 1
        yield 2


a = test3()
print(next(a))  # started /n 1
print(next(a))  # 2
print(next(a))  # 1
print(next(a))  # 2
print(next(a))  # 1
# и так далее...


print('----')


# также yield использует метод .send()
def test4():
    print('started')
    while True:
        x = yield
        print('recv:', x)


a = test4()
next(a)  # started
# только попав в yield можно вызывать метод .send(), иначе будет ошибка
next(a)  # recv: None
a.send('test')  # recv: test
