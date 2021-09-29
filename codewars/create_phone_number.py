def create_phone_number(n):
    return (f"("+"".join([str(x) for x in n[:3]])+") "+"".join([str(x) for x in n[3:6]])+"-"+"".join([str(x) for x in n[6:10]]))

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9]))