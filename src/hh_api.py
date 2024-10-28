import requests

from src.abstract_api import JobAPI


class HeadHunterAPI(JobAPI):
    def __init__(self):
        self._url = "https://api.hh.ru/vacancies"
        self._headers = {"User-Agent": "HH-User-Agent"}

    def connect_to_api(self):
        response = requests.get(self._url, headers=self._headers)
        if response.status_code != 200:
            raise ConnectionError("Не удалось подключиться к API hh.ru")

    def get_vacancies(self, keyword: str):
        params = {"text": keyword, "page": 0, "per_page": 100}
        self.connect_to_api()
        vacancies = []
        while params["page"] < 2:
            response = requests.get(self._url, headers=self._headers, params=params)
            if response.status_code != 200:
                break
            items = response.json().get("items", [])
            vacancies.extend(items)
            params["page"] += 1
        return vacancies
