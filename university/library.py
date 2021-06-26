import re
import os

class Library:
    __secret_key = os.environ.get("SECRET_LIB_KEY", default=None)
    __books_list = ["harry potter", "Убийство в восточном экспрессе ", 'Страна радости', 'Alice in wonderland']

    @classmethod
    @property
    def books_list(cls):
        if cls.__secret_key is not None:
            return cls.__books_list
        else:
            return "Forbidden"

    @classmethod
    def give_book(cls, book_name):
        if cls.__secret_key is not None and book_name in cls.__books_list:
            cls.__books_list.remove(book_name)
            return cls.__books_list
        else:
            print(f"Can't give this book {book_name} to you")
            return False

    @classmethod
    def return_book(cls, book_name):
        if cls.__secret_key is not None and book_name not in cls.__books_list:
            cls.__books_list.append(book_name)
            return cls.__books_list
        else:
            return False


    @staticmethod
    def check_student_key(student): # можете поставить public_key
        pattern = r"\b([a-zA-z0-9]{4})-([a-zA-z0-9]{4})-([a-zA-z0-9]{6})$"

        try:
            matched = re.match(pattern, student.public_key) # тогда здесь просто заменить на public_key
            print("Public Key Success", matched.group()[:8]+"***")
            return True
        except Exception:
            print("Wrong Public Key")
            return False