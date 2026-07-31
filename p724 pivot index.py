def pivot(nums):
    total=sum(nums)
    left_sum=0
    for i in range(len(nums)):
        right_sum=total-left_sum-nums[i]
        if right_sum==left_sum:
            return i
        left_sum+=nums[i]
    return -1
        
nums=[1,2,3]
print(pivot(nums))
