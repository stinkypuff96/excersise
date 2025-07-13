import json
import os

def get_answer(question_text, prompt, valid_choices=None):       # function to streamline user choice restrictions
    while True:
        print(question_text)
        answer = input(prompt).strip()
        if not answer:
            print("Input cannot be empty. Please try again.")
        elif valid_choices and answer not in valid_choices:
            print(f'Please pick between one of the given options.')
        else:
            return answer


user_data = get_answer("Log-in/Create an account.", "Username: ").strip().lower()
data_file = f"{user_data}_books.json"

def load_books():
    if os.path.exists(data_file):
        with open(data_file, "r") as f:
            return json.load(f)
    return []


def save_books(books):
    with open(data_file, "w") as f:
        json.dump(books, f, indent=4)


def display_books(books):
    if not books:
        print("No books in your collection.")
        return
    for i, book in enumerate(books, 1):
        status = "Read" if book ["read"] else "Unread"
        print(f"{i}. {book['title']} by {book['author']} "
              f"({book['year']}) - {book['genre']} - {status}")


def add_book(books):
    title = get_answer("What is the title of the book?", "Title: ").strip()
    author = get_answer("What is the name of the author?", "Author: ").strip()
    year = get_answer("What year was this book published?", "Publish year: ").strip()
    genre = get_answer("What is the genre of this book?", "Genre: ").strip()
    rarity = get_answer("What is the rarity of this book?(1 - low, 5 - high)", "Rarity: ",
                        ["1", "2", "3", "4", "5"]).strip()
    read = get_answer("Have you read this book?", "Yes or No(y/n): ", ["y", "n"]).strip().lower() == "y"

    books.append({
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "rarity": rarity,
        "read": read
    })
    print("Book added.")


def delete_book(books):
    display_books(books)
    index = int(get_answer("Which book would you like to delete?", "Book number: ")) - 1
    if 0 <= index < len(books):
        deleted = books.pop(index)
        print(f"Deleted: {deleted['title']}")

