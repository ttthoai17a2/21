import sqlite3

def connect_db():
    """Kết nối đến cơ sở dữ liệu hoặc tạo mới nếu chưa tồn tại."""
    conn = sqlite3.connect("product.db")  # Tên cơ sở dữ liệu
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
    print("Bảng 'product' đã được tạo thành công (nếu chưa tồn tại).")

# Gọi hàm để tạo cơ sở dữ liệu và bảng
create_table()
