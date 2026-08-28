def license(s, k):
    s = s.replace("-", "").upper()
    
    result = ""
    count = 0
    
    for i in range(len(s) - 1, -1, -1):
        result = s[i] + result
        count += 1

        if count == k and i != 0:
            result = "-" + result
            count = 0

    return result


s = "5F3Z-2e-9-w"
k = 3

print(license(s, k))
