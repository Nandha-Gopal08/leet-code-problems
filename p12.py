nums=[-1,0,1,2,-1,-4]
num=[]
for i in range(len(nums)):
    for j in range(len(nums)):
        for k in range(len(nums)):
            if(i !=j and i !=k and j !=k):
                if nums[i]+nums[j]+nums[k]==0:
                    tri=[nums[i],nums[j],nums[k]]
                    tri.sort()
                    if tri not in num:
                        num.append(tri)
                    
                
print(num)
            

