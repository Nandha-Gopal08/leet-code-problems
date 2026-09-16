def comm_char(words):
    res = []
    for ch in set(words[0]):
        count = min(word.count(ch) for word in words)

        for i in range(count):
            res.append(ch)
    return res
words = ["bella","label","roller"]
print(comm_char(words))
