# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

while True:
    number = input ("Введите целое положительное число: ")
    if number.isdigit():
        number = int (number)
        break
    else:
        print ("Ошибка ввода")

hours = number // 3600
ostatok = number % 3600
minutes = ostatok // 60
seconds = ostatok % 60
time = "{:02}час.:{:02}мин.:{:02}сек.".format (hours,minutes,seconds)
print("Время", time)