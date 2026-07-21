def missing(nums):
    n=len(nums)
    sumn=(n*(n+1))//2
    return sumn - sum(nums)
nums=[9,6,4,2,3,5,7,0,1]
print(missing(nums))
