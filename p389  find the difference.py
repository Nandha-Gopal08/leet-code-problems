def difference(s,t):
    for ch in t:
        if t.count(ch) != s.count(ch):
            return ch
s = "a"
t = "aa"
print(difference(s,t))
