import bisect

def add(lst, ele):
    lst.append(ele)
    return lst

def test(lst, ele):
    lst.sort()
    pos = bisect.bisect(lst, ele)
    if lst[pos - 1] == ele:
        return True
    else:
        return False

def remove(lst, ele):
    lst.sort()
    pos = bisect.bisect(lst, ele)
    if lst[pos - 1] == ele:
        lst[pos - 1:pos] = []
        return ele
    else:
        return None

lst = [1, 2, 3]
print add(lst, 4)
print test(lst, 3)
print test(lst, 5)
print remove(lst, 5)
print lst
print remove(lst, 3)
print lst
