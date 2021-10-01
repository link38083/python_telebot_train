def solution(number):
    print(range(number))
    return sum(range(number)[::3]) + sum(range(number)[::5]) - sum(range(number)[::15])

print(solution(200))