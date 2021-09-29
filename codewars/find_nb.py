def find_nb(m):
    n = int(m**(1./3.))
    #print (n)
    total_volume = 0
    for i in range (1,n+1):
      #print (i*i*i)
      total_volume += i*i*i
      print (total_volume)
      if(total_volume == m):
        #print (i)
        return i
        break
    return -1

print(find_nb(1071225))

# код выдает нам номер числа, которое будет последним в сумме 