numbers = [34, 22, 65, 3423, 64]

def sum_two_smallest_numbers(numbers):
    s = min(numbers)
    numbers.remove(s)
    s2 = min(numbers.remove(s))
    sum = s + s2
    return sum

print(sum_two_smallest_numbers(numbers))