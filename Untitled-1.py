def snail(snail_map):
    print(snail_map)
    if snail_map == [[]]:
        return []
    elif snail_map == [[1]]:
        return [1]
    sorted_list = []
    cloned = snail_map[:]
    def snail_mapper(snail_array):
        sorted_first = []
        sorted_last = []
        snail_helper_last = []
        snail_helper_first = []
        sorted_first = snail_array[0]
        cloned.remove(cloned[0])
        sorted_last = (snail_array[-1])[::-1]
        cloned.remove(cloned[-1])
        for i in cloned:
            snail_helper_last.append(i[-1])
            i.remove(i[-1])
        for i in cloned:
            snail_helper_first.append(i[0])
            i.remove(i[0])
        snail_helper_first = snail_helper_first[::-1]
        z = sorted_first + snail_helper_last + sorted_last + snail_helper_first
        return z
    while len(cloned) > 0:
        if len(cloned) == 1:
            sorted_list = sorted_list + cloned[0]
            break
        sorted_list = sorted_list + snail_mapper(cloned)
    print(sorted_list)
    return sorted_list
