# Задание 1: деление с обработкой ошибок
try:
    a = int(input("Введи первое число: "))
    b = int(input("Введи второе число: "))
    result = a / b
    print("Результат:", result)
except ValueError:
    print("Введено не число!")
except ZeroDivisionError:
    print("На ноль делить нельзя!")
