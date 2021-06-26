import os
from library import Library

class Student:
    def __init__(self,name):
        self.__name=name
        self.__public_key=os.environ.get('SECRET_LIB_KEY')
        self.books_taken=[]
    @classmethod
    @property
    def blic_key(cls):
        print(cls.__public_key)

    @classmethod
    @property
    def get_book(cls,LibraryClass,book_name):
        if book_name in Library.book_list() and Library.check_student_key(self.__public_key):
            LibraryClass.give_book(book_name)
            self.books_taken.append(book_name)
        else:
            return "оп,сломались"

    def return_book(self, book_name):
        if book_name == Library.book_list:
            print("This book is in Library already")
            return False
        if not Library.check_student_key(self.__public_key):
            print("Your public key is wrong or missing")
            return False
        else:
            self.books_taken.remove(book_name)
            Library.return_book(book_name)
