# Task 215

# Как вернуть дробную часть (т.е. цифры, идущие после запятой)
# любого переданного в функцию числа?
# decimal_part(1.2) -> 0.2
# decimal_part(-3.73) -> 0.73
# decimal_part(10) -> 0

# ! Варианты res = float(n % 1) или res = float(n) - int(n) не работают.
# Они вернут 0.19999999999999996 от 1.2
print(float(1.2 % 1))
print(float(1.2) - int(1.2))

# Right decision 1:
def decimal_part(n):
    if type(n) == int:
        return 0
    return float('0.' + str(n).split('.')[-1])


print(decimal_part(1.2))
print(decimal_part(-3.73))
print(decimal_part(10))

# Right decision 2:
from decimal import Decimal


def decimal_part2(n):
    n = str(abs(n))
    return float(Decimal(n) % 1)


print(decimal_part2(1.2))
print(decimal_part2(-3.73))
print(decimal_part2(10))
