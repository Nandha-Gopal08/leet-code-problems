def max_circular_subarray(nums):
    current_max = nums[0]
    max_ans = nums[0]

    current_min = nums[0]
    min_ans = nums[0]

    total = 0
    for num in nums:
        total += num
        current_max = max(num,num+current_max)
        max_ans = max(max_ans,current_max)
        current_min = min(num,num + current_min)
        min_ans = min(min_ans,current_min)
    circular_ans = total - min_ans
    if max_ans < 0:
        return max_ans
    return max(max_ans,circular_ans)
nums = [1,-2,3,-2]
print(max_circular_subarray(nums))
