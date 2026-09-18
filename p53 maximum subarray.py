def max_subarray(nums):
    final_ans = nums[0]
    prev_ans = 0
    for i in range(len(nums)):
        current_sum = max(nums[i],nums[i] + prev_ans)
        prev_ans = current_sum
        if prev_ans > final_ans:
            final_ans = prev_ans
    return final_ans
            
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(max_subarray(nums))
