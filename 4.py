# Задание 4: работа с файлами — дозапись
with open("hello.txt", "a", encoding="utf-8") as f:
    f.write("Ещё одна строка\n")

with open("hello.txt", "r", encoding="utf-8") as f:
    print(f.read())