class NhanVien:
    def __init__(self,ho_ten,luong_co_ban):
        self.ho_ten = ho_ten
        self.luong_co_ban = luong_co_ban
    def tinh_luong(self):
        return self.luong_co_ban
class NhanVienVanPhong(NhanVien):
    def __init__(self,ho_ten,luong_co_ban,thuong):
        super().__init__(ho_ten,luong_co_ban)
        self.thuong = thuong
    def tinh_luong(self):
        return super().tinh_luong() + self.thuong

class NhanVienSanXuat(NhanVien):
    def __init__(self,ho_ten,luong_co_ban,so_san_pham):
        super().__init__(ho_ten,luong_co_ban)
        self.so_san_pham = so_san_pham
    def tinh_luong(self):
        return super().tinh_luong() + self.so_san_pham * 5000



nhan_vien_van_phong1 = NhanVienVanPhong('Nguyễn Văn T',100000000,500000)
print(nhan_vien_van_phong1.tinh_luong()) 
nhan_vien_san_xuat1 = NhanVienSanXuat('Trân Văn B',2500000,10000)
print(nhan_vien_san_xuat1.tinh_luong())