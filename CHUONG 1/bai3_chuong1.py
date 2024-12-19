import math

class PhanSo:
    def __init__(self, tu=0, mau=1):
        self.tu = tu
        if mau == 0:
            raise ValueError("Mẫu số không thể bằng 0.")
        self.mau = mau
        self.rut_gon()

    
    def hop_le(self):
        return self.mau != 0

    
    def nhap(self):
        self.tu = int(input("Nhập tử số: "))
        self.mau = int(input("Nhập mẫu số: "))
        if self.mau == 0:
            raise ValueError("Mẫu số không thể bằng 0.")
        self.rut_gon()

    
    def xuat(self):
        if self.mau == 1:
            print(f"{self.tu}")
        else:
            print(f"{self.tu}/{self.mau}")

    
    def rut_gon(self):
        ucln = math.gcd(self.tu, self.mau)
        self.tu = self.tu // ucln
        self.mau = self.mau // ucln
        if self.mau < 0: 
            self.tu = -self.tu
            self.mau = -self.mau


ps = PhanSo()
ps.nhap()
ps.xuat()
