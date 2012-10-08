class Book(object):

    def __init__(self, id, title, author):
        '''Initialize all the information.'''
        self.id = id
        self.title = title
        self.author = author
        self.due_date = None
        self.checked_out = False
        
    def get_id(self):
        '''Returns the id of a book.'''
        return self.id
    
    def get_title(self):
        '''Returns the title of a book.'''
        return self.title
    
    def get_author(self):
        '''Returns the author of a book.'''
        return self.author
    
    def get_due_date(self):
        '''Returns the due date of a book.'''
        return self.due_date
    
    def check_out(self, due_date):
        '''Checks out a book.'''
        self.due_date = due_date
        
    def check_in(self):
        '''Checks in a book.'''
        self.due_date = None
        
    def __str__(self):
        '''Returns all the information of the book.'''
        return self.id + ' : ' + self.title + ' by ' + self.author
    

b = Book('01', 'Gone with the wind', 'Austin')
print b.id, b.title, b.author, b.due_date, b.checked_out
print b.get_id(), b.get_title(), b.get_author(), b.check_out(12), b.get_due_date()
print b.check_in(), b


