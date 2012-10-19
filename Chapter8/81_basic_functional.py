a = [0, 1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7, 8]
print filter(lambda x :x != 0, a)
print filter(lambda x :x % 2 != 0, a)
print reduce(lambda x, y: x + y, a)
print map(lambda x, y: (x + y) % 2 != 0, a, b)
print map(lambda x, y, z: (x + y) <= z, a, a, b)

a = range(1, 11)
print map(lambda x: x * x, a)
print map(lambda x: x ** 3, a)
print map(lambda x: x + 1, a)
print filter(lambda x: x % 2 == 0, a)
print filter(lambda x: x % 3 == 0, a)
print reduce(lambda x, y: x + y, [], 1)

def ave(lst):
    if lst:
        summation = reduce(lambda x, y: x + y, lst)
        return (summation + 0.0) / len(lst)
    else:
        return None

print ave(a)
print ave([])

print reduce(lambda x, y: x and y, filter(lambda x: x % 2 == 0, a))
print reduce(lambda x, y: x or y, filter(lambda x: x % 2 == 0, a))
d = [1, lambda x: x * 2, 3]
print d[1](2)
print filter(lambda x : x <= 5, a)
print [x ** 2 for x in a if x % 2 == 0]
print [x for x in a if x not in b]
print a + [x for x in b if x not in a]
f = lambda x, y: ((x < y) and x) or y
print f(0, 3)
print [1] and 5
def a(x):
    f = lambda x: x + 3
    print f(3)
    print x
a(4)



