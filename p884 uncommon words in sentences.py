def uncommon_word(s1,s2):
    words = s1.split() + s2.split()

    count = {}

    for word in words:
        if word in count :
            count[word] += 1
        else:
            count[word] = 1
    result = []
    for word in count:
        if count[word] == 1:
            result.append(word)
    return result
s1 = "this apple is sweet"
s2 = "this apple is sour"
print(uncommon_word(s1,s2))
