"""
Python 實戰速查表
================
專為 Flask/SQL/爬蟲 設計
C 程式設計師快速上手版
"""

# ==============================================
# 1. 核心語法差異（5 分鐘掌握）
# ==============================================

# 變數（不用宣告類型）
x = 10
name = "John"
data = [1, 2, 3]

# 條件（用縮排，不用大括號）
if x > 5:
    print("大於 5")
elif x > 0:
    print("大於 0")
else:
    print("小於等於 0")

# 迴圈
for i in range(10):          # 0 到 9
    pass

for item in data:            # 直接遍歷
    pass

# 函數（用 def，不用類型）
def add(a, b):
    return a + b

# 列表（動態陣列）
my_list = [1, 2, 3]
my_list.append(4)            # 添加
my_list.extend([5, 6])       # 合併
item = my_list[0]            # 存取
my_list[-1]                  # 最後一個

# 字典（key-value，超重要！）
user = {
    "name": "John",
    "age": 25,
    "email": "john@example.com"
}
print(user["name"])          # John
user["city"] = "Taipei"      # 新增
user.get("phone", "無")      # 安全取值


# ==============================================
# 2. 字串操作（爬蟲必備）
# ==============================================

# f-string（最推薦）
name = "John"
age = 25
print(f"{name} is {age} years old")

# 切片
text = "Hello, World!"
text[0:5]        # "Hello"
text[::-1]       # 反轉
text.split(",")  # ['Hello', ' World!']

# 常用方法
text.strip()           # 去除空白
text.lower()           # 轉小寫
text.replace("a", "b") # 替換
text.startswith("H")   # 檢查開頭
"sub" in text          # 包含檢查

# JSON 字串轉字典（API 必用）
import json
json_str = '{"name": "John", "age": 25}'
data = json.loads(json_str)
json_text = json.dumps(data)


# ==============================================
# 3. 檔案操作
# ==============================================

# 讀取檔案
with open("file.txt", "r", encoding="utf-8") as f:
    content = f.read()           # 全部讀取
    # lines = f.readlines()      # 按行讀取

# 寫入檔案
with open("file.txt", "w", encoding="utf-8") as f:
    f.write("Hello\n")

# CSV 操作（資料處理常用）
import csv
with open("data.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"])


# ==============================================
# 4. Web 開發核心（Flask）
# ==============================================

# Flask 基礎結構
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# 路由（GET）
@app.route("/")
def index():
    return "Hello, World!"

# 路由（POST）
@app.route("/api/data", methods=["POST"])
def post_data():
    data = request.json          # 獲取 JSON
    # data = request.form        # 獲取表單
    return jsonify({"status": "ok", "data": data})

# 動態路由
@app.route("/user/<int:user_id>")
def user_profile(user_id):
    return f"User ID: {user_id}"

# 渲染模板
@app.route("/page")
def page():
    return render_template("index.html", title="首頁", users=users)

# 運行
if __name__ == "__main__":
    app.run(debug=True)


# ==============================================
# 5. 資料庫操作（SQL）
# ==============================================

# SQLite（最簡單，適合練習）
import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# 創建表
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT
    )
