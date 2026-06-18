nums=[1,1,2]
count=1
print(nums)
for i in range(len(nums)):
    for j in range(i+1,len(nums)-1):
        if(nums[i]!=nums[j]):
            count+=1
            nums[i]=nums[j]
            nums[j]="_"
            
total=len(nums)-count
print(nums[:count])
print(total)
