def title(columNumber):
    res=""
    while columNumber > 0:
        columNumber-=1
        remainder = columNumber % 26
        res+=chr(remainder+ord('A'))
        columNumber//=26
    return res[::-1]
columNumber = 709
print(title(columNumber))
