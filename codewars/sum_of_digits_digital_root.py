def digital_root(n):
    while (len(str(n))) > 1:
        a = sum([int(b) for b in str(n)])
    return(a)

print(root(167))