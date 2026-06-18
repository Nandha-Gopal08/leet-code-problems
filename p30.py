def combination(candidates,target):
    result=[]

    def backtrack(start,path,target):
        if(target==0):
            result.append(path[:])
            return
        if(target < 0):
            return

        for i in range(start,len(candidates)):
            path.append(candidates[i])
            backtrack(i,path,target - candidates[i])
            path.pop()
    backtrack(0,[],target)
    return result
candidates = [2,3,6,7]
target = 7
print(combination(candidates,target))
            
        
