def runningSum( nums):
    i=1
    while(i<len(nums)):
        nums[i]=nums[i]+nums[i-1]
        i+=1
    return nums
nums=[1,1,1,1,1]
print(runningSum(nums))
