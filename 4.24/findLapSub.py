def findLapSub(s, sub):
    times = 0
    for i in range(len(s)):
        if s[i:i+len(sub)] == sub:
            times += 1
        else:
            pass
    print times

findLapSub('frisisisisisisip','sis')
