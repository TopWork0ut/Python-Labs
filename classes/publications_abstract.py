from abc import ABC


class Publications(ABC):
    _caption = "Default"
    _genre_type = "Fantasy"

    def __init__(self, caption: str, genre_type: str) -> None:
        self._caption = caption
        self._genre_type = genre_type

    @property
    def caption(self):
        return self._caption

    @caption.setter
    def caption(self, caption: str):
        self._caption = caption

    @property
    def genre_type(self):
        return self._genre_type

    @genre_type.setter
    def genre_type(self, genre_type: str):
        self._genre_type = genre_type

    def __str__(self):
        return f'The {self._caption} is {self._caption} publication'


class Book(Publications):
    _is_electric = False
    _number_of_pages = 100

    def __init__(self, caption: str, is_electric: bool, genre_type: str, number_of_pages: int):
        super().__init__(caption, genre_type)
        self._is_electric = is_electric
        if number_of_pages < 1:
            raise ValueError("Sorry, but the book can not have less than 1 page")
        self._number_of_pages = number_of_pages

    @property
    def is_electric(self):
        return self._is_electric

    @is_electric.setter
    def is_electric(self, is_electric: bool):
        self._is_electric = is_electric

    @property
    def number_of_pages(self):
        return self._number_of_pages

    @number_of_pages.setter
    def number_of_pages(self, number_of_pages: int):
        if number_of_pages < 1:
            raise ValueError("Sorry, but the book can not have less than 1 page")
        self._number_of_pages = number_of_pages

    def __str__(self):
        return f'The {self._caption} is {self._caption} book, is electric {self._is_electric} ' \
               f'and has {self.number_of_pages} pages'

