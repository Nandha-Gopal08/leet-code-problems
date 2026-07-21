class numarray(object):
    def __init__ (self,nums):
        self.nums=nums
    def sumrange(self,left,right):
        total=0
        while(left<=right):
            total+=self.nums[left]
            left+=1
        return total
numarray=numarray([-2,0,3,-5,2,-1])
print(numarray.sumrange(0,2))
print(numarray.sumrange(2,5))
print(numarray.sumrange(0,5))
print(numarray.sumrange(0,5))
                
