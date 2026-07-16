def single(nums):
    xor=0
    for i in range(len(nums)):
        xor^=nums[i]
    return xor
nums=[4,1,2,1,2,17,17]
print(single(nums))
