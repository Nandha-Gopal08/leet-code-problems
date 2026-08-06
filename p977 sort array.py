def sort_arr(nums):
    n=len(nums)
    for i in range(n):
        nums[i]=nums[i]*nums[i]
    for i in range(n):
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums
nums = [-7,-3,2,3,11]
print(sort_arr(nums))
