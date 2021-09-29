def solution(s):
    print(len(s)%2)
    if len(s) % 2:
        s = s + "_"
    s = [s[i:i+2] for i in range(0,len(s),2)]
    print(s)

    return s

solution("qwertyuiopasdfghj")