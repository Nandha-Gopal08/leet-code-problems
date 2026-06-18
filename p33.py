def jump(nums):
    jump=0
    CE=0
    F=0
    for i in range(len(nums)-1):
        F=max(F,i+nums[i])
        if(i==CE):
            jump+=1
            CE=F
    return jump
        
nums = [2,3,1,1,4]
print(jump(nums))
