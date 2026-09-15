def alien_language(words,order):
    rank = {}
    for i in range(len(order)):
        rank[order[i]] = i

    for i in range(len(words) - 1):
        word1 = words[i]
        word2 = words[i + 1]

        j = 0

        while j < len(word1) and j < len(word2):
            if rank[word1[j]] < rank[word2[j]]:
                break
            elif rank[word1[j]] > rank[word2[j]]:
                return False


            j += 1
        if j == len(word2) and j < len(aord1):
            return False

    return True
words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
print(alien_language(words,order))
