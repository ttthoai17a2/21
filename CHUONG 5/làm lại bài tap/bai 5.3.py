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

finally:
    connection.close()
