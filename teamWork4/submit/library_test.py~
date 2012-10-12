from library import *
import unittest

class library_test(unittest.TestCase):
    '''Unittest for library.'''
    def test_book(self):
        '''Test for the book class.'''
        book = Book('01', 'Gone with the wind', 'Austin')
        self.assertEqual(book.get_id(), '01')
        self.assertEqual(book.get_title(), 'Gone with the wind')
        self.assertEqual(book.get_author(), 'Austin')
        self.assertEqual(book.get_due_date(), None)
        self.assertEqual(book.checked_out, False)
        self.assertEqual(str(book), '01 : Gone with the wind by Austin')
        book.check_out(23)
        self.assertEqual(book.get_due_date(), 23)
        book.check_in()
        self.assertEqual(book.get_due_date(), None)

    def test_patron(self):
        '''Test for the patron class.'''
        patron = Patron('a', 'b')
        patron.check_out('Python')
        self.assertEqual(patron.get_books(), set(['Python']))
        patron.give_back('Python')
        self.assertEqual(patron.get_books(), set([]))


    def test_calendar(self):
        '''Test for the calendar class.'''
        calendar = Calendar()
        self.assertEqual(calendar.get_date(), 0)
        calendar.advance()
        self.assertEqual(calendar.get_date(), 1)

    def test_library(self):
        '''Test for the library class.'''
        library = Library()
        self.assertEqual(library.open(), 'Today is day 1.')
        library.is_open = True
        self.assertRaises(Exception, library.open)

if __name__ == '__main__':
    unittest.main()
