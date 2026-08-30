def common_min(jewels,stones):
    count=0
    for ch in stones:
        if ch in jewels:
            count+=1
    return count
jewels = "z"
stones = "ZZ"
print(common_min(jewels,stones))
