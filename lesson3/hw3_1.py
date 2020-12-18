#1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def div (*args):
    x = int(input("Введите число: "))
    y = int(input("Введите число: "))
    if y != 0:
        return x/y
    else:
        return None

print (div())

def div (*args):
    try:
        x = int(input("Введите число: "))
        y = int(input("Введите число: "))
        res = x/y
    except ZeroDivisionError:
        return ("На ноль делить нельзя")

    return res
print (div())