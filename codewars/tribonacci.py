def tribonacci(signature, n):
    if n < 1:
        return []
    if n < len(signature):
        return signature[0:n]
    inc = 0
    seq = signature[:]
    while inc <= n:
        add = sum(seq[inc:inc + 3])
        seq.append(add)
        inc += 1
    return seq[0:n]

print(tribonacci([0, 0, 1], 10))