# Flask 從零開始理解

## 🤔 Flask 是什麼？

**Flask = 讓 Python 能做網站的工具**

就像：
- C 語言寫程式 → 在終端機運行
- Flask 寫程式 → 在瀏覽器運行

---

## 💡 為什麼要學 Flask？

有了 Flask，您可以：
- ✅ 做網站（部落格、論壇）
- ✅ 做 API（讓手機 App 或其他程式連接）
- ✅ 做後端系統（處理資料、連資料庫）
- ✅ 做爬蟲的管理介面

**實際應用：**
- 做一個記帳網站
- 做一個個人部落格
- 做一個 TODO 清單網站
- 爬蟲結果用網頁顯示

---

## 🎯 核心概念（超重要！）

### 1. 什麼是「伺服器」？

```
您的電腦上有一個程式（Flask）在運行
    ↓
瀏覽器訪問 http://127.0.0.1:5000
    ↓
Flask 收到請求
    ↓
Flask 返回內容（HTML、JSON）
    ↓
瀏覽器顯示
```

**127.0.0.1 = 您自己的電腦（localhost）**
**5000 = Flask 預設的埠號（port）**

---

### 2. 什麼是「路由」（Route）？

```
http://127.0.0.1:5000/          → 首頁
http://127.0.0.1:5000/about     → 關於頁面
http://127.0.0.1:5000/user/123  → 使用者 123 的頁面
```

**路由 = 告訴 Flask「訪問這個網址時，要做什麼」**

就像：
- 按「首頁」按鈕 → 顯示首頁內容
- 按「關於」按鈕 → 顯示關於內容

---

## 📝 逐行解釋

### 第 1 行：引入 Flask
```python
from flask import Flask
```

**做什麼：** 把 Flask 這個工具引入程式

**為什麼：** 就像 C 語言要 `#include <stdio.h>` 才能用 `printf()`

**不寫會怎樣：** 後面無法使用 Flask

---

### 第 2 行：創建應用
```python
app = Flask(__name__)
```

**做什麼：** 創建一個 Flask 應用（網站）

**為什麼：**
- `app` = 您的網站
- `__name__` = 告訴 Flask 這個檔案的名稱（Flask 需要知道）

**比喻：** 就像開一家店，`app` 是這家店

---

### 第 3-5 行：定義路由
```python
@app.route('/')
def hello():
    return "Hello, World!"
```

**做什麼：** 定義「訪問首頁時要做什麼」

**逐句解釋：**

**`@app.route('/')`**
- `@` = 裝飾器（decorator），Python 的語法
- `'/'` = 首頁的網址（根目錄）
- 意思：「下面這個函數處理首頁」

**`def hello():`**
- 定義一個函數（就是普通的 Python 函數）
- 名字可以隨便取（`hello`、`home`、`index` 都可以）

**`return "Hello, World!"`**
- 返回內容給瀏覽器
- 瀏覽器會顯示 "Hello, World!"

**為什麼這樣設計：**
- 不同網址 → 不同函數
- 靈活：每個頁面做不同的事

---

### 第 6-7 行：運行應用
```python
if __name__ == '__main__':
    app.run(debug=True)
```

**做什麼：** 啟動 Flask 伺服器

**`if __name__ == '__main__':`**
- 確保這個檔案是直接運行的（不是被 import 的）
- Python 標準寫法

**`app.run(debug=True)`**
- 啟動伺服器
- `debug=True` = 開發模式（代碼改了會自動重新載入，顯示錯誤訊息）

---

## 🔄 完整流程

1. **運行 `python app.py`**
   → Flask 啟動伺服器，監聽 5000 埠

2. **瀏覽器訪問 `http://127.0.0.1:5000/`**
   → Flask 收到請求

3. **Flask 看到網址是 `/`**
   → 執行 `hello()` 函數

4. **`hello()` 返回 "Hello, World!"**
   → Flask 把這個字串傳給瀏覽器

5. **瀏覽器顯示**
   → 您看到 "Hello, World!"

---

## 🚀 可以衍伸的應用

### 應用 1: 多個頁面
```python
@app.route('/')
def home():
    return "首頁"

@app.route('/about')
def about():
    return "關於頁面"
```

### 應用 2: 動態內容
```python
@app.route('/user/<name>')
def user(name):
    return f"你好，{name}！"
```
訪問 `/user/John` → 顯示 "你好，John！"

### 應用 3: 顯示 HTML
```python
@app.route('/')
def home():
    return "<h1>標題</h1><p>這是段落</p>"
```

### 應用 4: 返回 JSON（做 API）
```python
from flask import jsonify

@app.route('/api/data')
def api():
    return jsonify({'name': 'John', 'age': 25})
```

---

## 💭 現在理解了嗎？

**核心就是：**
1. **創建應用** (`app = Flask(__name__)`)
2. **定義路由** (`@app.route('/')`)
3. **寫函數** (`def hello():`)
4. **返回內容** (`return "..."`)
5. **啟動伺服器** (`app.run()`)

---

## ✍️ 現在可以開始寫了

**理解了這些概念後，您可以：**

1. **先安裝 Flask**
   ```bash
   pip install flask
   ```

2. **創建 `app.py`，自己打代碼**
   - 現在您知道每一行在做什麼了
   - 知道為什麼要這樣寫

3. **運行並測試**
   ```bash
   python app.py
   ```

4. **實驗改變**
   - 改 `return` 的內容
   - 加新的路由
   - 試試動態網址

---

**理解了嗎？還有哪裡不清楚？**
