import math
class Diem:
    def __init__(self, x=0, y=0):
        self.x = x  
        self.y = y  

    
    def hien_thi(self):
        return "Điểm({},{})".format(self.x, self.y)


class Elip(Diem):
    def __init__(self, x, y, truc_lon, truc_nho):
        super().__init__(x, y)  
        self.truc_lon = truc_lon 
        self.truc_nho = truc_nho  

    
    def dien_tich(self):
        return math.pi * self.truc_lon * self.truc_nho  
    
    def hien_thi_elip(self):
        return "Elip có tọa độ tâm: {}, trục lớn: {}, trục nhỏ: {}, diện tích: {:.2f}".format(
            super().hien_thi(), self.truc_lon, self.truc_nho, self.dien_tich()
        )


class DuongTron(Elip):
    def __init__(self, x, y, ban_kinh):
        super().__init__(x, y, ban_kinh, ban_kinh) 
    
    def hien_thi_duong_tron(self):
        return "Đường tròn có tọa độ tâm: {}, bán kính: {}, diện tích: {:.2f}".format(
            super().hien_thi(), self.truc_lon, self.dien_tich()
        )


elip = Elip(0, 0, 5, 3)  
print(elip.hien_thi_elip())

duong_tron = DuongTron(2, 2, 4)  
print(duong_tron.hien_thi_duong_tron())
