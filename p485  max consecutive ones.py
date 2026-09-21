def max_consecutive_ones(nums):
    Max = 0
    count = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            count += 1

            if count > Max :
                Max = count
        else:
            count = 0
       
    
    return Max
        
nums = [1,1,0,1,1,1]
print(max_consecutive_ones(nums))
