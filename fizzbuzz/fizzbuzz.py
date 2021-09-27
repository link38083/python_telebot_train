for n in range(100):
    print("fizz"*(not n%3) + "buzz"*(not n%5) or n)
#    print("fizzbuzz"[n%-3&4:12&8-(n%-5&4)] or n)
# второй тоже вариант, это будет прям ЛевелАп