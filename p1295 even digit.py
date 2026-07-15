def even(nums):
    count=0
    for i in range(len(nums)):
        length=0
        while(nums[i]!=0):
            length+=1
            nums[i]//=10
        if(length%2==0):
            count+=1
    return count
        
nums=[12,345,2,6,7896]
print(even(nums))
