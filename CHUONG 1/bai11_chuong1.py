import math
class TamGiac:
    def __init__(self, a, b, c):
        self.a = a  
        self.b = b  
        self.c = c  

    
    def is_valid(self):
        return (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a)

    
    def chu_vi(self):
        return self.a + self.b + self.c

    
    def dien_tich(self):
        if not self.is_valid():
            return None
        s = self.chu_vi() / 2 
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))  
    
    def hien_thi(self):
        return "Tam giác với các cạnh a={}, b={}, c={}".format(self.a, self.b, self.c)


class TamGiacCan(TamGiac):
    def __init__(self, a, b):
        super().__init__(a, b, a) 
   
    def hien_thi_can(self):
        return "Tam giác cân với cạnh đáy b={} và cạnh bên a={}".format(self.b, self.a)


class TamGiacVuong(TamGiac):
    def __init__(self, canh_a, canh_b):
        super().__init__(canh_a, canh_b, math.sqrt(canh_a**2 + canh_b**2))  

   
    def hien_thi_vuong(self):
        return "Tam giác vuông với các cạnh a={}, b={}, c={}".format(self.a, self.b, self.c)


class TamGiacDeu(TamGiacCan):
    def __init__(self, canh):
        super().__init__(canh, canh) 
   
    def hien_thi_deu(self):
        return "Tam giác đều với cạnh a={}".format(self.a)




tam_giac = TamGiac(3, 4, 5) 
if tam_giac.is_valid():
    print(tam_giac.hien_thi())
    print("Chu vi tam giác: {}".format(tam_giac.chu_vi()))
    print("Diện tích tam giác: {:.2f}".format(tam_giac.dien_tich()))
else:
    print("Tam giác không hợp lệ.")


tam_giac_can = TamGiacCan(5, 4)  
print(tam_giac_can.hien_thi_can())
print("Chu vi tam giác cân: {}".format(tam_giac_can.chu_vi()))
print("Diện tích tam giác cân: {:.2f}".format(tam_giac_can.dien_tich()))

tam_giac_vuong = TamGiacVuong(3, 4)  
print(tam_giac_vuong.hien_thi_vuong())
print("Chu vi tam giác vuông: {}".format(tam_giac_vuong.chu_vi()))
print("Diện tích tam giác vuông: {:.2f}".format(tam_giac_vuong.dien_tich()))


tam_giac_deu = TamGiacDeu(6)  
print(tam_giac_deu.hien_thi_deu())
print("Chu vi tam giác đều: {}".format(tam_giac_deu.chu_vi()))
print("Diện tích tam giác đều: {:.2f}".format(tam_giac_deu.dien_tich()))
