from sets import Set

class Patron(object):

    def __init__(self, name, library):
        '''Initializes all the information of a patron.'''
        self.name = name
        self.library = library
        self.books = Set() #!!!

    def get_name(self):
        '''Returns the patron's name.'''
        return self.name

    def check_out(self, book):
        '''Adds this Boook object to the set of books checked out by this patron.'''
        self.books.add(book)

    def give_back(self, book):
        '''Removes the Book object from the set of books checked out by this patron.'''
        self.books.remove(book)

    def get_books(self):
        '''Returns the books checked out by this patron.'''
        return self.books

    def send_overdue_notice(self, notice):
        '''Tells this patron that he/she has overdue books.'''
        print 'Dear', self.name, ': you own the library some books!'
        print notice
    
p = Patron('a', 'b')
p.check_out('Python')
print p.books
print p.get_books()
p.give_back('Python')
print p.books
print p.send_overdue_notice('Good Job!')
