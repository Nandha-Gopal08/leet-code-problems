def replace_elem(arr):
    greatest=-1
    for i in range(len(arr)-1,-1,-1):
        cur = arr[i]
        arr[i] = greatest
        if(cur > greatest):
            greatest=cur
    return arr
arr = [1,2,3]
print(replace_elem(arr))
