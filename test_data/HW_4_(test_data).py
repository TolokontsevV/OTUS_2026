import csv
import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
print(f"BASE_DIR: {BASE_DIR}")

def conversion_for_dict(filename: str) -> list[dict]:
    """
    Преобразуем CSV файл в список с словарями
    """
    file_path = BASE_DIR / "data" / filename
    with open(file_path, newline='') as file:
        reader = csv.DictReader(file)
        data_books = list(reader)
    return data_books


def deserialization_json(filename: str) -> list[dict]:
    """
    Десериализация JSON файла в список с словарями
    """
    file_path = BASE_DIR / "data" / filename
    with open(file_path, 'r', encoding='utf-8') as file:
        data_users = json.load(file)
    return data_users


def distribution_of_books(users: list[dict], books: list[dict]) -> list[dict]:
    """
    Распределяет книги по пользователям и возврвщвет новый список со словарями.
    """
    result = []
    index_book = 0
    length_books = len(books)
    length_users = len(users)
    number_books_for_user = length_books / length_users

    for index in range(length_users):
        user: dict = users[index]
        data_user = {
            "name": user.get('name'),
            "gender": user.get('gender'),
            "address": user.get('address'),
            "age": user.get('age'),
            "books": []
        }

        if number_books_for_user % 1 != 0 and index == length_users - 1:
            numeric = round((number_books_for_user // 1) + 1)
        else:
            numeric = round(number_books_for_user // 1)

        for _ in range(numeric):
            book: dict = books[index_book]
            data_book = {
                "title": book.get('Title'),
                "author": book.get('Author'),
                "pages": book.get('Pages'),
                "genre": book.get('Genre')
            }
            data_user.get('books').append(data_book)
            index_book += 1

        result.append(data_user)
    return result


def save_json(total_date: list[dict], filename: str) -> None:
    """
    Записывает в файл JSON.
    """
    file_path = BASE_DIR / "data" / filename
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(total_date, file, ensure_ascii=False, indent=2)


def app() -> None:
    users = deserialization_json('users.json')
    books = conversion_for_dict('books.csv')
    result = distribution_of_books(users=users, books=books)
    save_json(total_date=result, filename='result.json')


if __name__ == '__main__':
    app()
