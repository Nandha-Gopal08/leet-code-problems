def permutation(nums):
    nums.sort()
    final_op=[]
    used=[False]*len(nums)
    def backtrack(c,r):
        if not r:
            final_op.append(c)
            return
        seen=set()
        for i in range(len(r)):
            if r[i] in seen:
                continue
            seen.add(r[i])
            nc=c+[r[i]]
            nr=r[:i]+r[i+1:]
            backtrack(nc,nr)
    backtrack([],nums)
    return final_op
    
nums = [1,1,2]
print(permutation(nums))
