def valid_anagram(s,t):
    s_check = {}
    t_check = {}
    for ch in s:
        if ch not in s_check:
            s_check[ch] = 1
        elif ch in s_check:
            s_check[ch] += 1
    for ch in t:
        if ch not in t_check:
            t_check[ch] = 1
        elif ch in t_check:
            t_check[ch] += 1
    return s_check == t_check
    
s = "rat"
t = "car"

print(valid_anagram(s,t))
