def digit(digits):
    for i in range(len(digits)-1,0,-1):
        if(digits[i]+1<10):
            digits[i]+=1
            return digits
        else:
            digits[i]=0
    digits=[1]+[0]*len(digits)
    return digits
digits=[9,9]
print(digit(digits))
