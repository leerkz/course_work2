import unittest

from src.vacancy import Vacancy


class TestVacancy(unittest.TestCase):
    def setUp(self):
        self.vacancy1 = Vacancy("Python Developer", "https://example.com/1", 100000, "Experience with Python")
        self.vacancy2 = Vacancy("Java Developer", "https://example.com/2", 150000, "Experience with Java")
        self.vacancy3 = Vacancy("C++ Developer", "https://example.com/3", None, "Experience with C++")

    def test_vacancy_creation(self):
        self.assertEqual(self.vacancy1.name, "Python Developer")
        self.assertEqual(self.vacancy1.link, "https://example.com/1")
        self.assertEqual(self.vacancy1.salary, 100000)
        self.assertEqual(self.vacancy1.description, "Experience with Python")

    def test_salary_validation(self):
        self.assertEqual(self.vacancy3.salary, 0)

    def test_comparison(self):
        self.assertTrue(self.vacancy1 < self.vacancy2)
        self.assertFalse(self.vacancy2 < self.vacancy1)


if __name__ == "__main__":
    unittest.main()
