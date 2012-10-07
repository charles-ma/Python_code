def my_bisect(lst, ele):
    '''lst should be sorted!'''
    return bi_sort(0, len(lst) - 1, lst, ele)

def bi_sort(low, high, lst, ele):
    if high > low + 1:
        middle = (high - low) / 2 + low
        if ele > lst[middle]:
            return bi_sort(middle, high, lst, ele)
        else:
            return bi_sort(low, middle, lst, ele)
    else:
        return high

lst = [1,2,5,6,7]
print my_bisect(lst,3)
