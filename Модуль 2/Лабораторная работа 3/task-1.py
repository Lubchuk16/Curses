class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Название книги должно быть непустой строкой")
        self._name = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Автор книги должен быть непустой строкой")
        self._author = value


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = pages

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = value


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Длительность должна быть положительным числом")
        self._duration = float(value)


if __name__ == "__main__":
    print("Test")
    print()

    print("Class Book")
    book = Book('Правление волков', 'Ли Бардуго')
    print(book)
    print(book.__repr__())
    print()

    print("Class PaperBook")
    book = PaperBook('Правление волков', 'Ли Бардуго', 663)
    print(book)
    print(book.__repr__())
    print()

    print("Class AudioBook")
    book = AudioBook('Правление волков', 'Ли Бардуго', 317.6)
    print(book)
    print(book.__repr__())

