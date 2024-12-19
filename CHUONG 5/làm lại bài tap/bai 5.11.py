import sqlite3

# Kết nối đến cơ sở dữ liệu SQLite (ql_nhan_vien.db)
connection = sqlite3.connect('ql_nhan_vien.db')
cursor = connection.cursor()

# Tạo bảng 'PHONG' nếu chưa tồn tại
cursor.execute("""
    CREATE TABLE IF NOT EXISTS PHONG (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        amount INTEGER NOT NULL
    );
""")

# Tạo bảng 'NHAN_VIEN' với khóa ngoại tham chiếu đến bảng 'PHONG'
cursor.execute("""
    CREATE TABLE IF NOT EXISTS NHAN_VIEN (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ho_ten TEXT NOT NULL,
        tuoi INTEGER NOT NULL,
        dia_chi TEXT NOT NULL,
        luong REAL NOT NULL,
        id_phong INTEGER,
        FOREIGN KEY (id_phong) REFERENCES PHONG(id)
    );
""")

connection.commit()

print("Cơ sở dữ liệu và bảng đã được tạo thành công.")

# Hàm thêm phòng ban vào bảng PHONG
def add_phong(name, price, amount):
    cursor.execute("INSERT INTO PHONG (name, price, amount) VALUES (?, ?, ?);", (name, price, amount))
    connection.commit()
    print(f"Phòng ban '{name}' đã được thêm vào!")

# Hàm thêm nhân viên vào bảng NHAN_VIEN
def add_nhan_vien(ho_ten, tuoi, dia_chi, luong, id_phong):
    cursor.execute("INSERT INTO NHAN_VIEN (ho_ten, tuoi, dia_chi, luong, id_phong) VALUES (?, ?, ?, ?, ?);", 
                   (ho_ten, tuoi, dia_chi, luong, id_phong))
    connection.commit()
    print(f"Nhân viên '{ho_ten}' đã được thêm vào phòng {id_phong}!")

# Hàm hiển thị danh sách phòng ban
def display_phong():
    cursor.execute("SELECT * FROM PHONG;")
    rooms = cursor.fetchall()
    print("Danh sách phòng ban:")
    for room in rooms:
        print(f"ID: {room[0]}, Name: {room[1]}, Price: {room[2]}, Amount: {room[3]}")

# Hàm hiển thị danh sách nhân viên
def display_nhan_vien():
    cursor.execute("""
        SELECT NHAN_VIEN.id, NHAN_VIEN.ho_ten, NHAN_VIEN.tuoi, NHAN_VIEN.dia_chi, NHAN_VIEN.luong, PHONG.name
        FROM NHAN_VIEN
        JOIN PHONG ON NHAN_VIEN.id_phong = PHONG.id;
    """)
    employees = cursor.fetchall()
    print("Danh sách nhân viên:")
    for emp in employees:
        print(f"ID: {emp[0]}, Name: {emp[1]}, Age: {emp[2]}, Address: {emp[3]}, Salary: {emp[4]}, Department: {emp[5]}")

# Giao diện người dùng cho việc thực hiện các thao tác
def menu():
    while True:
        print("\n--- Quản lý nhân viên ---")
        print("1. Hiển thị danh sách phòng ban")
        print("2. Thêm phòng ban")
        print("3. Thêm nhân viên")
        print("4. Hiển thị danh sách nhân viên")
        print("5. Thoát")
        choice = input("Chọn chức năng (1-5): ")

        if choice == '1':
            display_phong()
        elif choice == '2':
            name = input("Nhập tên phòng ban: ")
            price = float(input("Nhập giá trị phòng ban: "))
            amount = int(input("Nhập số lượng nhân viên: "))
            add_phong(name, price, amount)
        elif choice == '3':
            ho_ten = input("Nhập họ tên nhân viên: ")
            tuoi = int(input("Nhập tuổi nhân viên: "))
            dia_chi = input("Nhập địa chỉ nhân viên: ")
            luong = float(input("Nhập lương nhân viên: "))
            id_phong = int(input("Nhập ID phòng ban nhân viên thuộc về: "))
            add_nhan_vien(ho_ten, tuoi, dia_chi, luong, id_phong)
        elif choice == '4':
            display_nhan_vien()
        elif choice == '5':
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

# Chạy chương trình
menu()

# Đóng kết nối với cơ sở dữ liệu
connection.close()
