class Rectangle:
    def __init__(self,width:int,height:int):
        self.width = width 
        self.height = height
        self.s = 0 
        self.c = 0

    def area(self):
        self.s = self.width*self.height
        print( f'Diện tích hình chữ nhật:{self.s}')
    def perimeter(self):
        self.c = (self.width+self.height)*2
        print(f'Chu vi hình chữ nhật:{self.c}')

    def show_info(self):
        print(f'Chiều dài {self.width} , chiều rộng :{self.height}')
        print(f'Diện tích hình chữ nhật {self.s}, chu vi hình chữ nhật {self.c}')

    
        

hcn1 = Rectangle(3,4)
hcn1.area()
hcn1.perimeter()
hcn1.show_info()
