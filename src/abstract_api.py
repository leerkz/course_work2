from abc import ABC, abstractmethod
from typing import Dict, List


class JobAPI(ABC):
    @abstractmethod
    def connect_to_api(self):
        """Подключение к API и проверка успешности соединения"""
        pass

    @abstractmethod
    def get_vacancies(self, keyword: str) -> List[Dict]:
        """Получение вакансий по ключевому слову"""
        pass
