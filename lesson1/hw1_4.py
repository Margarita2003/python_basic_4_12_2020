# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции


while True:
    number = input ("Введите целое положительное число: ")
    if number.isdigit():
        number = int (number)
        break
    else:
        print ("Ошибка ввода")

number_max = 0
while number and number_max != 9:
    a = number % 10
    number = number // 10
    if a > number_max:
        number_max = a
print(number_max)