import random
from sets import Set

def random_relation(size):
    '''Generates random relations between people.'''
    relation_list = []
    for i in range(0, size):
        sub_list = []
        for j in range(0, size):
           # sub_list.append(random.randint(-1, 1))
            ran_num = random.randint(1, 15)
            if ran_num <= 3:
                sub_list.append(-1)
            elif ran_num >11:
                sub_list.append(1)
            else:
                sub_list.append(0)
        relation_list.append(sub_list)
    for k in range(0, size):
        relation_list[k][k] = 0
    return relation_list

def gene_sets(relation_list):
    '''Generates sets to use.'''
    possible_set_dic = {}
    for i in range(0, len(relation_list)):
        possible_set = Set([])
        for j in range(0, len(relation_list[i])):
            if relation_list[i][j] != -1:
                possible_set.add(j)
            else:
                pass
        possible_set_dic[i] = possible_set
    return possible_set_dic

def sort_sets(possible_set_dic):
    '''Sorts the sets.'''
    set_tuples = possible_set_dic.items()
    set_tuples.sort(smaller_than)
    key_list = []
    for i in range(0, len(set_tuples)):
        key_list.append(set_tuples[i][0])
    #!!!print set_tuples
    return key_list

def smaller_than(set_tuple1, set_tuple2):
    '''Defines what's \'large\'.'''
    if len(set_tuple1[1]) < len(set_tuple2[1]):
        return 1
    elif len(set_tuple1[1]) == len(set_tuple2[1]):
        return 0
    else:
        return -1

def calculate(relation_list):
    '''Calculates possible solutions to constraint #1.'''
    #!!!print 'random list', relation_list
    possible_set_dic = gene_sets(relation_list)
    #!!!print 'possible set', possible_set_dic
    key_list = sort_sets(possible_set_dic)
    #!!!print 'key_list', key_list
    final_set = Set([])
    for i in key_list:
        i_set = possible_set_dic[i]
        for j in key_list:
            if j in i_set:
                if i_set != possible_set_dic[j]:
                    i_set = i_set & possible_set_dic[j]
                else:
                    pass
            else:
                pass
        if len(final_set) < len(i_set):
            final_set = i_set
        else:
            pass
    return rm_no_like(list(final_set), relation_list)
    
def rm_no_like(final_list, relation_list):
    '''Removes the people who does not have anyone he likes in the party.'''
    #!!!print final_list
    for i in final_list:
        summ = 0
        for j in final_list:
            summ += relation_list[i][j]
        #!!!print summ
        if summ == 0:
            final_list.remove(i)
            final_list = rm_no_like(final_list, relation_list)
            break
        else:
            pass
    #!!!print final_list
    return final_list

def cons_2(relation_list):
    '''Solves problem limited by constraint #2.'''
    #print relation_list
    ini_invite_list = calculate(relation_list)
    final_invite_list = recursive_add(ini_invite_list, relation_list)
    return final_invite_list
    
def recursive_add(ini_invite_list, relation_list):
    '''Uses recursive method to add legal elememts.'''
    for i in range(0, len(relation_list)):
        if not (i in ini_invite_list):
            if is_proper([i] + ini_invite_list, relation_list):
                ini_invite_list.append(i)
                return recursive_add(ini_invite_list, relation_list)
            else:
                pass
    return ini_invite_list

def is_proper(invite_list, relation_list):
    '''Checks whether an invite_list is legal or not.'''
    for i in invite_list:
        summation = 0
        for j in invite_list:
            summation += relation_list[i][j]
        if summation <= 0:
            return False
        else:
            pass
    return True

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
    '''Parses the file datas.'''
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

def solve_1(file_name):
    '''Solves constraint #1 and print out the solution.'''
    file_data = read_file(file_name)
    data_list = []
    name_dic = {}
    for s in file_data:
        sub_list = s.split()
        data_list.append(sub_list)
    for i in range(0, len(data_list)):
        name_dic[data_list[i][0]] = i
    relation_list = parse_file_data(file_data, data_list, name_dic)
    final_list = calculate(relation_list)
    final_name_list = []
    for i in final_list:
        for j in name_dic:
            if name_dic[j] == i:
                final_name_list.append(j)
            else:
                pass
    print 'The solution to constraint #1 is: \n', final_name_list

def solve_2(file_name):
    '''Solves constraint #2 and print out the solution.'''
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
    solve_1('nameInfo.txt')
    solve_2('nameInfo.txt')
