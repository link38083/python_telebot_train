a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"

def alphabet(a, b):
    rtext = "".join(sorted(list(set(a + b))))
    return rtext

# данный код объединяет списки, сортирует и выписывает уникальные символы в строчку