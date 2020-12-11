# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек,
# или убыток — издержки больше выручки). Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

while True:
    proceeds = input ("Введите выручку (руб.): ")
    if proceeds.isdigit():
        proceeds = int (proceeds)
        break
    else:
        print ("Ошибка ввода")

while True:
    cost = input ("Введите издержки (руб.): ")
    if cost.isdigit():
        cost = int (cost)
        break
    else:
        print ("Ошибка ввода")
result = proceeds-cost
if result > 0:
    print ("Финансовый результат - прибыль")
    while True:
        worker = input("Введите численность сотрудников ")
        if worker.isdigit():
            worker = int(worker)
            break
        else:
            print("Ошибка ввода")

    ren = proceeds/cost*100
    ren_worker = proceeds/worker
    print("Рентабельность", ren , "%" )
    print("Прибыль на одного сотрудника", ren_worker, "руб.");
elif result < 0:
    print ("Финансовый результат - убыток");
else:
    print("Результат в 'ноль'")