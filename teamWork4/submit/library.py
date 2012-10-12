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
        return str(self.id) + ' : ' + self.title + ' by ' + self.author
    

class Patron(object):

    def __init__(self, name, library):
        '''Initializes all the information of a patron.'''
        self.name = name
        self.library = library
        self.books = set() #!!!

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


class Calendar(object):

    def __init__(self):
        '''Initializes the date information.'''
        self.date = 0

    def get_date(self):
        '''Returns the date now.'''
        return self.date

    def advance(self):
        '''Puts time forward.'''
        self.date += 1


class Library(object):

    def __init__(self):
        '''Initializes the Library.'''
        lines = []
        raw_content = ''
        self.books = []#books available in the library
        self.calendar = Calendar()#singleton should be applied
        self.patrons = {}#patron name as key and patron object as value
        self.patrons_books = {}#patron name as key and books set as value
        self.is_open = False
        self.current_patron = None
        self.current_patron_books = {}#the dictionary of books of the current patron
        self.search_ids = []#the ids of the books found by the search method

        try:
            f = open('collection.txt')
        except IOError, e:
            print 'Unable to open collection.txt.'
        else:
            lines = f.readlines()
            f.close()
        for line in lines:
            line = line.strip('\n')
            raw_content += line
        content_list = eval(raw_content)
        index = 0
        for book_info in content_list:
            id = 10000 + index
            index += 1
            book = Book(id, book_info[0], book_info[1])
            self.books.append(book)
        
    
    def open(self):
        '''Opens the library.'''
        if self.is_open:
            raise Exception('The library is already open!')
        else:
            self.calendar.advance()
            self.is_open = True
        print 'Today is day ' + str(self.calendar.get_date()) + '.\n'
            
    def find_all_overdue_books(self):
        '''Finds all the patrons with overdue books and the books as well.'''
        over_due = False #indicates whether the library has any overdue books.
        over_due_string = ''
        for patron in self.patrons_books:
            over_due_books = []
            for book in self.patrons_books[patron]:
                if self.calendar.get_date() > book.get_due_date():
                    over_due_books.append(book)
                    over_due = True
                else:
                    pass
            if over_due:
                over_due_string += (patron + ':\n')
                for book in over_due_books:
                    over_due_string += (str(book) + '\n')
            over_due = False
        if over_due_string == '':
            over_due_string = 'No books are over due.'
        else:
            pass
        print over_due_string + '\n'

    def issue_card(self, name_of_patron):
        '''Issues a card to a person new to the library.'''
        if self.is_open:
            if name_of_patron in self.patrons:
                print name_of_patron + ' already has a library card.'
            else:
                self.patrons[name_of_patron] = Patron(name_of_patron, self)
                self.patrons_books[name_of_patron] = set([])
                print 'Library card issued to ' + name_of_patron + '.\n'
        else:
            raise Exception('The library is not open.')

    def serve(self, name_of_patron):
        '''Changes the patron to be served.'''
        if self.is_open:
            if name_of_patron in self.patrons:
                self.current_patron = self.patrons[name_of_patron]
                books_string = ''
                books = list(self.patrons_books[name_of_patron])
                for i in range(0, len(books)):
                    self.current_patron_books[i] = books[i]
                    books_string += (str(i) + '.' + str(books[i]) + '\n')
                print 'Now serving ' + name_of_patron + '.' + '\n' +books_string + '\n'
            else:
                print name_of_patron + ' does not have a library card.\n'
        else:
            raise Exception('The library is not open.')

    def find_overdue_books(self):
        '''Finds out all the overdue books of the current patron.'''
        if self.is_open:
            if self.current_patron != None:
                over_due_string = ''
                books = self.patrons_books[self.current_patron.get_name()]
                for book in books:
                    if book.get_due_date() < self.calendar.get_date():
                        over_due_string += (str(book) + '\n')
                    else:
                        pass
                if over_due_string == '':
                    return None
                else:
                    print over_due_string + '\n'
            else:
                raise Exception('No patron is currently being served.')
            pass
        else:
            raise Exception('The library is not open.')

    def check_in(self, *book_numbers):
        '''Checks in some borrowed books.'''
        if self.is_open:
            if self.current_patron != None:
                book_amount = 0
                for book_number in book_numbers:
                    book_set = set([])
                    if book_number in self.current_patron_books:
                        rt_book = self.current_patron_books[book_number]
                        rt_book.check_in()
                        self.books.append(rt_book)
                        for book in self.patrons_books[self.current_patron.get_name()]:
                            if book.get_id() == rt_book.get_id():
                                book_amount += 1
                            else:
                                book_set.add(book)
                        self.patrons_books[self.current_patron.get_name()] = book_set
                    else:
                        raise Exception('The patron does not have book ' + str(book_number) + '.')
                print self.current_patron.get_name() + ' has returned ' + str(book_amount) + ' books.\n'
            else:
                raise Exception('No patron is currently being served.')
        else:
            raise Exception('The library is not open.')

    def search(self, string):
        '''Searches for the books containing the string in their titles or author names.'''
        result_list = []
        middle_result_list = []
        lower_case_string = string.lower()
        result_string = ''
        if len(string) >= 4:
            for book in self.books:
                book_info = ''
                if lower_case_string in book.get_title().lower() or lower_case_string in book.get_author().lower():
                    middle_result_list.append(book)
                else:
                    pass
            for i in range(0, len(middle_result_list)):
                flag = True
                for j in range(i + 1, len(middle_result_list)):
                    if middle_result_list[i].get_title() == middle_result_list[j].get_title():
                        flag = False
                        break
                    else:
                        pass
                if flag:
                    result_list.append(middle_result_list[i])
                else:
                    pass
            if len(result_list) != 0:
                for book in result_list:
                    result_string += (str(book) + '\n')
                    self.search_ids.append(book.get_id())
            else:
                result_string = 'No books found.'
            print result_string + '\n'
        else:
            print 'Search string must contain at least four characters.\n'

    def check_out(self, *book_ids):
        '''Checks out some books.'''
        if self.is_open:
            if self.current_patron != None:
                if len(book_ids) > 3:
                    raise Exception('You are allowed to check out 3 books at most.')
                else:
                    book_amount = 0
                    for book_id in book_ids:
                        pos = False
                        for possible_book in self.books:
                            if book_id == possible_book.get_id():
                                pos = True
                                break
                            else:
                                pass
                        if pos:
                            for book in self.books:
                                if book_id == book.get_id():
                                    book.check_out(self.calendar.get_date() + 7)
                                    self.patrons_books[self.current_patron.get_name()].add(book)
                                    self.books.remove(book)
                                    book_amount += 1
                        else:
                            raise Exception('The library does not have book ' + str(book_id) + '.')
                    print str(book_amount) +' books have been checked out to ' + self.current_patron.get_name() + '.\n'
            else:
                raise Exception('No patron is currently being served.')
        else:
            raise Exception('The library is not open.')
    
    def renew(self, *book_ids):
        '''Renews the books for the patron currently being served.'''
        if self.is_open:
            if self.current_patron != None:
                book_amount = 0
                for book_id in book_ids:
                    flag = False
                    for book in self.patrons_books[self.current_patron.get_name()]:
                        if book.get_id() == book_id:
                            book.check_out(self.calendar.get_date() + 7)
                            book_amount += 1
                            flag = True
                            break
                        else:
                            pass
                    if not flag:
                        raise Exception('The patron does not have book ' + str(book_id) + '.')
                    else:
                        pass
                print str(book_amount) + ' books have been renewed for ' + self.current_patron.get_name() + '.\n'
            else:
                raise Exception('No patron is currently being served.')
        else:
            raise Exception('The library is not open.')

    def close(self):
        '''Closes the library.'''
        if self.is_open:
            self.is_open = False
            self.current_patron = None
            self.current_patron_books = {}#the dictionary of books of the current patron
            self.search_ids = []
            print 'Good night.\n'
        else:
            raise Exception('The library is not open.')

    def quit(self):
        '''End the program.'''
        quit('The library is now closed for renovations.')
