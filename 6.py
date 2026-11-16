# Задание 6: Сохранение списка объектов в файл

class Streamer:
    def __init__(self, nickname, subscribers, donates):
        self.nickname = nickname
        self.subscribers = subscribers
        self.donates = donates

    def to_line(self):
        donates_str = ",".join(str(d) for d in self.donates)
        return f"{self.nickname};{self.subscribers};{donates_str}"

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

streamers = [
    Streamer("CyberPro", 1500, list((100, 500, 250))),
    Streamer("AlexGame", 3200, list((1000, 200)))
]

save_to_file(streamers, "streamers.txt")
loaded_streamers = load_from_file("streamers.txt")

print("Загружено стримеров:", len(loaded_streamers))
for s in loaded_streamers:
    print(s.nickname, s.subscribers, s.donates)