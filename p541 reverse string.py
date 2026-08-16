def reverseStr(s, k):
    s = list(s)

    for i in range(0, len(s), 2 * k):
        s[i:i+k] = reversed(s[i:i+k])

    return ''.join(s)


s = "abcdefg"
k = 2

print(reverseStr(s, k))
