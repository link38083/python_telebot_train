def shades_of_grey(n):
    nlist = []
    if 0<n:
        if n>254:
            n = 254
        for i in range(1, n+1):
            grey = str(hex(i)[2:].lower())
            if len(grey) < 2:
                grey = "0" + grey
            nlist.append("#" + grey + grey + grey)
        return nlist
    else:
        return []

def shades_of_grey(n):
  if n > 254:
    n = 254
  return ["#%02x%02x%02x" % (i,i,i) for i in range(1,n+1)]

print(shades_of_grey(1115))