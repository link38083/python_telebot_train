word = input()

def is_isogram(word):
    clean = word.lower()
    list = []
    for i in clean:
        if i.isalpha():
            if i in list:
                return False
            list.append(i)
    return True

print(is_isogram(word))

# программа выдает, является ли наше слоав изограммой