import json
from src.vacancy import Vacancy
from src.vacancy_storage_abstract import VacancyStorageAbstract


class JSONSaver(VacancyStorageAbstract):
    def __init__(self, filename="vacancies.json"):
        self._filename = filename
        with open(self._filename, "w", encoding="utf8") as file:
            json.dump([], file)

    def add_vacancy(self, vacancy: Vacancy):
        with open(self._filename, "r+", encoding="utf8") as file:
            data = json.load(file)
            if any(v["name"] == vacancy.name for v in data):
                print(f"Вакансия {vacancy.name} уже существует.")
                return
            data.append(
                {
                    "name": vacancy.name,
                    "link": vacancy.link,
                    "salary": vacancy.salary,
                    "description": vacancy.description,
                }
            )
            file.seek(0)
            json.dump(data, file, ensure_ascii=False, indent=4)

    def delete_vacancy(self, vacancy: Vacancy):
        with open(self._filename, "r+", encoding="utf8") as file:
            data = json.load(file)
            data = [v for v in data if v["name"] != vacancy.name]
            file.seek(0)
            file.truncate()
            json.dump(data, file, ensure_ascii=False, indent=4)
