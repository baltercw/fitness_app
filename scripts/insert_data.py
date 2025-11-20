import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

cursor.execute("INSERT INTO users (name, age) VALUES ('john', 25)")

conn.commit()
conn.close()

print('資料新增成功')