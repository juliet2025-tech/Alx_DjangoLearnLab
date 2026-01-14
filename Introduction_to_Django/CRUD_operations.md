# CRUD Operations for Book Model

This file documents the database operations performed in the Django shell using the `Book` model from the `bookshelf` app.  
Each section includes the exact commands and the expected outputs.

---

## Create

```python
from bookshelf.models import Book
book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)
# <Book: 1984 by George Orwell>
 
# Retrieve
 books = Book.objects.all()
books
# <QuerySet [<Book: 1984 by George Orwell>]>

#Update
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book
# <Book: Nineteen Eighty-Four by George Orwell>


#Delete
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Book.objects.all()
# <QuerySet []>



