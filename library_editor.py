"""
Данная программа представляет собой библиотеку для хранения книг и управления библиотекой.
Книга содержит:
1. Уникальный ID для каждой книги.
2. Название книги
3. Имя автора
4. Год публикации

Функционал приложения:
1. Добавление книги.
2. Удаление книги по ID.
3. Показ всей библиотеки.
4. Поиск книги по: Названию, Автору, Году.
5. Изменение статуса книги.
"""
from datetime import datetime


class Book:
    """Этот класс отвечает за объявление книги"""
    def __init__(self, book_id: int, title: str, author: str, year: int, status: str = "в наличии"):
        self.id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def to_line(self):
        """Преобразует данные книги в строку для хранения в текстовом файле"""
        return f"{self.id}|{self.title}|{self.author}|{self.year}|{self.status}"

    @staticmethod
    def from_line(line: str):
        """Создает объект книги состоящий из строки"""
        part = line.strip("").split("|")
        return Book(int(part[0]), part[1], part[2], int(part[3]), part[4])


class Library:
    """Этот класс отвечает за управление библиотекой"""
    def __init__(self, data_file: str = "library_data.txt"):
        self.data_file = data_file
        self.books = self.load_books()

    def load_books(self):
        """Загружает книги из текстового файла"""
        books = []
        try:
            with open(self.data_file, "r", encoding="utf-8") as file:
                books = [Book.from_line(line) for line in file if line.strip()]
        except FileNotFoundError:
            print("Файл с данными не найден 🤷‍♂️. Будет создан новый файл при добавлении книг.")
        except Exception as e:
            print(f"Ошибка загрузки данных: {e}")
        return books

    def save_books(self, append: bool = False, new_book: Book = None):
        """Сохраняет книги в файл"""
        if append and new_book:
            with open(self.data_file, "a", encoding="utf-8") as file:
                file.write(new_book.to_line() + "\n")
        else:
            with open(self.data_file, "w", encoding="utf-8") as file:
                for book in self.books:
                    file.write(book.to_line() + "\n")

    def add_book(self):
        """Добавляет новую книгу с проверкой ввода данных"""
        title = input("Введите название книги: ").strip()
        if not title:
            print("Название книги не может быть пустым!")
            return
        author = input("Введите автора книги: ").strip()
        if not author:
            print("Автор книги не может быть пустым!")
            return
        try:
            year = int(input("Введите год издания книги: ").strip())
            if year < 0 or year > datetime.now().year:
                print("Год издания не может быть отрицательным или превышать текущий год!")
                return
        except ValueError:
            print("Год издания должен быть числом!")
            return

        new_id = max((book.id for book in self.books), default=0) + 1
        new_book = Book(new_id, title, author, year)
        self.books.append(new_book)
        self.save_books()
        self.save_books(append=True, new_book=new_book)
        print(f"Книга '{title}' добавлена с ID {new_id}.")

    def find_book_by_id(self, book_id: int):
        """Находит книгу по ID."""
        for book in self.books:
            if book.id == book_id:
                return book
        return None

    def search_books(self):
        """Ищет книги по заданным критериям."""
        print("Поиск по:\n1. Названию\n2. Автору\n3. Году")
        search_choice = input("Выберите критерий поиска: ").strip()
        results = []

        if search_choice == "1":
            title = input("Введите название: ").strip()
            results = [book for book in self.books if title.lower() in book.title.lower()]
        elif search_choice == "2":
            author = input("Введите автора: ").strip()
            results = [book for book in self.books if author.lower() in book.author.lower()]
        elif search_choice == "3":
            try:
                year = int(input("Введите год: ").strip())
                results = [book for book in self.books if book.year == year]
            except ValueError:
                print("Год должен быть числом!")
                return
        else:
            print("Некорректный выбор!")
            return

        if results:
            self.display_books(results)
        else:
            print("Книги не найдены.")

    def display_books(self, books=None):
        """Отображает список всех книг."""
        books = books or self.books
        if not books:
            print("Библиотека пуста.")
        else:
            print(f"{'ID'} {'Название'} {'Автор'} {'Год'} {'Статус'}")
            print("-" * 100)
            for book in books:
                print(f"{book.id} {book.title} {book.author} {book.year} {book.status}")

    def change_status(self):
        """Изменяет статус книги."""
        try:
            book_id = int(input("Введите ID книги: ").strip())
            book = self.find_book_by_id(book_id)
            if book:
                new_status = input("Введите новый статус ('в наличии' или 'выдана'): ").strip()
                if new_status in ["в наличии", "выдана"]:
                    book.status = new_status
                    self.save_books()
                    print(f"Статус книги с ID {book_id} обновлен на '{new_status}'.")
                else:
                    print("Некорректный статус. Используйте 'в наличии' или 'выдана'.")
            else:
                print("Книга с указанным ID не найдена.")
        except ValueError:
            print("ID должен быть числом!")

    def delete_book(self):
        """Удаляет книгу по ID."""
        try:
            self.display_books()
            book_id = int(input("Введите ID книги для удаления: ").strip())
            book = self.find_book_by_id(book_id)
            if book:
                self.books.remove(book)
                self.save_books()
                print(f"Книга с ID {book_id} под названием {book.title} удалена.")
            else:
                print("Книга с указанным ID не найдена.")
        except ValueError:
            print("ID должно быть числом!")

def main():
    manager = Library()
    while True:
        print("\n1. Добавить книгу\n2. Удалить книгу\n3. Поиск книг\n4. Отобразить все книги\n5. Изменить статус книги\n6. Выход")
        choice = input("Выберите действие: ").strip()
        if choice == "1":
            manager.add_book()
        elif choice == "2":
            manager.delete_book()
        elif choice == "3":
            manager.search_books()
        elif choice == "4":
            manager.display_books()
        elif choice == "5":
            manager.change_status()
        elif choice == "6":
            print("Вы вышли из программы.\nБлагодарим что пользуетесь нашим приложением и надеемся что вы ещё вернетесь к нам😊. ")
            break
        else:
            print("Некорректный выбор 😢.\nПожалуйста попробуйте снова у вас все получиться👌.")

if __name__ == "__main__":
    main()
