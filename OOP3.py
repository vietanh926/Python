class Animal:
    def __init__(self,name):
        self.name = name 
    def speak(self):
        print(f'{self.name} speaks')

class Dog(Animal):
    def __init__(self,name):
        super().__init__(name)
    
    def bark(self):
        print(f'{self.name} barks')
    
class Bulldog(Dog):
    def __init__(self,name):
        super().__init__(name)
    def guard(self):
        print(f'{self.name} guards the house')       
        
        
dog = Bulldog("Buddy")
dog.speak()
dog.bark()
dog.guard()

#Tính đóng gói 
class Car:
    def __init__(self, name, mileage):
        self._name = name # Protected variable (theo quy ước)
        self.mileage = mileage
    def description(self):
        return f"The {self._name} car gives the mileage of {self.mileage} km/l"

obj = Car("BMW 7-series", 39.53)
# Truy cập thuộc tính bảo vệ thông qua phương thức lớp
print(obj.description()) # The BMW 7-series car gives the mileage of 39.53km/l
# Truy cập trực tiếp thuộc tính bảo vệ từ bên ngoài (vẫn hoạt động)
print(obj._name) # BMW 7-series (vẫn truy cập được)
print(obj.mileage) # 39.53 (thuộc tính public)


