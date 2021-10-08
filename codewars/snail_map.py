def snail(snail_map):
    new_list = []

    while len(snail_map) != 0:
        new_list.extend(snail_map[0])
        snail_map.remove(snail_map[0])
        if len(snail_map) == 0:
            break
        for i in snail_map:
            new_list.append(i.pop())
        new_list.extend(reversed(snail_map[len(snail_map)-1]))
        snail_map.remove(snail_map[len(snail_map)-1])
        if len(snail_map) != 1:
            list_2 = []
            for i in snail_map:
                list_2.append(i.pop(0))
            new_list.extend(reversed(list_2))
    return new_list

print(snail([[1,2,3],
            [4,5,6],
            [7,8,9]]))