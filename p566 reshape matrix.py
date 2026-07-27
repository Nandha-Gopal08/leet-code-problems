def reshape(mat,r,c):
    m=len(mat)
    n=len(mat[0])
    if(m*n!=r*c):
        return mat
    res=[]
    elem=[]
    for row in mat:
        for value in row:
            elem.append(value)
    index=0
    for i in range(r):
        new_row=[]
        for j in range(c):
            new_row.append(elem[index])
            index+=1
        res.append(new_row)
    return res
mat=[[1,2],[3,4]]
r=1
c=4
print(reshape(mat,r,c))
