def check_height(heights):
    expected=sorted(heights)
    count = 0
    for i in range(len(heights)):
        if (heights[i] != expected[i]):
            count+=1
    return count
heights = [1,2,3,4,5]
print(check_height(heights))
