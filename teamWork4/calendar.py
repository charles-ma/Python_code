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

