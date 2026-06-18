x="0-1"
x=x.strip()
n=""
sign=1
if x and x[0] in "+-":
    if x[0]=="-":
        sign=-1
    x=x[1:]
for ch in x:
    if ch.isdigit():
        n+=ch
    else:
        break
if n=="":
    print(0)
else:
    print(sign*int(n))
        

    
