keyboard={"2":"abc",
          "3":"def",
          "4":"ghi",
          "5":"jkl",
          "6":"mno",
          "7":"pqrs",
          "8":"tuv",
          "9":"wxyz"
          }
digits=input("enter a digit :   ")
result=[""]
for d in digits:
    temp=[]
    for combo in result:
        for ch in keyboard[d]:
            temp.append(combo+ch)
    result=temp
print(result)
          
