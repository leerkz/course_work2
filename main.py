import json

from src.hh_api import HeadHunterAPI
from src.json_saver import JSONSaver
from src.vacancy import Vacancy


def user_interaction():
    hh_api = HeadHunterAPI()
    json_saver = JSONSaver()
    print("1. Введите поисковый запрос для получения вакансий")
    print("2. Получить топ N вакансий по зарплате")
    print("3. Найти вакансии по ключевому слову")
    print("4. Выйти")

    while True:
        action = input("Выберите действие: ")
        if action == "1":
            keyword = input("Введите ключевое слово для поиска: ")
            vacancies_data = hh_api.get_vacancies(keyword)
            vacancies = Vacancy.cast_to_object_list(vacancies_data)
            for vacancy in vacancies:
                json_saver.add_vacancy(vacancy)
            print(f"Добавлено {len(vacancies)} вакансий.")

        elif action == "2":
            top_n = int(input("Введите количество вакансий для отображения: "))
            with open("vacancies.json", "r", encoding="utf8") as file:
                vacancies = sorted(json.load(file), key=lambda x: x["salary"], reverse=True)[:top_n]
                for v in vacancies:
                    print(f"{v['name']} — зарплата: {v['salary']}, ссылка: {v['link']}")

        elif action == "3":
            keyword = input("Введите ключевое слово для поиска в описании: ")
            with open("vacancies.json", "r", encoding="utf8") as file:
                vacancies = [v for v in json.load(file) if keyword.lower() in v["description"].lower()]
                for v in vacancies:
                    print(f"{v['name']} — зарплата: {v['salary']}, ссылка: {v['link']}")

        elif action == "4":
            print("Выход.")
            break


if __name__ == "__main__":
    user_interaction()
