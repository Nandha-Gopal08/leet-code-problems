def image(img):
    n=len(img)
    m=len(img[0])
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            total=0
            count=0
            for x in range(i-1,1+2):
                for y in range(j-1,j+2):
                    if 0<=x<n and 0<=y<m:
                        total += img[x][y]
                        count += 1
            result[i][j] = total//count
    return result
            
img=[[1,1,1],[1,0,1],[1,1,1]]
print(image(img))
