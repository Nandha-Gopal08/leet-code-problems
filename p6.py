x=int(input("enter a number "))
rev=0
nrev=1
if  x.isdigit():
    while x>0:
        r=x%10
        rev=r+rev*10
        x=x//10
        print(r)
        print(rev)
        print(x)
    print(rev)
    while x<0:
        s=str(x)
        rev=int(str(x)[1:][::-1])
    print(rev)

        
