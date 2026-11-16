# Задание 7: Полная программа (главное задание)

class Streamer:
    def __init__(self, nickname, subscribers, donates):
        self.nickname = nickname
        self.subscribers = subscribers
        self.donates = donates

    def to_line(self):
        donates_str = ",".join(str(d) for d in self.donates)
        return f"{self.nickname};{self.subscribers};{donates_str}"

    def show_card(self):
        total = sum(self.donates)
        avg = total / len(self.donates) if len(self.donates) > 0 else 0.0
        print(f"Стример: {self.nickname}")
        print(f"Подписчики: {self.subscribers}")
        print(f"Всего донатов: {total}")
        print(f"Средний донат: {avg}")
        print("-" * 25)

def streamer_from_line(line):
    nickname, subscribers, donates_str = line.strip().split(";")
    if donates_str == "":
        donates = []
    else:
        donates = [int(d) for d in donates_str.split(",")]
    return Streamer(nickname, int(subscribers), donates)

def save_to_file(objects, filename):
    with open(filename, "w", encoding="utf-8") as f:
        for obj in objects:
            f.write(obj.to_line() + "\n")

def load_from_file(filename):
    objects = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip() != "":
                    objects.append(streamer_from_line(line))
    except FileNotFoundError:
        print("Файл не найден, начинаем с пустого списка.")
    except ValueError:
        print("Ошибка в формате данных.")
    return objects

# 1. Создаём 3 объекта своего класса с разными данными
streamers = [
    Streamer("Golubkin", 1200, list((300, 350))),
    Streamer("FrostMikron", 5400, list((1000, 500, 1500))),
    Streamer("CyberPro", 850, list((100, 200)))
]

# 2. Сохраняем их в файл data.txt
save_to_file(streamers, "data.txt")

# 3. Очищаем список
streamers = []

# 4. Загружаем объекты из файла
streamers = load_from_file("data.txt")

# 5. Выводим карточки на экран
for s in streamers:
    s.show_card()