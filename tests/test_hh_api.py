import unittest

from src.hh_api import HeadHunterAPI


class TestHeadHunterAPI(unittest.TestCase):
    def setUp(self):
        self.api = HeadHunterAPI()

    def test_connect_to_api_success(self):
        try:
            self.api.connect_to_api()
        except Exception as e:
            self.fail(f"Connection to API failed with exception: {e}")

    def test_get_vacancies(self):
        vacancies = self.api.get_vacancies("Python")
        self.assertIsInstance(vacancies, list)
        self.assertGreater(len(vacancies), 0)
        self.assertIn("name", vacancies[0])


if __name__ == "__main__":
    unittest.main()
