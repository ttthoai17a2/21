import sqlite3
connection = sqlite3.connect(":memory:")

try:

    cursor = connection.cursor()
    cursor.execute("SELECT sqlite_version();")
    version = cursor.fetchone()

    print(f"SQLite version: {version[0]}")

finally:
    connection.close()
