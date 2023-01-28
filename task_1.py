class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        """
        Инициализация экземпляра класса
        :param name: название книги
        :param author: автор книги
        """
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        """
        Инициализация экземпляра класса
        :param name: название книги
        :param author: автор книги
        :param pages: кол-во страниц
        """
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, pages: int) -> None:
        if not isinstance(pages, int):
            raise TypeError
        if pages < 0:
            raise ValueError
        self._pages = pages

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Количество страниц {self.pages}."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        """
        Инициализация экземпляра класса
        :param name: название книги
        :param author: автор книги
        :param duration: продолжительность в минутах
        """
        super().__init__(name, author)
        self.duration = duration

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Продолжительность {self.duration} минут."

    @property
    def duration(self) -> int:
        return self._duration

    @duration.setter
    def duration(self, duration: int) -> None:
        if not isinstance(duration, int):
            raise TypeError
        if duration < 0:
            raise ValueError
        self._duration = duration


print(PaperBook("Tot", "Kooll", 234))
print(AudioBook("Tot", "Kooll", 234))