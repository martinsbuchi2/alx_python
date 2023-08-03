def common_elements(set_1, set_2):
    common_set = set()
    for i in set_2:
        if i in set_1:
            common_set.add(i)
            
    return common_set