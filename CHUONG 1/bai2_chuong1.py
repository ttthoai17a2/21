class TS:
    def __init__(self, ho_ten, diem_toan, diem_ly, diem_hoa):
        self.ho_ten = ho_ten
        self.diem_toan = diem_toan
        self.diem_ly = diem_ly
        self.diem_hoa = diem_hoa

    def tinh_tong_diem(self):
        return self.diem_toan + self.diem_ly + self.diem_hoa

    def in_thong_tin(self):
        print(f"Họ tên: {self.ho_ten}")
        print(f"Điểm Toán: {self.diem_toan}, Điểm Lý: {self.diem_ly}, Điểm Hóa: {self.diem_hoa}")
        print(f"Tổng điểm: {self.tinh_tong_diem()}")

def nhap_danh_sach_thi_sinh():
    danh_sach = []
    so_thi_sinh = int(input("Nhập số lượng thí sinh: "))
    for i in range(so_thi_sinh):
        ho_ten = input("Nhập họ tên thí sinh: ")
        diem_toan = float(input("Nhập điểm Toán: "))
        diem_ly = float(input("Nhập điểm Lý: "))
        diem_hoa = float(input("Nhập điểm Hóa: "))
        thi_sinh = TS(ho_ten, diem_toan, diem_ly, diem_hoa)
        danh_sach.append(thi_sinh)
    return danh_sach

def hien_thi_thi_sinh_trung_tuyen(danh_sach, diem_chuan=20):
    # Lọc danh sách thí sinh có tổng điểm >= điểm chuẩn và sắp xếp theo tổng điểm giảm dần
    danh_sach_trung_tuyen = sorted([ts for ts in danh_sach if ts.tinh_tong_diem() >= diem_chuan], 
                                   key=lambda ts: ts.tinh_tong_diem(), reverse=True)
    
    if not danh_sach_trung_tuyen:
        print("Không có thí sinh nào trúng tuyển.")
    else:
        print("\nDanh sách thí sinh trúng tuyển:")
        for ts in danh_sach_trung_tuyen:
            ts.in_thong_tin()
            print("-" * 20)


danh_sach = nhap_danh_sach_thi_sinh()
hien_thi_thi_sinh_trung_tuyen(danh_sach)
