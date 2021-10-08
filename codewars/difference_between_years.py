def how_many_years(date1, date2):
    n = int(date1[:4]) - int(date2[:4])
    return n if n>0 else -n

def how_many_years (date1,date2):
    return abs(int(date1[:4]) - int(date2[:4]))

print(how_many_years('1997/10/10', '2015/10/10'))