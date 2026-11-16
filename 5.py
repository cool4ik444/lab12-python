# Задание 5: Класс + сохранение в файл (Вариант «Стример»)
class Streamer:
    def __init__(self, nickname, subscribers, donates):
        self.nickname = nickname
        self.subscribers = subscribers
        self.donates = donates  # список чисел

    def to_line(self):
        # донаты сохраняем через запятую внутри одного поля
        donates_str = ",".join(str(d) for d in self.donates)
        return f"{self.nickname};{self.subscribers};{donates_str}"

def streamer_from_line(line):
    nickname, subscribers, donates_str = line.strip().split(";")
    if donates_str == "":
        donates = []
    else:
        donates = [int(d) for d in donates_str.split(",")]
    return Streamer(nickname, int(subscribers), donates)

# Проверка («круговой тест»)
s1 = Streamer("CyberPro", 1500, [100, 500, 250])
line = s1.to_line()
print("Строка для файла:", line)

s2 = streamer_from_line(line)
print("Совпадают ли атрибуты:", s1.nickname == s2.nickname and s1.subscribers == s2.subscribers and s1.donates == s2.donates)