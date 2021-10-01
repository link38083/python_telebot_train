def snail(snail_map):
    new_list = []

    while len(snail_map) != 0:
        new_list.extend(snail_map[0])
        # easier to know when finished and avoid adding repeats with column and row elements
        # if we just trim away sections we've already dealt with from original 2d list
        snail_map.remove(snail_map[0])

        # will exit while-loop if nothing left (for later iterations of while loop)
        if len(snail_map) == 0:
            break

        # 2: (on first go) (going down rightmost column of 2d list)
        for i in snail_map:
            # for each leftover list in 2d list, pops off the ending item from original 2d list
            # and appends that to the new list
            new_list.append(i.pop())

        # 3: (going left) (on first go, just takes the list at the bottom, flips it,
        # and then adds it to the new list)
        new_list.extend(reversed(snail_map[len(snail_map)-1]))
        # stripping it away from original 2d list
        snail_map.remove(snail_map[len(snail_map)-1])

        # 4: (going up leftmost column) (depending) (if we are not at the last list)
        if len(snail_map) != 1:
            # created another list to contain values, so that we can flip them before adding them
            list_2 = []
            for i in snail_map:
                # for each leftover list in 2d list, we pop off the values at the front and then append
                # them to the list created right before for-loop
                list_2.append(i.pop(0))
            # after for-loop, we add this temporary list's values after its been flipped
            new_list.extend(reversed(list_2))

        # the while-loop will repeat this process until we have nothing left of the original 2d list

    # when the while-loop terminates we return the final list for the traversal
    return new_list