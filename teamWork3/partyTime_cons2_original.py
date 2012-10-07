def cons_2(relation_list):
    '''Solves problem limited by constraint #2.'''
    #print relation_list
    ini_invited_list = range(0, len(relation_list))
    relation_sum_dic = {}
    for i in ini_invited_list:
        summation = 0
        for j in relation_list[i]:
            summation += j
        relation_sum_dic[i] = summation
    final_dic = recursive_subt(relation_sum_dic, relation_list)
    return final_dic.keys()
    
def recursive_subt(relation_sum_dic, relation_list):
    '''Uses recursive method to get rid of the illegal elememt.'''
    changed = False
    keys = relation_sum_dic.keys()
    for j in keys:
        if relation_sum_dic[j] <= 0:
            #print 'sum of', j, '<= 0'
            del relation_sum_dic[j]
            #print 'after_delete', relation_sum_dic
            for k in relation_sum_dic:
                relation_sum_dic[k] -= relation_list[k][j]
                #print 'after_change', relation_sum_dic
                changed = True
        else:
            pass
    if changed:
        return recursive_subt(relation_sum_dic, relation_list)
    else:
        return relation_sum_dic

def read_file(file_name):
    '''Reads datas from a file.'''
    try:
        f = open(file_name)
    except IOError, e:
        print 'Unable to open file ' + file_name
    else:
        file_data = f.readlines()
        f.close()
    return file_data

def parse_file_data(file_data, data_list, name_dic):
    '''Parse the file datas.'''
    digit_data_list = []
    for i in range(0, len(data_list)):
        sub_digit_list = [0] * len(data_list)
        for j in range(1, len(data_list[i])):
            name = data_list[i][j][1:]
            sign = data_list[i][j][0]
            if name in name_dic:
                index = name_dic[name]
                if sign == '+':
                    sub_digit_list[index] = 1
                elif sign == '-':
                    sub_digit_list[index] = -1
                else:
                    pass
        digit_data_list.append(sub_digit_list)
    return digit_data_list

def solve_2(file_name):
    '''Solve constraint #2 and print out the solution.'''
    file_data = read_file(file_name)
    data_list = []
    name_dic = {}
    for s in file_data:
        sub_list = s.split()
        data_list.append(sub_list)
    for i in range(0, len(data_list)):
        name_dic[data_list[i][0]] = i
    relation_list = parse_file_data(file_data, data_list, name_dic)
    final_list = cons_2(relation_list)
    final_name_list = []
    for i in final_list:
        for j in name_dic:
            if name_dic[j] == i:
                final_name_list.append(j)
            else:
                pass
    print 'The solution to constraint #2 is: \n', final_name_list

if __name__ == '__main__':
    solve_2('nameInfo.txt')
