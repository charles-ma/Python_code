def frequency(lis):
    '''This function counts the frequencies of different entries.'''
    dic = {}
    for i in lis:
        count = dic.get(i, 0)
        count += 1
        dic[i] = count
    return dic

def dis_fre(lis):
    '''This function prints out the counting result in a visual fasion.'''
    dic = frequency(lis)
    #for i in sorted(dic):
        #print i, '*' * dic[i]
    tuples = dic.items()
    tuples.sort(smaller_than)
    for i in tuples:
        print i[0], i[1] * '*'

def smaller_than(t1, t2):
    '''Defines the order of the result.'''
    if t1[1] < t2[1]:
        return 1
    elif t1[1] == t2[1]:
        #if values are the same, compare the keys
        if t1[0] < t2[0]:
            return -1
        elif t1[0] == t2[0]:
            return 0
        else:
            return 1
    else:
        return -1

if __name__ == '__main__':
    name_list = ['Jobs', 'Gates', 'Jobs', 'Page', 'Zakerburg', 'Jobs', 'Page']
    dis_fre(name_list)
