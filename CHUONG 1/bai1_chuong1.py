class hinhchunhat:
    def __init__(self, chieu_dai=0, chieu_rong=0):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong

    def nhap_du_lieu(self):
        self.chieu_dai = float(input("Nhập chiều dài: "))
        self.chieu_rong = float(input("Nhập chiều rộng: "))

    def chu_vi(self):
        return 2 * (self.chieu_dai + self.chieu_rong)

    def dien_tich(self):
        return self.chieu_dai * self.chieu_rong

    def thong_tin(self):
        chu_vi = self.chu_vi()
        dien_tich = self.dien_tich()
        print(f"hcn có chiều dài: {self.chieu_dai}, chiều rộng: {self.chieu_rong}")
        print(f"Chu vi: {chu_vi}")
        print(f"Diện tích: {dien_tich}")

hcn= hinhchunhat()
hcn.nhap_du_lieu()
hcn.thong_tin()