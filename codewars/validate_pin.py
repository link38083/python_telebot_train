import re
from string import digits, ascii_letters, punctuation

def validate_pin(pin):
#    count = len(re.findall(r'\b\d+\b', "".join(n.split())))
#    print(n.split(","))
#    print(count)
#    return count
#    return "".join(str(int(x) for x in n.split(","))).count() == 4 or n.isnumeric().count() == 6
#    if (len([i for i in pin if i in digits]) == 4 or len([i for i in pin if i in digits]) == 6) and \
#    if [i for i in pin if i in ascii_letters] or [i for i in pin if i in punctuation]:
#        return False
#    elif len([i for i in pin if i in digits]) == (4 or 6) :
#        return True
#    else:
#        return False
    return pin.isdigit() and len(pin) in (4,6)

print(validate_pin("1234"))


