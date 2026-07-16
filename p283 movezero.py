def move(nums):
    move=0
    for i in range(len(nums)):
        if(nums[i]!=0):
            temp=nums[move]
            nums[move]=nums[i]
            nums[i]=temp
            move+=1
    return nums

nums = [0]
print(move(nums))
