def square(num):
    a = ([n for n in (list(str(num)))])
    return "".join([str(int(n)**2) for n in a])

print(square(9223))