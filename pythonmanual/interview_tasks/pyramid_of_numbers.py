# Вывести пирамиду из целых чисел

def pyramid(number):
    for i in range(1, number + 1):
        space = ' ' * (number - i)
        nums = str(i) * (i * 2 - 1)
        print(space + nums)


pyramid(6)

#      1
#     222
#    33333
#   4444444
#  555555555
# 66666666666
