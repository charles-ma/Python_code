def sieve(a):
    if a:
        return a[0 : 1] + sieve(filter(lambda x: x % a[0] != 0, a[1 :]))
    else:
        return []

print sieve(range(2, 20))
