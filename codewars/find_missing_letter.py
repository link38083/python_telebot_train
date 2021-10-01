#1

def find_missing_letter(chars):
    for n in chars[1:]:
        if abs(ord(n) - ord(chars[chars.index(n)-1]) == 2):
            return chr(ord(n)-1)

#2
def find_missing_letter(chars):
    return "".join([chr(ord(n)-1) for n in chars if abs(ord(n) - ord(chars[chars.index(n)-1]) == 2)])

#def find_missing_letter(chars):
 #   #print([chr(ord(n)) for n in enumerate(chars)])
  #  return "".join([chr(ord(n(1))-1) for n in chars if abs(ord(n) - ord(chars[chars.index(n)-1]) == 2)])

print(find_missing_letter(['O','Q','R','S']))