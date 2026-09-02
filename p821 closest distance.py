def short_dist(s,c):
    answer = []
    for i in range(len(s)):
        min_dist = float('inf')
        
        for j in range(len(s)):
            if (s[j] == c):
                distance = abs(i-j)

                if distance < min_dist:
                    min_dist = distance
        answer.append(min_dist)
                
                
    return answer

s = "loveleetcode"
c = "e"
print(short_dist(s,c))
