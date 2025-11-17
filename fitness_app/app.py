from flask import Flask, render_template, request, redirect, url_for
import sqlite3

def init_db():
    conn = sqlite3.connect('fitness_app.db')
    cursor = conn.cursor()
    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''') #大肌群分類 胸 肩 背 腿 二頭 三頭

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS exercises (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category_id INTEGER NOT NULL,
            FOREIGN KEY (category_id) REFERENCES categories(id)
        )
    ''') #動作表 槓鈴臥推 啞鈴臥推

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS workouts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            exercise_id INTEGER NOT NULL,
            sets INTEGER NOT NULL,
            reps INTEGER NOT NULL,
            weight REAL NOT NULL,
            FOREIGN KEY (exercise_id) REFERENCES exercises(id)
        )
    ''') #紀錄表
    conn.commit()
    conn.close()

init_db()
app = Flask(__name__)

conn = sqlite3.connect('fitness_app.db')
cursor = conn.cursor()
cursor.execute("SELECT COUNT(*) FROM categories")
if cursor.fetchone()[0] == 0:
    # 插入預設值
    default_categories = [
        ('胸',), ('背',), ('肩',), ('腿',), ('二頭',), ('三頭',),
    ]
    cursor.executemany("INSERT INTO categories (name) VALUES (?)", default_categories)
conn.commit()
conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect('fitness_app.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT workouts.date, exercises.name, workouts.sets, workouts.reps, workouts.weight
        FROM workouts
        JOIN exercises ON workouts.exercise_id = exercises.id
        ORDER BY workouts.date DESC
    ''')
    rows = cursor.fetchall()
    #按日期分組
    workout_by_date = {}
    for row in rows:
        date = row[0]
        if date not in workout_by_date:
            workout_by_date[date] = []

        workout_by_date[date].append({
            'name' : row[1],
            'sets' : row[2],
            'reps' : row[3],
            'weight' : row[4],
        })
    conn.close()

    return render_template('index.html', workout_by_date=workout_by_date)

@app.route('/workout/<date>')
def workout_detail(date):
    conn = sqlite3.connect('fitness_app.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT workouts.id, exercises.name, workouts.sets, workouts.reps, workouts.weight
        FROM workouts
        JOIN exercises ON workouts.exercise_id = exercises.id
        WHERE workouts.date = ?
        ORDER BY workouts.id
    ''', (date,))
    rows = cursor.fetchall()

    workouts = []
    for row in rows:
        workouts.append({
            'id' : row[0],
            'name' : row[1],
            'sets' : row[2],
            'reps' : row[3],
            'weight' : row[4]
        })

    conn.close()
    return render_template('workout_detail.html', date=date, workouts=workouts)

if __name__ == '__main__':
    app.run(debug=True)