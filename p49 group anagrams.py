def group(strs):
    res=[]
    visited=[False]*len(strs)

    for i in range(len(strs)):
        if(visited[i]):
            continue
        group=[strs[i]]
        for j in range(i+1,len(strs)):
            if(sorted(strs[i])==sorted(strs[j])):
                group.append(strs[j])
                visited[j]=True
        res.append(group)
    return res
    


strs = ["eat","tea","tan","ate","nat","bat"]
print(group(strs))
