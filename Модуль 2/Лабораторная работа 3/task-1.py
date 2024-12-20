class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)

        self.pages = pages

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"

    @property
    def check(self):
        return self.pages

    @check.setter
    def check(self, pages):
        if not isinstance(pages, int) or pages <= 0:
            raise ValueError
        self.pages = pages


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)

        self.duration = duration

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"

    @property
    def check(self):
        return self.duration

    @check.setter
    def check(self, duration):
        if not isinstance(duration, float) or duration <= 0:
            raise ValueError
        self.duration = duration


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
