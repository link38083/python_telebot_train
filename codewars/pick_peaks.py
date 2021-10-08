def pick_peaks(arr):
    dict = {"pos": 0, "peaks": 0}
    pos = 0
    poslist = []
    peaks = []
    for x, y, z in zip(arr, arr[1:], arr[2:]):
        #print(x,y,z)
        #print(arr.index(n))
        pos += 1
        if x<y>z:
            print("-----------------")
            print(x, y, z, pos)
            poslist.append(pos)
            peaks.append(y)
            dict.update({"pos": poslist, "peaks": peaks})
    return dict

print(pick_peaks([3,2,3,6,4,1,2,3,2,1,2,3]))