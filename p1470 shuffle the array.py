def shuffle(nums,n):
    rs=[]
    j=n
    for i in range(n):
        rs.append(nums[i])
        rs.append(nums[j])
        j+=1
    return rs
nums = [2,5,1,3,4,7]
n = 3
print(shuffle(nums,n))
