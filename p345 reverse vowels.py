def vowels(s):
    vowels="AEIOUaeiou"
    s=list(s)
    left=0
    right=len(s)-1
    while left<=right:
        if s[left] in vowels and s[right]not in vowels:
            right -=1
        elif s[right] in vowels and s[left] not in vowels:
            left+=1
        elif s[left] in vowels and s[right] in vowels:
            s[left],s[right]=s[right],s[left]
            right-=1
            left+=1
        else:
            right-=1
            left+=1
    return "".join(s)
s = "IceCreAm"
print(vowels(s))
