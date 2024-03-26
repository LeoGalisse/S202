from database.database import Database
from model.library import LibraryModel

db = Database(database="biblioteca", collection="livros")
db.reset_database()
library = LibraryModel(db)

# Criar outros livros
book_one = library.create_book("3", "The Great Gatsby", "F. Scott Fitzgerald", 1925, 25.0)
book_two = library.create_book("4", "To Kill a Mockingbird", "Harper Lee", 1960, 20.0)
book_three = library.create_book("5", "1984", "George Orwell", 1949, 22.0)

# Ler os livros criados
books = [
    library.read_book_by_id(book_one),
    library.read_book_by_id(book_two),
    library.read_book_by_id(book_three)
]

# Atualizar um livro
library.update_book(book_one, "The Great Gatsby", "F. Scott Fitzgerald", 1925, 30.0)

# Deletar um livro
library.delete_book(book_two)
