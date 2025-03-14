class ClassName:
    # Định nghĩa class
    
    pass

# class Student: #Tên class  
#     name = '' 
#     grade = None
#     #Name và grade là thuộc tính , '' và None là giá trị tương ứng 
    
#Đối tượng 
objectName = ClassName() # Đây là 1 đối tượng 
# Ví dụ 

class Student:
    name = "Việt Anh"
    grade = 'Năm 4 ĐH'

student1 = Student()

student1.name = "Anh"
student1.grade = 12
print(student1.name,student1.grade) 


class Employee:
    employee_id = 0
# Khởi tạo 2 đối tượng từ lớp Employee
employee1 = Employee()
employee2 = Employee()
# Truy xuất thuộc tính của employee1
employee1.employeeID = 1001
print(f"Employee ID: {employee1.employeeID}")

#Instante Method 
class Person1:
    n = 1 
    def __init__(self,name,age):
        self.name = name 
        self.age = age
    def introduce(self):
        return f'Xin chào tôi tên là {self.name}, {self.age} lần làm việc thứ {self.n}'
    
p1 = Person1("Việt",21)
print(p1.introduce())


#Class method 
class Person2:
    total = 0
    def __init__(self,name):
        self.name = name 
        Person2.total += 1 
    @classmethod
    def get_total(cls):
        return f"Hiện có {cls.total} người"

p2 = Person2("Nam")
p2 = Person2('Linh')
print(Person2.get_total())


#Static Method 
class MathUnit:
    @staticmethod
    def add(x,y):
        return x+y
    @staticmethod
    def mutiply(x,y):
        return x*y

print(MathUnit.add(2,3))
print(MathUnit.mutiply(2,3))


#Tính kế thừa
class Animal:
    name = ""
    def eat(self):
        print('I can eat')


class Dog(Animal):
    def display(self):
        print('Tên tôi là :',self.name)
    

dog = Dog()
dog.name = "Nick"
dog.eat()
dog.display()