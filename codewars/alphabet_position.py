from string import ascii_letters
text1 = "siboru topchik"

def qq(text):
    rtext = " ".join([str(ord(c)-96) for c in text.lower() if c in ascii_letters])
    return(rtext)

print(qq(text1))

#данный код переводит буквы в их порядковый номер и выписывает их в строчку, игнорируя пробелы
