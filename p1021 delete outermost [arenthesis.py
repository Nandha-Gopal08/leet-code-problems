def out_parenthesis(s):
    s = list(s)
    count = 0
    res = []
    for i in range(len(s)):
        if(s[i] == "("):
            if count > 0:
                res.append(s[i])
            count += 1
        elif(s[i] == ")"):
            count -= 1
            if count > 0:
                res.append(s[i])
    return "".join(res)
s = "(()())(())"
print(out_parenthesis(s))
