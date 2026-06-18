def position(nums,target):
    right=-1
    left=-1
    for i in range(len(nums)):
        if nums[i]==target :
            if left==-1:
                left=i
            right=i
    return [left,right]
nums = [5,7,7,8,8,10]
target = 8
print(position(nums,target))
