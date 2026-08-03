def index(nums):
    largest=max(nums)
    n=len(nums)
    count=0
    for i in range(n):
        if nums[i]!=largest and largest >= 2*nums[i]:
            count+=1
        if(nums[i]==largest):
            index=i
    if(count==n-1):
        return index
    else:
        return -1
        
nums=[1,2,3,4]
print(index(nums))
