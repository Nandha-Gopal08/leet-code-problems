def mst_com_word(paragraph,banned):
    
    words = paragraph.lower()
    
    for ch in "!?',;.":
        words = words.replace(ch, " ")
        
    words = words.split()
    count = {}
    for w in words:
        if w not in  banned:
            if w in count:
                count[w] += 1
            else:
                count[w] = 1
    return max(count,key=count.get)
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print(mst_com_word(paragraph,banned))
