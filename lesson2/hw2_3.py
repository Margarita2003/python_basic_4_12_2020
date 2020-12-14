#3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

while True:
    number = input("Введите месяц в виде числа: ")
    if number.isdigit():
        number = int(number)
        break
    else:
        print ("Ошибка ввода")

calendar = {'зима':(1, 2, 12),'весна':(3, 4, 5), 'лето':(6, 7, 8), 'осень':(9, 10, 11)}
if number > 12 or number <= 0:
    print('Неверное значение')
for key in calendar.keys():
    if number in calendar[key]:
        print(key)


while True:
    number_2 = input("Введите месяц в виде числа: ")
    if number_2.isdigit():
        number_2 = int(number_2)
        break
    else:
        print("Ошибка ввода")
calendar_2 = ('зима', 'весна', 'лето', 'осень', 'зима')
if number_2>12 or number_2 <=0:
    print('Неверное значение');
else:
    print(calendar_2[number_2//3])