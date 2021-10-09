def narcissistic(value):
    v = len(str(value))
    print(v)
    print(sum([int(n)**v for n in str(value)]))
    return sum([int(n)**v for n in str(value)]) == value

print(narcissistic(153382))