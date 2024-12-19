class DaGiac:
    def __init__(self, so_canh, do_dai_canh):
        self.so_canh = so_canh                      
        self.do_dai_canh = do_dai_canh              

   
    def chu_vi(self):
        return sum(self.do_dai_canh)               

class HinhBinhHanh(DaGiac):
    def __init__(self, day, canh_ben, chieu_cao):
        super().__init__(4, [day, canh_ben, day, canh_ben])  
        self.chieu_cao = chieu_cao                          

    
    def dien_tich(self):
        return self.do_dai_canh[0] * self.chieu_cao          


class HinhChuNhat(HinhBinhHanh):
    def __init__(self, chieu_dai, chieu_rong):
        super().__init__(chieu_dai, chieu_rong, chieu_rong)  

    
    def dien_tich(self):
        return self.do_dai_canh[0] * self.do_dai_canh[1]     


class HinhVuong(HinhChuNhat):
    def __init__(self, canh):
        super().__init__(canh, canh)                         

    
    def dien_tich(self):
        return self.do_dai_canh[0] ** 2                      



print("Đa giác:")
dagiac = DaGiac(3, [3, 4, 5])  
print("Chu vi đa giác: {}".format(dagiac.chu_vi()))


print("\nHình bình hành:")
hinh_binh_hanh = HinhBinhHanh(6, 4, 5) 
print("Chu vi hình bình hành: {}".format(hinh_binh_hanh.chu_vi()))
print("Diện tích hình bình hành: {}".format(hinh_binh_hanh.dien_tich()))

# Hình chữ nhật
print("\nHình chữ nhật:")
hinh_chu_nhat = HinhChuNhat(5, 3)  
print("Chu vi hình chữ nhật: {}".format(hinh_chu_nhat.chu_vi()))
print("Diện tích hình chữ nhật: {}".format(hinh_chu_nhat.dien_tich()))

# Hình vuông
print("\nHình vuông:")
hinh_vuong = HinhVuong(4)  
print("Chu vi hình vuông: {}".format(hinh_vuong.chu_vi()))
print("Diện tích hình vuông: {}".format(hinh_vuong.dien_tich()))
