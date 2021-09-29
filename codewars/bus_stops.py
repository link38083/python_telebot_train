def number(bus_stops):
    return sum([i[0] - i[1] for i in bus_stops])

print(number([[10,0],[3,5],[5,8]]))