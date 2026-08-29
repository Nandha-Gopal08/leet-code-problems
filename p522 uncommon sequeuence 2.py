def findLUSlength(strs):
    def isSubsequence(a, b):
        i = 0

        for ch in b:
            if i < len(a) and a[i] == ch:
                i += 1
        return i == len(a)
    ans = -1

    for i in range(len(strs)):
        uncommon = True
            
        for j in range(len(strs)):
            print(i,j)
            if i == j:
                continue

            if isSubsequence(strs[i], strs[j]):
                uncommon = False
                break

        if uncommon:
            ans = max(ans, len(strs[i]))
        
    return ans
strs = ["aba", "cdc", "eae"]
print(findLUSlength(strs))
