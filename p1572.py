def diagonal_sum(mat):
    i=0
    j=len(mat[0])-1
    add=0
    if(len(mat)==1):
        return mat[0][0]
    while(i<len(mat)):
        if(i==j):
            add=add+mat[i][j]
        else:
            add=add+mat[i][i]+mat[i][j]
        i+=1
        j-=1
    return add
mat = [[5]]
print(diagonal_sum(mat))
