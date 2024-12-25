import sqlite3

def connect_db():
    """Kết nối đến cơ sở dữ liệu hoặc tạo mới nếu chưa tồn tại."""
    conn = sqlite3.connect("product.db")
    return conn

def create_table():
    """Tạo bảng product trong cơ sở dữ liệu."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS product (
            Id INTEGER PRIMARY KEY,
            Name TEXT NOT NULL,
            Price REAL NOT NULL,
            Amount INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def display_products():
    """Hiển thị danh sách sản phẩm."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM product")
    products = cursor.fetchall()
    conn.close()
    print("\nDanh Sách Sản Phẩm:")
    print("ID | Tên Sản Phẩm | Giá | Số Lượng")
    for product in products:
        print(f"{product[0]} | {product[1]} | {product[2]} | {product[3]}")

def add_product():
    """Thêm sản phẩm mới vào cơ sở dữ liệu."""
    name = input("Nhập tên sản phẩm: ")
    price = float(input("Nhập giá sản phẩm: "))
    amount = int(input("Nhập số lượng sản phẩm: "))
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO product (Name, Price, Amount) VALUES (?, ?, ?)", (name, price, amount))
    conn.commit()
    conn.close()
    print("\nSản phẩm đã được thêm thành công!")

def search_product():
    """Tìm kiếm sản phẩm theo tên."""
    search_name = input("Nhập tên sản phẩm cần tìm: ")
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM product WHERE Name LIKE ?", (f"%{search_name}%",))
    products = cursor.fetchall()
    conn.close()
    if products:
        print("\nKết quả tìm kiếm:")
        print("ID | Tên Sản Phẩm | Giá | Số Lượng")
        for product in products:
            print(f"{product[0]} | {product[1]} | {product[2]} | {product[3]}")
    else:
        print("\nKhông tìm thấy sản phẩm phù hợp.")

def update_product():
    """Cập nhật thông tin sản phẩm dựa trên ID."""
    product_id = int(input("Nhập ID sản phẩm cần cập nhật: "))
    new_price = float(input("Nhập giá mới: "))
    new_amount = int(input("Nhập số lượng mới: "))
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE product SET Price = ?, Amount = ? WHERE Id = ?", (new_price, new_amount, product_id))
    conn.commit()
    conn.close()
    print("\nThông tin sản phẩm đã được cập nhật thành công!")

def delete_product():
    """Xóa sản phẩm khỏi cơ sở dữ liệu dựa trên ID."""
    product_id = int(input("Nhập ID sản phẩm cần xóa: "))
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM product WHERE Id = ?", (product_id,))
    conn.commit()
    conn.close()
    print("\nSản phẩm đã được xóa thành công!")

def main_menu():
    """Menu chính của chương trình."""
    create_table()  # Đảm bảo bảng được tạo trước khi sử dụng
    while True:
        print("\nQuản Lý Sản Phẩm")
        print("1. Hiển Thị Danh Sách Sản Phẩm")
        print("2. Thêm Sản Phẩm Mới")
        print("3. Tìm Kiếm Sản Phẩm Theo Tên")
        print("4. Cập Nhật Thông Tin Sản Phẩm")
        print("5. Xóa Sản Phẩm")
        print("6. Thoát")
        choice = input("Chọn chức năng (1-6): ")

        if choice == "1":
            display_products()
        elif choice == "2":
            add_product()
        elif choice == "3":
            search_product()
        elif choice == "4":
            update_product()
        elif choice == "5":
            delete_product()
        elif choice == "6":
            print("\nThoát chương trình. Tạm biệt!")
            break
        else:
            print("\nLựa chọn không hợp lệ. Vui lòng chọn lại.")

# Chạy chương trình
main_menu()
