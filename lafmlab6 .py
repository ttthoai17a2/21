import sqlite3
import tkinter as tk
from tkinter import messagebox

# Kết nối với cơ sở dữ liệu
def connect_db():
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            quantity INTEGER NOT NULL,
            description TEXT
        )
    """)
    conn.commit()
    conn.close()

# Thêm sản phẩm
def add_product():
    name = entry_name.get()
    price = entry_price.get()
    quantity = entry_quantity.get()
    description = entry_description.get()

    if not (name and price and quantity):
        messagebox.showwarning("Lỗi", "Vui lòng nhập đầy đủ thông tin")
        return

    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (name, price, quantity, description) VALUES (?, ?, ?, ?)",
                   (name, float(price), int(quantity), description))
    conn.commit()
    conn.close()
    load_products()
    clear_entries()

# Hiển thị danh sách sản phẩm
def load_products():
    listbox_products.delete(0, tk.END)
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    for row in cursor.fetchall():
        listbox_products.insert(tk.END, f"{row[0]}: {row[1]} - {row[2]} VND")
    conn.close()

# Xóa dữ liệu trong Entry
def clear_entries():
    entry_name.delete(0, tk.END)
    entry_price.delete(0, tk.END)
    entry_quantity.delete(0, tk.END)
    entry_description.delete(0, tk.END)

# Giao diện người dùng
def setup_gui():
    global entry_name, entry_price, entry_quantity, entry_description, listbox_products

    root = tk.Tk()
    root.title("Quản lý sản phẩm")

    # Labels and Entries
    tk.Label(root, text="Tên sản phẩm").grid(row=0, column=0)
    entry_name = tk.Entry(root)
    entry_name.grid(row=0, column=1)

    tk.Label(root, text="Giá").grid(row=1, column=0)
    entry_price = tk.Entry(root)
    entry_price.grid(row=1, column=1)

    tk.Label(root, text="Số lượng").grid(row=2, column=0)
    entry_quantity = tk.Entry(root)
    entry_quantity.grid(row=2, column=1)

    tk.Label(root, text="Mô tả").grid(row=3, column=0)
    entry_description = tk.Entry(root)
    entry_description.grid(row=3, column=1)

    # Buttons
    tk.Button(root, text="Thêm sản phẩm", command=add_product).grid(row=4, column=0, columnspan=2)

    # Listbox
    listbox_products = tk.Listbox(root, width=50)
    listbox_products.grid(row=5, column=0, columnspan=2)

    # Load initial data
    load_products()

    root.mainloop()

connect_db()
setup_gui()
