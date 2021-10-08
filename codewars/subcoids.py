def subcoids(x,y,z):
    print(sum(range(x)), sum(range(y)), sum(range(y-1)))
    print(x*x*sum(range(y-1))*sum(range(z-1)))
    n = (x*y*z) + (x*x*sum(range(y))*sum(range(z))+y*y*sum(range(z))*sum(range(x))+z*z*sum(range(y))*sum(range(x))) + (x*y+x*z+y*z) + 1
    return n

print(subcoids(2,2,2))