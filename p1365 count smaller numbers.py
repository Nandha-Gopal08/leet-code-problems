def count(nums):
    ans=[]
    for i in range(len(nums)):
        count=0
        for j in range(len(nums)):
            if(nums[j]<nums[i]):
                count+=1
        ans.append(count)
    return ans
            
nums = [5,5,5]
print(count(nums))
