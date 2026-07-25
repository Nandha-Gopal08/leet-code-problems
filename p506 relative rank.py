def rank(nums):
    sort_nums=sorted(nums,reverse=True)
    rank={}
    for i in range(len(sort_nums)):
        if i==0:
            rank[sort_nums[i]]="Gold Medal"
        elif i==1:
            rank[sort_nums[i]]="Silver Medal"
        elif i==2:
            rank[sort_nums[i]]="Bronze Medal"
        else:
            rank[sort_nums[i]]=str(i+1)
    answer=[]

    for value in nums:
        answer.append(rank[value])
    return answer
            
nums=[10,3,8,9,4]
print(rank(nums))
