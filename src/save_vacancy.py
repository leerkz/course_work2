import json

from src.vacancies import Vacancy


class SaveVacancy:
    def __init__(self, filename):
        self.filename = filename
        with open(filename, "w", encoding="utf8") as file:
            json.dump([], file)

    def add_vacancy(self, vacancy: 'Vacancy'):
        data_vacancy = {"name": vacancy.name}
        with open(self.filename, "r", encoding="utf8") as file:
            data = json.load(file)
        data.append(data_vacancy)
        with open(self.filename, "w", encoding="utf8") as file2:
            json.dump(data, file2, ensure_ascii=False)

    def add_vacancy(self, vacancy: 'Vacancy'):
        data_vacancy = {"name": vacancy.name}
        with open(self.filename, "r", encoding="utf8") as file:
            data = json.load(file)
        data.remove(data_vacancy)
        with open(self.filename, "w", encoding="utf8") as file2:
            json.dump(data, file2, ensure_ascii=False)


v = Vacancy("n", "url", 12354, "o")
saver = SaveVacancy("test.json")
saver.add_vacancy(v)
