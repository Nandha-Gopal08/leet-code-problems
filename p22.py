nums=[1,3,5,6]
target=2
l=0
r=len(nums)-1
while l<=r:
    mid=(l+r)//2
    if(nums[mid]==target):
        print(i)
    elif nums[mid]<target:
        l=mid+1
    else:
        r=mid-1
    
print(l)
    
