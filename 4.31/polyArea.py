import math

def area_of_polygon(lst):
    '''Calculates the area of a polygon which is defined by the points in the list
The points in the list should be in the right order.'''
    point_num = len(lst)
    area = 0
    if point_num >= 3:
        x1, y1 = lst[0]
        x2, y2 = lst[1]
        x3, y3 = lst[2]
        triangle_area = abs((x1 * y2 + x2 * y3 + x3 * y1 - y3 * x1 - y1 * x2 - y2 * x3) / 2.0)
        #this fomula is a little different from textbook
        lst = lst[0:1] + lst[2:]
        area = triangle_area + area_of_polygon(lst)
    else:
        area = 0
    return area


lst = [(0,0), (0,0.5), (1.0,0.5), (1.0,0)]
print area_of_polygon(lst)
    
