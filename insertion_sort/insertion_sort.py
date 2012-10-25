def insertion_sort(ls):
    '''implements the insertion sort algorithm using for loop.'''
    for j in range(1, len(ls)):
        key = ls[j]
        for i in range(j - 1, -1, -1):
            if ls[i] > key:
                ls[i + 1] = ls[i]
            else:
                ls[i + 1] = key
                break
    return ls

def insertion_sort_1(ls):
    '''implements the insertion sort using while loop.'''
    for j in range(1, len(ls)):
        key = ls[j]
        i = j - 1
        while i >= 0 and ls[i] > key:
            ls[i + 1] = ls[i]
            i -= 1
        ls[i + 1] = key
    return ls

ls = [1,6,3,6,7,4,9]
print insertion_sort(ls)
print insertion_sort_1(ls)
