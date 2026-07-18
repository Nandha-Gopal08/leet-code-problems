def duplicate(nums,k):
    seen={}
    for i in range(len(nums)):
        if(nums[i] in seen  and i-seen[nums[i]]<=k):
            return True
        seen[nums[i]]=i
    return False
nums=[1,2,3,1,2,3]
k=2
print(duplicate(nums,k))
