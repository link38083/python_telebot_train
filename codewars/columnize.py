import numpy as np

def columnized(items, columns_count):
    #cols = [items[i::columns_count] for i in range(columns_count)]
    #widths = [max(map(len, i)) for i in cols]
    #return "\n".join(' | '.join(i + " " * (w - len(i)) for i, w in zip(row, widths)) for row in itertools.zip_longest(*cols, fillvalue=""))
    #a = np.array(items)
    #b = np.arange(a.reshape(len(items)//columns_count, columns_count))
    #return a
    ints = ([int(n) for n in items])
    a = np.array(ints)
    b = a.reshape(len(items) // columns_count+1, columns_count)
    print(b)
print(columnized(["1", "12", "123", "1234", "12345", "123456"], 4))