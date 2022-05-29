from classes.publications_abstract import Book, Publications


class PrintedBook(Book):
    __material = "Paper"

    def __init__(self, caption: str, is_electric: bool, genre_type: str, number_of_pages: int, material: str):
        super().__init__(caption, is_electric, genre_type, number_of_pages)
        self.__material = material

    @property
    def material(self):
        return self._material

    @material.setter
    def material(self, material: str):
        self.__material = material

    def __str__(self):
        return f'The {self._caption} is printed book, is electric {self._is_electric} ' \
               f'and has {self.number_of_pages} pages and consist of {self.__material} material'


class AudioBook(Book):
    __time_to_listen_in_hours = 2

    def __init__(self, caption: str, is_electric: bool, genre_type: str, number_of_pages: int,
                 time_to_listen_in_hours: float):
        super().__init__(caption, is_electric, genre_type, number_of_pages)
        if time_to_listen_in_hours < 0.1:
            raise ValueError("Sorry, but time to listen in hours can not be less than 10 minutes")
        self.__time_to_listen_in_hours = time_to_listen_in_hours

    @property
    def time_to_listen_in_hours(self):
        return self.__time_to_listen_in_hours

    @time_to_listen_in_hours.setter
    def time_to_listen_in_hours(self, time_to_listen_in_hours: float):
        if time_to_listen_in_hours < 0.1:
            raise ValueError("Sorry, but time to listen in hours can not be less than 10 minutes")
        self.__time_to_listen_in_hours = time_to_listen_in_hours

    def __str__(self):
        return f'The {self._caption} is audio book, is electric {self._is_electric} ' \
               f'and has {self.number_of_pages} pages and you need {self.__time_to_listen_in_hours} hours to listen it'


class ElectricBook(Book):
    __insert_memory_in_gb = 8

    def __init__(self, caption: str, is_electric: bool, genre_type: str, number_of_pages: int,
                 insert_memory_in_gb: int):
        super().__init__(caption, is_electric, genre_type, number_of_pages)
        if insert_memory_in_gb < 1:
            raise ValueError("Sorry, but the memory in gb cannot be less than 1")
        self.__insert_memory_in_gb = insert_memory_in_gb

    @property
    def insert_memory_in_gb(self):
        return self.__insert_memory_in_gb

    @insert_memory_in_gb.setter
    def insert_memory_in_gb(self, insert_memory_in_gb: int):
        if insert_memory_in_gb < 1:
            raise ValueError("Sorry, but the memory in gb cannot be less than 1")
        self.__insert_memory_in_gb = insert_memory_in_gb

    def __str__(self):
        return f'The {self._caption} is electric book and it has {self.__insert_memory_in_gb} GB memory '


class Magazine(Publications):
    __producer_edition = "Ukraine24"

    def __init__(self, caption: str, genre_type: str, producer_edition: str) -> None:
        super().__init__(caption, genre_type)
        self.__producer_edition = producer_edition

    @property
    def producer_edition(self):
        return self.__producer_edition

    @producer_edition.setter
    def producer_edition(self, producer_edition: str):
        self.__producer_edition = producer_edition

    def __str__(self):
        return f'The {self._caption} is magazine and its produces is {self.__producer_edition}'


class Monograph(Publications):
    __main_theme = "Default"

    def __init__(self, caption: str, genre_type: str, main_theme: str) -> None:
        super().__init__(caption, genre_type)
        self.__main_theme = main_theme

    @property
    def main_theme(self):
        return self.__main_theme

    @main_theme.setter
    def main_theme(self, main_theme: str):
        self.__main_theme = main_theme

    def __str__(self):
        return f'The {self._caption} is magazine and its main theme is {self.__main_theme}'
