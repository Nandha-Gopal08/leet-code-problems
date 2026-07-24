def disappear(nums):
    num_set=set(nums)
    res=[]
    for number in range(1,len(nums)+1):
        if number not in num_set:
            res.append(number)
    return res
nums=[4,3,2,7,8,2,3,1]
print(disappear(nums))
