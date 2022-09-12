# https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-dict-slovar/

# словари - dict() - изменяемый контейнерный объект

# Синтаксис:
# dict = {key: value, key: value, key: value, ...}

ex_dict = {
    "John": 25,
    "Ann": 20,
    "Anton": 3
}
print("Anton" in ex_dict)  # True
print("Anton" not in ex_dict)  # False
print(ex_dict.get("John"))  # 25
print(ex_dict.get("Jesus"))  # None
print(ex_dict.get("Jesus", 2000))  # 2000
print(ex_dict.get("Jesus", "Not found"))  # Not found
print(ex_dict.get("Ann", "Not found"))  # 20
list(reversed(ex_dict))  # ['Anton', 'Ann', 'John']
list(reversed(ex_dict.values()))  # [3, 20, 25]
list(reversed(ex_dict.items()))  # [('Anton', 3), ('Ann', 20), ('John', 25)]

