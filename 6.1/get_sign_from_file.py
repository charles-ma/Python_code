try:
    f = open(src.txt)
except Exception, e:
    print 'Could\'t find the file named src.txt.'
else:
    lines = f.readlines()
    for line in lines:
        if '#' in line:
            print line
        else:
            pass
    f.close()

