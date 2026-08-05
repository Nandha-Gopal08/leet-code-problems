def parity(nums):
    res=[]
    even=[]
    odd=[]
    if(len(nums)==1):
        return nums
    for i in range(len(nums)):
        if(nums[i]%2==0):
            even.append(nums[i])
        else:
            odd.append(nums[i])
    for j in range(len(even)):
        res.append(even[j])
    for k in range(len(odd)):
        res.append(odd[k])
    return res
            
nums=[0]
print(parity(nums))
