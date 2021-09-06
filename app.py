def foo(a, b, c):
    return c([a, b])

print(foo(1, 3, sum))
print(foo(1, 1, set))