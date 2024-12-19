import json
from datetime import datetime


danh_sach_giao_dich = []


def them_giao_dich():
    loai_giao_dich = input("Nhập loại giao dịch (tiền/vàng): ")
    so_luong = float(input("Nhập số lượng: "))
    danh_sach_giao_dich.append({"loai": loai_giao_dich, "so_luong": so_luong})


while True:
    them_giao_dich()
    tiep_tuc = input("Bạn có muốn thêm giao dịch nữa không? (y/n): ")
    if tiep_tuc.lower() != 'y':
        break


ghi = input("Bạn có muốn ghi vào tập tin không? (1: Có, 0: Không): ")
if ghi == '1':
    
    thoi_gian_hien_tai = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    ten_tap_tin = f"{thoi_gian_hien_tai}.json"
    
    
    with open(ten_tap_tin, "w", encoding="utf-8") as file:
        json.dump(danh_sach_giao_dich, file, ensure_ascii=False, indent=4)
    
    print(f"Đã ghi vào tệp {ten_tap_tin}")
else:
    print("Không ghi vào tệp.")
