def buddy(s,goal):
    if len(s) != len(goal):
        return False

    if s == goal:
        print(len(set(s) < len(s)))
    diff = []

    for i in range(len(s)):
        if s[i] != goal[i]:
            diff.append(i)

    if len(diff) != 2:
        return False

    i = diff[0]
    j = diff[1]

    return s[i] == goal[j] and s[j] == goal[i]
s = "ab"
goal = "ba"
print(buddy(s,goal))
