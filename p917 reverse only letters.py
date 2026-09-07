def rev_let(s):
    s = list(s)
    left = 0
    right = len(s) - 1

    while(left <= right):
        if s[left].isalpha() and s[right].isalpha():
            s[left],s[right] = s[right],s[left]

            left += 1
            right -= 1
        elif s[left].isalpha():
            if s[right].isalpha():
                continue
            else:
                right -= 1
        else:
            left += 1
    return "".join(s)
            
s = "Test1ng-Leet=code-Q!"
print(rev_let(s))
