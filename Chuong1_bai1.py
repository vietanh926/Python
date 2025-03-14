is_log_in = False 

def require_login(func):  # Decorator nhận một hàm cần kiểm tra
    def wrapper(name):  # Nhận tham số của hàm gốc
        if is_log_in:  # Kiểm tra trạng thái đăng nhập
            return func(name)  # Gọi hàm gốc nếu đã đăng nhập
        else:
            print("Bạn cần đăng nhập trước!")  # Chặn truy cập nếu chưa đăng nhập
    return wrapper  # Trả về phiên bản mới của hàm

        


@require_login 
def view_dashboard(name):
    print(f'Chào mừng bạn đến với bảng điều khiển {name}')
    


view_dashboard('Việt')

is_log_in = True

view_dashboard('Việt')