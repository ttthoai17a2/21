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

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    print("Tables in the database:")
    for table in tables:
        print(f"- {table[0]}")

finally:
    connection.close()
