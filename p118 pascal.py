def pascal(numRows):
    result=[[1]]
    if(numRows==1):
        return result[0]
    for i in range(numRows-1):
        temp=[0]+result[-1]+[0]
        temp_res=[]
        
        for j in range(len(temp)-1):
            temp_res.append(temp[j]+temp[j+1])
        result.append(temp_res)
    return result
numRows=int(input("enter no.of rows"))
print(pascal(numRows))
