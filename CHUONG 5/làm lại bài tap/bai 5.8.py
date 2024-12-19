import sqlite3

connection = sqlite3.connect("example.db")

try:
    cursor = connection.cursor()

    
    user_id_to_delete = 2

    cursor.execute("DELETE FROM users WHERE id = ?;", (user_id_to_delete,))


    connection.commit()

    if cursor.rowcount > 0:
        print(f"Đã xóa người dùng có id = {user_id_to_delete}.")
    else:
        print(f"Không tìm thấy người dùng có id = {user_id_to_delete}.")

    cursor.execute("SELECT * FROM users;")
    updated_rows = cursor.fetchall()

    print("Các bản ghi còn lại trong bảng 'users':")
    for row in updated_rows:
        print(row)

finally:
    connection.close()
