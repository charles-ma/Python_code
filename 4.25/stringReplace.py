def string_overlap_replace(ori_string, string_to_replace, string_to_add):
    '''Replaces all the occurences of string_to_replace by string_to_add.'''
    replace_list = []
    for i in range(0, len(ori_string)):
        if ori_string[i:i + len(string_to_replace)] == string_to_replace:
            replace_list.append(i)
        else:
            pass
    for i in range(0, len(replace_list)):
        ori_string = ori_string[0:replace_list[i]] + string_to_add + ori_string[replace_list[i] + len(string_to_replace):]  
    return ori_string

print string_overlap_replace('frisisisisisip', 'sis', 'xix')
