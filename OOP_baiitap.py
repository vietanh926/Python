class Classroom:
    def __init__(self,name):
        self.name = name 
        self.student = []
        self.teacher = []
        self.gpa = []
    def add_student(self,student_name):
        self.student.append(student_name)
    
    def add_teacher(self,teacher_name):
        self.teacher.append(teacher_name)
    
    def info(self):
        print(f"Lớp {self.name}")
        print(f"Học sinh {', '.join(self.student) if self.student else 'chưa có'}")
        print(f"Giáo viên {', '.join(self.teacher) if self.teacher else 'chưa có'}")

class School:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.classes = {}

    def add_class(self, class_name):
        if class_name not in self.classes:
            self.classes[class_name] = Classroom(class_name)
        else:
            print(f"Lớp {class_name} đã tồn tại!")

    def remove_class(self, class_name):
        if class_name in self.classes:
            del self.classes[class_name]
        else:
            print(f"Lớp {class_name} không tồn tại!")

    def show_school_info(self):
        print(f"Trường: {self.name} - Địa chỉ: {self.address}")
        print("Danh sách lớp học:")
        for classroom in self.classes.values():
            classroom.info()
            print("-" * 30)

my_school = School("Trường THPT ABC", "123 Đường XYZ")

my_school.add_class("10A1")
my_school.add_class("10A2")

my_school.classes["10A1"].add_student("Nguyễn Văn A")
my_school.classes["10A1"].add_student("Trần Thị B")
my_school.classes["10A1"].add_teacher("Cô Hoa")

my_school.show_school_info()

