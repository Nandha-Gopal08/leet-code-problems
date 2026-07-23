def third(nums):
    temp=list(set(nums))
    temp.sort(reverse=True)
    if len(nums)>=3:
        return temp[2]
    else:
        return temp[0]
nums = [3,2,2,1]
print(third(nums))
