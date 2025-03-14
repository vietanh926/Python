#Ghi đè phương thức 
class Animal:
    name = ""
    def eat(self):
        print("Tôi có thể ăn")


class Dog(Animal):
    #Ghi đè 
    def eat(self):
        #Hàm super
        super().eat()
        print("Tôi thích ăn xương")
    

dog = Dog()
dog.eat()

#Đa kế thừa 
class Person():
    def info(self):
        print("Info a person")

class Employee():
    def showSalary(self):
        print("Salary of an Employee")

class Teacher(Person, Employee):
    pass



Alice = Teacher()
Alice.info()
Alice.showSalary()    