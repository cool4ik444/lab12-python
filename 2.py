# Задание 2: несколько except и finally
try:
    x = int(input("Введи число: "))
    result = 10 / x
except ValueError:
    print("Введено не число!")
except ZeroDivisionError:
    print("На ноль делить нельзя!")
else:
    print("Результат:", result)
finally:
    print("Программа завершена")