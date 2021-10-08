def check_exam(arr1, arr2):
    sum = 0
    print(arr1[1] == arr2[1], range(len(arr1)))
    for n in range(len(arr1)):
        if arr1[n] == arr2[n]:
            sum = sum + 4
        elif arr2[n] == "":
            sum = sum
        else:
            sum = sum - 1
    if sum < 0:
        return 0
    return sum

print(check_exam(["a", "b", "c", "d"], ["a", "b", "c", "a"]))