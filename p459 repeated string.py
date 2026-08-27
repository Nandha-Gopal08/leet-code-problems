def repeat(s):
    for i in range(1,len(s)):
        if len(s)%i==0:
            sub=s[:i]
            if sub*(len(s)//i) == s:
                return True
    return False
s = "abab"
print(repeat(s))
    
