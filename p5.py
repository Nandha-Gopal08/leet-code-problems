s=input("enter a string ")
if len(s) <= 1:
    print(s)

start = 0
max_len = 1

for i in range(len(s)):

    # Odd length
    l, r = i, i
    while l >= 0 and r < len(s) and s[l] == s[r]:
        if r - l + 1 > max_len:
            start = l
            max_len = r - l + 1
        l -= 1
        r += 1

    # Even length
    l, r = i, i + 1
    while l >= 0 and r < len(s) and s[l] == s[r]:
        if r - l + 1 > max_len:
            start = l
            max_len = r - l + 1
        l -= 1
        r += 1

print(s[start:start + max_len])
