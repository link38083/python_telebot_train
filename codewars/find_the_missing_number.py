def missing_no(nums):
    if nums[0]<nums[-1]:
        return [((n)-1) for n in nums if abs(n - nums[nums.index(n) - 1]) == 2][0]
    else:
        return [((n)+1) for n in nums if abs(n - nums[nums.index(n) - 1]) == 2][0]


nums = list(range(0,101))
nums.remove(10)
print(missing_no(nums))