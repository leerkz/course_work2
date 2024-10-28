class Vacancy:
    __slots__ = ["__name", "__link", "__salary", "__description"]

    def __init__(self, name, link, salary, description):
        self.__name = name
        self.__link = link
        self.__salary = salary if salary is not None else 0
        self.__description = description

    @property
    def name(self):
        return self.__name

    @property
    def link(self):
        return self.__link

    @property
    def salary(self):
        return self.__salary

    @property
    def description(self):
        return self.__description

    def __lt__(self, other: 'Vacancy') -> bool:
        return self.__salary < other.salary
