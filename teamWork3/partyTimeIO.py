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

##_________________________________________
##Put the code below into solve_n function to get relation_list from file.

#file_data = read_file(file_name)
#data_list = []
#name_dic = {}
#for s in file_data:
#    sub_list = s.split()
#    data_list.append(sub_list)
#for i in range(0, len(data_list)):
#    name_dic[data_list[i][0]] = i
#relation_list = parse_file_data(file_data, data_list, name_dic)

##_________________________________________
##Test the code above.

file_data = read_file('nameInfo.txt')
data_list = []
name_dic = {}
for s in file_data:
    sub_list = s.split()
    data_list.append(sub_list)
for i in range(0, len(data_list)):
    name_dic[data_list[i][0]] = i
relation_list = parse_file_data(file_data, data_list, name_dic)

print relation_list
