def find_nb(m):
    i=0
    while int((i(i+1)/2)**2) < m:
        i += 1
    if ((i(i+1)/2)^2) == m:
        return(i)
    return(-1)

print(find_nb(1071225))

# no comments, just math
# смотри find_nb для объяснений