import json
import os
import unittest

from src.json_saver import JSONSaver
from src.vacancy import Vacancy


class TestJSONSaver(unittest.TestCase):
    def setUp(self):
        self.saver = JSONSaver("test_vacancies.json")
        self.vacancy1 = Vacancy("Python Developer", "https://example.com/1", 100000, "Experience with Python")
        self.vacancy2 = Vacancy("Java Developer", "https://example.com/2", 150000, "Experience with Java")
        # Очистка файла перед каждым тестом
        with open(self.saver._filename, "w", encoding="utf8") as file:
            json.dump([], file)

    def test_add_vacancy(self):
        self.saver.add_vacancy(self.vacancy1)
        with open(self.saver._filename, "r", encoding="utf8") as file:
            data = json.load(file)
            self.assertEqual(len(data), 1)
            self.assertEqual(data[0]["name"], "Python Developer")

    def test_prevent_duplicate_vacancies(self):
        self.saver.add_vacancy(self.vacancy1)
        self.saver.add_vacancy(self.vacancy1)
        with open(self.saver._filename, "r", encoding="utf8") as file:
            data = json.load(file)
            self.assertEqual(len(data), 1)  # Проверка на отсутствие дублирования

    def test_delete_vacancy(self):
        self.saver.add_vacancy(self.vacancy1)
        self.saver.delete_vacancy(self.vacancy1)
        with open(self.saver._filename, "r", encoding="utf8") as file:
            data = json.load(file)
            self.assertEqual(len(data), 0)

    def tearDown(self):
        os.remove(self.saver._filename)  # Удаление файла после теста


if __name__ == "__main__":
    unittest.main()
