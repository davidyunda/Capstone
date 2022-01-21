# Part 1: Author class
# Create a new class called Author.
# An Author has a name, and a list of books published.
# When you create a new Author, they don't have any books. So create an empty books list attribute in the __init__ method.
# Your Author class should have a publish method, which takes the title of a book as an argument. Add the title of this book to this object's books list.
# Add a __str__ method that returns a String with the author's name, and the names of all of their book's titles.
# Write a main function to test your class, create some example authors, and publish some example books.

class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

    def publish(self, title):
        self.books.append(title)        
    
    def __str__(self):
        titles = ', '.join(self.books) or 'No published books'
        return f'{self.name}. Books: {titles}'

def main():
    new_book = Author('David')
    new_book.publish('The two bears')
    new_book.publish('On the running')
    print(new_book)

main()

