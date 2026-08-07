def rel_arr(arr1,arr2):
    res=[]
    for i in range(len(arr2)):
        for j in range(len(arr1)):
            if(arr1[j]==arr2[i]):
                res.append(arr1[j])
    rem=[]
    for x in arr1:
        if x not in arr2:
            rem.append(x)
    rem.sort()
    for y in rem:
        res.append(y)
    return res
arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
print(rel_arr(arr1,arr2))
