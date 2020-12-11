# 3. Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

while True:
    number = input("Введите целое положительное число: ")
    if number.isdigit():
        number = int(number)
        break
    else:
        print("Ошибка ввода")

total = f"{number}{int(number)*2}{int(number)*3}"
print(total)