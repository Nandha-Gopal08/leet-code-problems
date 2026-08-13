def lowercase(s):
    res=""
    for x in s:
        if x.isupper():
            res+=x.lower()
        else:
            res+=x
    return res
s = "Hello"
print(lowercase(s))