""")

# 插入資料
cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", 
               ("John", "john@example.com"))
conn.commit()

# 查詢資料
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()


# Flask + SQLAlchemy（推薦！）
from flask_sqlalchemy import SQLAlchemy

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
db = SQLAlchemy(app)

# 定義模型
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)

# 創建表
# db.create_all()

# 新增
# user = User(name="John", email="john@example.com")
# db.session.add(user)
# db.session.commit()

# 查詢
# users = User.query.all()
# user = User.query.filter_by(name="John").first()
# user = User.query.get(1)  # 按 ID


# ==============================================
# 6. 網頁爬蟲
# ==============================================

# requests（發送 HTTP 請求）
import requests

# GET 請求
response = requests.get("https://example.com")
html = response.text
status = response.status_code

# POST 請求
data = {"username": "john", "password": "123"}
response = requests.post("https://example.com/login", data=data)

# 帶 Headers
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get("https://example.com", headers=headers)


# BeautifulSoup（解析 HTML）
from bs4 import BeautifulSoup

soup = BeautifulSoup(html, "html.parser")

# 找元素
title = soup.find("title").text
links = soup.find_all("a")
div = soup.find("div", class_="content")
item = soup.select_one("#item")       # CSS selector

# 提取資料
for link in links:
    url = link.get("href")
    text = link.text
    print(f"{text}: {url}")


# 完整爬蟲範例
def scrape_website(url):
    response = requests.get(url, headers={
        "User-Agent": "Mozilla/5.0"
    })
    soup = BeautifulSoup(response.text, "html.parser")
    
    # 提取標題
    titles = soup.find_all("h2", class_="title")
    results = []
    for title in titles:
        results.append(title.text.strip())
    
    return results


# ==============================================
# 7. 實用技巧
# ==============================================

# 列表推導式（超好用）
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]

# 字典推導式
user_ages = {user["name"]: user["age"] for user in users}

# enumerate（需要索引時）
for i, item in enumerate(my_list):
    print(f"{i}: {item}")

# zip（平行遍歷）
names = ["John", "Jane", "Bob"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age}")

# try-except（錯誤處理）
try:
    result = 10 / 0
except ZeroDivisionError:
    print("除以零錯誤")
except Exception as e:
    print(f"其他錯誤：{e}")
finally:
    print("總是執行")

# lambda（匿名函數）
add = lambda x, y: x + y
sorted_list = sorted(users, key=lambda u: u["age"])

# map, filter
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x*2, numbers))
evens = list(filter(lambda x: x%2==0, numbers))


# ==============================================
# 8. 常用套件安裝
# ==============================================
"""
# 基礎
pip install flask
pip install requests
pip install beautifulsoup4

# 資料庫
pip install flask-sqlalchemy
pip install pymysql

# 爬蟲進階
pip install selenium
pip install scrapy

# 資料處理
pip install pandas
pip install numpy
"""


# ==============================================
# 9. Flask 完整範例
# ==============================================
"""
# app.py
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.Text)

@app.route('/')
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)

@app.route('/post/<int:id>')
def post(id):
    post = Post.query.get_or_404(id)
    return render_template('post.html', post=post)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        post = Post(title=title, content=content)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('create.html')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
"""


# ==============================================
# 10. 爬蟲完整範例
# ==============================================
"""
# scraper.py
import requests
from bs4 import BeautifulSoup
import time

def scrape_news():
    url = "https://example.com/news"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    
    articles = soup.find_all("article", class_="news-item")
    news_list = []
    
    for article in articles:
        title = article.find("h2").text.strip()
        link = article.find("a")["href"]
        date = article.find("time")["datetime"]
        
        news_list.append({
            "title": title,
            "link": link,
            "date": date
        })
    
    return news_list

# 儲存到資料庫
def save_to_db(news_list):
    for news in news_list:
        # 插入資料庫邏輯
        pass
"""


# ==============================================
# 快速參考
# ==============================================
"""
C → Python 速記：

int x;              → x = 0
for(;;)            → for i in range():
if (x) { }         → if x:
printf("%d", x)    → print(f"{x}")
arr[i]             → my_list[i]
struct             → dict 或 class
malloc/free        → 自動管理
char *str          → str (字串)
&&, ||, !          → and, or, not
i++                → i += 1

實用技巧：
- 多用 f-string：f"{變數}"
- 字典取代 struct
- 列表推導式超好用
- with 自動關閉檔案
- try-except 處理錯誤
- requests + BeautifulSoup = 爬蟲
- Flask + SQLAlchemy = Web App
"""

print("速查表載入完成！")
print("開始寫 practice.py 的練習題吧！")

