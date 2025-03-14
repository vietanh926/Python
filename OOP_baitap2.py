class BankAccount:
    def __init__(self,account_number:int,owner:str,balance = 0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
    
    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print(f'Đã nạp vào {amount}, số tiền hiện tại {self.balance}')
        else: 
            print('Không thể nạp tiền vào')
    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f'Đã rút {amount}')
        else:
            print('Không thể rút tiền')
    def show_balance(self):
        print(f'Số dư hiện tại {self.balance}') 
    
    def show_info(self):
        print(f'Id: {self.account_number}, Tên: {self.owner}, Số dư: {self.balance}')


person1 = BankAccount(123,"Nguyen Van A",1000)
person1.show_info()
person1.deposit(100)    
person1.withdraw(1200)
person1.show_balance()