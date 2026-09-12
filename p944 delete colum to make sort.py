def delete_colum(strs):
    count = 0
    for i in range(len(strs[0])):
        left = 0
        right = 1
        while(right < len(strs)):
            if strs[left][i] > strs[right][i]:
                count += 1
                break

            left += 1
            right += 1
    return count
strs = ["cba","daf","ghi"]
print(delete_colum(strs))
