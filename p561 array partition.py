def pairsum(nums):
    nums.sort()
    total=0
    i=0
    while(i<len(nums)):
        total+=nums[i]
        i+=2
    return total
nums=[1,4,3,2]
print(pairsum(nums))
