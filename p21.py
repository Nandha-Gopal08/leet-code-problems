haystack="hello"
needle="p"
check=""
f=False
for i in range(len(haystack)-len(needle)+1):
    check=""
    for j in range(len(needle)):
        if haystack[i+j]==needle[j]:
            check+=haystack[i+j]
        else:
            break
    if check==needle:
        print(i)
        f=True
        break
    
if not f:
    print(-1)
print("executed")
            
