def countAndSay(n):
    if n==1:
        return "1"
    result = "1"
    prev=countAndSay(n-1)
    result=""
    count=1
    for j in range(len(prev)):
        if j + 1 < len(prev) and prev[j] == prev[j+1]:
            count += 1
        else:
            result += str(count) + prev[j]
            count = 1
    return result
n=int(input("enter the nth sequential of adigit"))
print(countAndSay(n))
    
    
    
