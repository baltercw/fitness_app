# Flask 速查表

## 基礎結構

```python
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello"

if __name__ == '__main__':
    app.run(debug=True)
```

---

## 路由類型

```python
# 基本路由
@app.route('/')
def home():
    return "首頁"

# 動態路由
@app.route('/user/<name>')
def user(name):
    return f"你好，{name}"

# 整數參數
@app.route('/post/<int:id>')
def post(id):
    return f"文章 {id}"

# 多個參數
@app.route('/profile/<name>/<int:age>')
def profile(name, age):
    return f"{name}, {age} 歲"
```

---

## GET vs POST

```python
@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # 處理表單送出
        data = request.form['欄位名']
        return redirect(url_for('函數名'))
    
    # 顯示頁面
    return render_template('form.html')
```

---

## 模板（Jinja2）

### 傳變數
```python
# Python
return render_template('page.html', name='John', age=25)
```

```html
<!-- HTML -->
<h1>{{ name }}</h1>
<p>{{ age }} 歲</p>
```

### for 迴圈
```html
{% for item in items %}
    <li>{{ item }}</li>
{% endfor %}
```

### if 判斷
```html
{% if score >= 60 %}
    <p style="color: green">及格</p>
{% else %}
    <p style="color: red">不及格</p>
{% endif %}
```

### 字典取值
```html
{% for user in users %}
    <li>{{ user.name }} - {{ user.age }} 歲</li>
{% endfor %}
```

---

## 表單

```html
<form method="POST">
    <input type="text" name="username" placeholder="姓名">
    <input type="text" name="message" placeholder="留言">
    <button type="submit">送出</button>
</form>
```

```python
# Python 取得
username = request.form['username']
message = request.form['message']
```

---

## 重新導向

```python
# 跳轉到其他函數
return redirect(url_for('home'))
return redirect(url_for('guestbook'))

# 跳轉到外部網址
return redirect('https://google.com')
```

---

## 常見模式

### 留言板模式
```python
messages = []

@app.route('/guestbook', methods=['GET', 'POST'])
def guestbook():
    if request.method == 'POST':
        msg = request.form['message']
        messages.append(msg)
        return redirect(url_for('guestbook'))
    return render_template('guestbook.html', messages=messages)
```

### 顯示列表
```python
items = [1, 2, 3, 4, 5]
return render_template('page.html', items=items)
```

```html
{% for item in items %}
    <li>{{ item }}</li>
{% endfor %}
```

### 顯示字典列表
```python
users = [
    {'name': 'John', 'age': 25},
    {'name': 'Mary', 'age': 30}
]
return render_template('users.html', users=users)
```

```html
{% for user in users %}
    <li>{{ user.name }} - {{ user.age }} 歲</li>
{% endfor %}
```

---

## Jinja2 語法

| 功能 | 語法 |
|------|------|
| 顯示變數 | `{{ 變數 }}` |
| for 迴圈 | `{% for x in list %}...{% endfor %}` |
| if 判斷 | `{% if 條件 %}...{% endif %}` |
| if-else | `{% if 條件 %}...{% else %}...{% endif %}` |
| if-elif-else | `{% if %}...{% elif %}...{% else %}...{% endif %}` |
| 註解 | `{# 註解 #}` |

---

## 常見錯誤

```python
# ❌ 路由忘記 /
@app.route('about')

# ✅
@app.route('/about')

# ❌ 檔名忘記引號
render_template(page.html)

# ✅
render_template('page.html')

# ❌ request.form 忘記引號
request.form[name]

# ✅
request.form['name']

# ❌ Jinja2 if 用了 {{ }}
{% if {{ score }} >= 60 %}

# ✅
{% if score >= 60 %}
```

---

**需要什麼隨時查這個！** 📖

