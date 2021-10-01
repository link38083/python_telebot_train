def get_middle(s):
    slist = list(s)
    n = len(slist)
    middle = "".join((slist[int(n/2-0.5)], slist[int(n/2+0.5)])*(not n%2) or slist[int(n/2)])
    return middle

print(get_middle("djosfbgdfghsdfdjfhsdj"))
