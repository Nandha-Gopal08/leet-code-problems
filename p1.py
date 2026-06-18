l1=[2,4,3]
l2=[5,6,4]
carry=0
result=[]
if len(l1)==len(l2):
    for i in range(len(l1)-1,-1,-1):
        c=l1[i]+l2[i]+carry
        carry=c//10
        result=c%10
        print(result)
            
            
