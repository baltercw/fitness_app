import sqlite3

conn = sqlite3.connect('guestbook.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM messages")
rows = cursor.fetchall()

print("Guestbook的所有資料!!")
for row in rows:
    print(row)
conn.close()