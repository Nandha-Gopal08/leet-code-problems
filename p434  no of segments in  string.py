def segments(s):
    words=s.split()
    count = 0
    for ch in words:
        count += 1
    return count
s = "Hello, my name is John"
print(segments(s))
