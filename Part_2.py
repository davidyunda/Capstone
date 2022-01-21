# Part 2: Author class - no duplicate books
# Start with the program from part 1.
# In this version, an author can't publish two books with the same name.

# When the publish function is called, print an error message if the book given has the 
# same name as a book currently in the books list. (In other words, make sure the Author 
# object's book list doesn't already contain that name).

class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

    def publish(self, title):
        self.books.append(title)        
    
    def __str__(self):
        not_duplicated = set(self.books)
        new_list = []
        
        for b in not_duplicated:
            if b in self.books:
                new_list.append(b)
                self.books.remove(b)
            
        titles = ', '.join(new_list) or 'No published books'
        if len(self.books) > 0:
            print('This books were duplicated: ')
            print(self.books)
    
        return f'{self.name}. Books: {titles} '

def main():
    new_book = Author('David')
    new_book.publish('The two bears')
    new_book.publish('On the running')
    new_book.publish('On the running')
    new_book.publish('Algebra 101')
    new_book.publish('Algebra 101')
    print(new_book)

main()
