def buildarray(nums):
    ans=[]
    for i in range(len(nums)):
        ans.append(nums[nums[i]])
    return ans
nums = [0,2,1,5,3,4]
print(buildarray(nums))
