str=["flower","flow","flight"]
cp=str[0]
for cpr in str:
    while not cpr.startswith(cp):
        cp=cp[:-1]
print(cp)
