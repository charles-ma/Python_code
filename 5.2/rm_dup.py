def remove_dup(lis):
    '''Removes the duplicate values in the list using dictionary.'''
    dic = {}
    for i in lis:
        dic[i] = i
    return dic.keys()

def remove_dup_1(lis):
    '''Another implement of remove_dup not using dictionary.'''
    result_list = []
    for i in lis:
        if not i in result_list:
            result_list.append(i)
        else:
            pass
    return result_list


if __name__ == '__main__':
    lis = [1, 2, 2, 3, 5, 3, 6, 10, 20, 99, 20]
    print remove_dup(lis)
    print remove_dup_1(lis)
