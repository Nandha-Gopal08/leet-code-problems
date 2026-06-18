def permutation(numsd):
    final_op=[]

    def backtrack(current,rem):
        if len(rem)==0:
            final_op.append(current)
            return
        for i in range(len(rem)):
            new_curr=current +[rem[i]]
            new_rem = rem[:i]+rem[i+1:]
            backtrack(new_curr,new_rem)
    backtrack([],nums)
    return final_op

nums = [1,2,3]
print(permutation(nums))
