def rot_str(s,goal):
    if len(s) != len(goal):
        return False
    for i in range(len(s)):
        shift = s[i:] + s[:i]

        if shift == goal:
            return True
    return False
s = "abcde"
goal = "cdaeb"
print(rot_str(s,goal))
