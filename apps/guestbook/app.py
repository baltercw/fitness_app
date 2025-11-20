from flask import Flask, render_template, request, redirect, url_for
import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'guestbook.db')

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            message TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

app = Flask(__name__)

@app.route('/guestbook', methods=['GET', 'POST'])
def guestbook():
    if request.method == 'POST':
        name = request.form['name']
        msg = request.form['message']

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        # ⚠️ 注意：第二個參數必須是 tuple (name, msg)，不是 name, msg
        # SQL 字串裡的 name, message 是「資料庫欄位名稱」，不是 Python 變數
        cursor.execute("INSERT INTO messages (name, message) VALUES (?, ?)",
        (name, msg))

        conn.commit()
        conn.close()

        return redirect(url_for('guestbook'))

    # ⚠️ 注意：GET 請求也要重新建立連線（每次請求都是獨立的）
    # 不能共用 POST 的連線，因為那是不同次的請求
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, message FROM messages")
    # fetchall() 回傳 list of tuple: [(id, name, message), ...]
    # 模板中 message[0]=id, message[1]=name, message[2]=message
    rows = cursor.fetchall()
    conn.close()

    return render_template('guestbook.html', messages=rows)

@app.route('/guestbook/delete/<int:id>')
def delete(id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM messages WHERE id = ?", (id,))  # SQL 參數必須是 tuple
    conn.commit()
    conn.close()
    return redirect(url_for('guestbook'))

@app.route('/guestbook/edit/<int:id>')
def edit(id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM messages WHERE id = ?", (id,))  # SQL 參數必須是 tuple
    row = cursor.fetchone()  # tuple: (id, name, message)
    conn.close()
    return render_template('edit.html', row=row)

@app.route('/guestbook/update/<int:id>', methods=['POST'])
def update(id):
    name = request.form['name']
    msg = request.form['message']

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("UPDATE messages SET name = ?, message = ? WHERE id = ?", (name, msg, id))  # SQL 參數必須是 tuple
    conn.commit()
    conn.close()

    return redirect(url_for('guestbook'))

if __name__ == '__main__':
    app.run(debug=True)
