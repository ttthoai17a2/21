import sqlite3

# Kết nối đến cơ sở dữ liệu SQLite (product.db)
connection = sqlite3.connect('product.db')
cursor = connection.cursor()

# Tạo bảng sản phẩm nếu chưa tồn tại
cursor.execute("""
    CREATE TABLE IF NOT EXISTS product (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        amount INTEGER NOT NULL
    );
""")
connection.commit()

# Hàm hiển thị danh sách sản phẩm
def display_products():
    cursor.execute("SELECT * FROM product;")
    products = cursor.fetchall()
    print("Danh sách sản phẩm:")
    for product in products:
        print(f"ID: {product[0]}, Name: {product[1]}, Price: {product[2]}, Amount: {product[3]}")

# Hàm thêm sản phẩm vào bảng
def add_product(name, price, amount):
    cursor.execute("INSERT INTO product (name, price, amount) VALUES (?, ?, ?);", (name, price, amount))
    connection.commit()
    print(f"Sản phẩm '{name}' đã được thêm vào!")

# Hàm tìm kiếm sản phẩm theo tên
def search_product(name):
    cursor.execute("SELECT * FROM product WHERE name LIKE ?;", ('%' + name + '%',))
    products = cursor.fetchall()
    if products:
        print("Kết quả tìm kiếm:")
        for product in products:
            print(f"ID: {product[0]}, Name: {product[1]}, Price: {product[2]}, Amount: {product[3]}")
    else:
        print("Không tìm thấy sản phẩm với tên này.")

# Hàm cập nhật giá và số lượng sản phẩm theo ID
def update_product(id, price, amount):
    cursor.execute("UPDATE product SET price = ?, amount = ? WHERE id = ?;", (price, amount, id))
    connection.commit()
    print(f"Sản phẩm có ID {id} đã được cập nhật.")

# Hàm xóa sản phẩm theo ID
def delete_product(id):
    cursor.execute("DELETE FROM product WHERE id = ?;", (id,))
    connection.commit()
    print(f"Sản phẩm có ID {id} đã bị xóa.")

# Giao diện người dùng cho việc thực hiện các thao tác
def menu():
    while True:
        print("\n--- Quản lý sản phẩm ---")
        print("1. Hiển thị danh sách sản phẩm")
        print("2. Thêm sản phẩm")
        print("3. Tìm kiếm sản phẩm theo tên")
        print("4. Cập nhật sản phẩm theo ID")
        print("5. Xóa sản phẩm theo ID")
        print("6. Thoát")
        choice = input("Chọn chức năng (1-6): ")

        if choice == '1':
            display_products()
        elif choice == '2':
            name = input("Nhập tên sản phẩm: ")
            price = float(input("Nhập giá sản phẩm: "))
            amount = int(input("Nhập số lượng sản phẩm: "))
            add_product(name, price, amount)
        elif choice == '3':
            name = input("Nhập tên sản phẩm để tìm kiếm: ")
            search_product(name)
        elif choice == '4':
            id = int(input("Nhập ID sản phẩm cần cập nhật: "))
            price = float(input("Nhập giá mới của sản phẩm: "))
            amount = int(input("Nhập số lượng mới của sản phẩm: "))
            update_product(id, price, amount)
        elif choice == '5':
            id = int(input("Nhập ID sản phẩm cần xóa: "))
            delete_product(id)
        elif choice == '6':
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

# Chạy chương trình
menu()

# Đóng kết nối với cơ sở dữ liệu
connection.close()
