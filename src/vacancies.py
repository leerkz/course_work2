class Vacancy:
    __slots__ = ['__name', '__link', '__salary', '__describe']

    def __init__(self, name, link, salary: float, describe):
        self.__name = name
        self.__link = link
        self.__salary = salary
        self.__describe = describe
        self.__validation()

    def __lt__(self, other: 'Vacancy'):
        return self.__salary < other.salary

    def __le__(self, other):
        return self.__salary <= other.salary

    def __validation(self):
        if self.__salary is None:
            self.__salary = 0.0

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
    def describe(self):
        return self.__describe
