import string


def remove_chars(s):
    return "".join([n for n in s if (n in string.ascii_letters) or (n in string.whitespace)])

print(remove_chars("hiui23 56 ssd"))