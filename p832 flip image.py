def flip(image):
    for row in image:
        row.reverse()
        for i in range(len(row)):
            if row[i] == 0:
                row[i]=1
            else:
                row[i]=0
    return image
image = [[1,1,0],[1,0,1],[0,0,0]]
print(flip(image))
