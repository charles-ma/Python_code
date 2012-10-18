class Rectangle(object):
    '''Encapsulates some calculations about the rectangles.'''
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def get_area(self):
        return self.height * self.width

    def get_peri(self):
        return 2 * (self.height + self.width)

    def is_square(self):
        if self.height == self.width:
            return True
        return False

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

rectangle = Rectangle(3,4)
print rectangle.get_area(), rectangle.get_peri(), rectangle.is_square(), rectangle.get_width(), rectangle.get_height()
print Rectangle.get_area(rectangle)
