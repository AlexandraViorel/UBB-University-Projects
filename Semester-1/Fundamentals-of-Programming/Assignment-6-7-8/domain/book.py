class Book:
    def __init__(self, book_id, title, author):
        self._book_id = book_id
        self._title = title
        self._author = author

    @property
    def book_id(self):
        return self._book_id

    @book_id.setter
    def book_id(self, book_id):
        self._book_id = book_id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        self._author = author

    def __str__(self):
        return "Book id: " + str(self._book_id) + ", " + self._title + " by " + self._author


def generate_random_books(n=20):
    books = [{"title": "Ugly love", "author": "Colleen Hoover"},
             {"title": "Harry Potter and the Deathly Hallows", "author": "JK Rowling"},
             {"title": "The Da Vinci Code", "author": "Dan Brown"},
             {"title": "Fluturi 1", "author": "Irina Binder"},
             {"title": "Fluturi 2", "author": "Irina Binder"},
             {"title": "Fluturi 3", "author": "Irina Binder"},
             {"title": "Ion", "author": "Liviu Rebreanu"},
             {"title": "Padurea spanzuratilor", "author": "Liviu Rebreanu"},
             {"title": "It ends with us", "author": "Colleen Hoover"},
             {"title": "Verity", "author": "Colleen Hoover"},
             {"title": "Harry Potter and the Sorcerer’s Stone", "author": "JK Rowling"},
             {"title": "Harry Potter and the Chamber of Secrets", "author": "JK Rowling"},
             {"title": "Harry Potter and the Prisoner of Azkaban", "author": "JK Rowling"},
             {"title": "Harry Potter and the Goblet of Fire", "author": "JK Rowling"},
             {"title": "Harry Potter and the Order of the Phoenix", "author": "JK Rowling"},
             {"title": "Harry Potter and the Half-Blood Prince", "author": "JK Rowling"},
             {"title": "Harry Potter and the Cursed Child", "author": "JK Rowling"},
             {"title": "The Adventures of Sherlock Holmes", "author": "Arthur Conan Doyle"},
             {"title": "The Memoirs of Sherlock Holmes", "author": "Arthur Conan Doyle"},
             {"title": "The Return of Sherlock Holmes", "author": "Arthur Conan Doyle"}]
    books_data = {}
    for i in range(1, n+1):
        book_id = i
        book = books[i - 1]
        book_title = book["title"]
        book_author = book["author"]
        random_generated_book = Book(book_id, book_title, book_author)
        books_data[book_id] = random_generated_book
    return books_data
