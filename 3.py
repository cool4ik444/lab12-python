# Задание 3: запись и чтение файла
with open("hello.txt", "w", encoding="utf-8") as f:
    f.write("Привет\n")
    f.write("Как дела?\n")
    f.write("Пока\n")

with open("hello.txt", "r", encoding="utf-8") as f:
    lines = f.read().split("\n")

print(lines) # все строки списком
real_lines = [x for x in lines if x != ""]
print("Строк в файле:", len(real_lines))