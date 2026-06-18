def divide(dividend, divisor):
    if dividend== -2**31 and divisor==-1:
        return 2**31-1
    sign=-1 if(dividend<0) ^ (divisor<0) else 1
    count=0
    dividend=abs(dividend)
    divisor=abs(divisor)
    while(dividend>=divisor):
        dividend-=divisor
        count+=1
    return sign*count
dividend=int(input("enter dividend"))
divisor=int(input("enter divisor"))
print(divide(dividend,divisor))
