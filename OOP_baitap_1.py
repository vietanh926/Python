class Student:
    def __init__(self,name :str,student_id:int,gpa:float):
        self.name = name 
        self.student_id = student_id
        self.gpa = gpa 
    
    def show_info(self):
        return f"Student ID:{self.student_id} - Name:{self.name} - GPA:{self.gpa}"
        
        


hocsinh1 = Student('Nguyen Van A',123456,3.5)
hocsinh2 = Student('Nguyen Van B',678910,3.0)

print(hocsinh1.show_info())
print(hocsinh2.show_info())