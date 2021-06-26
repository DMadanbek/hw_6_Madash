from university.library import Library
from university.student import Student
s = Student("Loksli")
d = Student("Artur")

print(list(Library.book_list()))

s.get_book(Library, "harry potter")
d.get_book(Library, "harry potter")

s.return_book("harry potter")

print(list(Library.book_list()))

d.get_book(Library, "harry potter")

print(list(Library.book_list()))

cowsay.tux("Well Done")