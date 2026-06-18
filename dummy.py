
x=int(input("enter a number"))
rev=0
if x<0:
    s=str(x)
    rev=int(str(x)[1:][::-1]) * -1
print(rev)
