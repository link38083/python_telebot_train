def likes(names):
    #if len(names) == 0:
    #    return ("no one likes this")
    #elif len(names) == 1:
    #    return (f"{names[0]} likes this")
    #elif len(names) == 2:
    #    return (f"{names[0]} and {names[1]} like this")
    #elif len(names) == 3:
    #    return (f"{names[0]}, {names[1]} and {names[2]} like this")
    #elif len(names) > 3:
    #    return (f"{names[0]}, {names[1]} and {len(names[2:])} others like this")

    dict = {
        0: "no one likes this",
        1: f"{names[0]} likes this",
        2: f"{names[0]} and {names[1]} like this",
        3: f"{names[0]}, {names[1]} and {names[2]} like this",
        4: f"{names[0]}, {names[1]} and {len(names[2:])} others like this"
    }
    return (dict[len(names)])

print(likes(['Alex', 'Jacob', 'Mark', "hui"]))