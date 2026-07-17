class ParkingSystem(object):

    def __init__(self, big, medium, small):
        self.count = [0, big, medium, small]

    def addCar(self, carType):
        if self.count[carType] > 0:
            self.count[carType] -= 1
            return True
        return False
obj = ParkingSystem(1, 1, 0)

print(obj.addCar(1))  
print(obj.addCar(2))  
print(obj.addCar(3))  
print(obj.addCar(1)) 
