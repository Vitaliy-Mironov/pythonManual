# https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/bool-logicheskij-tip-dannyh/

# булевые - bool()

ex_bool1 = True
ex_bool2 = False

# 0 и пустое значение дают False
# остальные варианты дают True

x = bool(0)
print(x)  # False

x = bool('')
print(x)  # False

x = bool([])
print(x)  # False

x = bool(10)
print(x)  # True

x = bool('foo')
print(x)  # True

x = bool([0, 1, 2, 3, 4, 5, 6])
print(x)  # True

# Хорошей практикой считается использование конструкции 'if x:', а не
# if bool(x):
# if x is True:
# if x == True:
# if bool(x) == True:
