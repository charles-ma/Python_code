import random

def random_element(lst):
    length = len(lst)
    random_selected = random.randint(0,length - 1)
    return lst[random_selected]

lst = [0, 1, 2, 3, 4, 5, 6]
print random_element(lst)
