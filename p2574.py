def left_right_diff(nums):
    leftsum = [0]*len(nums)
    rightsum = [0]*len(nums)
    answer = []

    for i in range(1,len(nums)):
        leftsum[i] = (leftsum[i-1]+ nums[i-1])
    for i in range(len(nums)-2,-1,-1):
        rightsum[i] = (rightsum[i+1]+nums[i+1])
    for i  in range(len(nums)):
        answer.append(abs(leftsum[i]-rightsum[i]))
    return answer
    
nums = [1]
print(left_right_diff(nums))
