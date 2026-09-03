def large_group(s):
    answer = []
    start = 0

    for i in range(1,len(s)):
        if i == len(s) or s[i] != s[i-1]:
            if i - start >= 3:
                answer.append([start,i-1])
            start = i
    return answer
s = "aaa"
print(large_group(s))
