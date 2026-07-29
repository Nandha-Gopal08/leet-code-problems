def subavg(nums,k):
    left=0
    right=k
    final=sum(nums[left:right])
    cursum=final
    while(right<len(nums)):
        cursum=cursum-nums[left]+nums[right]
        if(cursum>final):
            final=cursum
        left+=1
        right+=1
    return final/k
            
nums=[1,12,-5,-6,50,3]
k=int(input("enter the number K:"))
print(subavg(nums,k))
