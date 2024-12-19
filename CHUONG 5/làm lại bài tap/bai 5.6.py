import sqlite3

connection = sqlite3.connect("example.db")

try:
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        );
    """)

    print("Table 'users' created successfully.")

    users_data = [
        ("Alice", 30),
        ("Bob", 25),
        ("Charlie", 35)
    ]
    cursor.executemany("INSERT INTO users (name, age) VALUES (?, ?);", users_data)
    connection.commit()
    print("Records inserted successfully.")

    cursor.execute("SELECT COUNT(*) FROM users;")
    record_count = cursor.fetchone()[0]
    print(f"Total records in 'users' table: {record_count}")

finally:
    connection.close()
