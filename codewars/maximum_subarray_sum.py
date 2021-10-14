def max_squence(arr):
    #print(sum(listi))
    #return [sum(listi[n:n+4]) for n in listi[:-4]]
    list1 = []
    ss = list(enumerate(arr))
    print(ss)
    for i in ss[:-3]:
        #print(ss[i[0]][0])
        list1.append(ss[ss[i[0]][0]][1]+ss[ss[i[0]][0]+1][1]+ss[ss[i[0]][0]+2][1]+ss[ss[i[0]][0]+3][1])
    print(list1)
    return (max(list1))

print(max_squence([-2, 1, -3, 4, -1, 2, 1, -5, 4, 7, -10]))
#0 1 2 6 -3 2