import sqlite3

conn = sqlite3.connect('test.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
''')

conn.commit()
conn.close()

print("資料庫創建成功!")