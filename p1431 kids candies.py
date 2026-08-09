def kids_candies(candies,extraCandies):
    m_c=max(candies)
    res=[]
    for i in range(len(candies)):
        if(candies[i]+extraCandies >= m_c):
            res.append(True)
        else:
            res.append(False)
    return res
candies = [2,3,5,1,3]
extraCandies = 3
print(kids_candies(candies,extraCandies))
