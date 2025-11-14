# SQL 從零開始

## 🤔 SQL 是什麼？

**SQL = 資料庫的語言**

就像：
- Python 用來寫程式
- SQL 用來管理資料

**資料庫 = 有組織的資料儲存庫**

---

## 💡 為什麼要學 SQL？

**現在您的留言板：**
```python
messages = []  # 存在記憶體
```

**問題：**
- ❌ 程式關掉，資料就不見了
- ❌ 資料多了很慢
- ❌ 無法搜尋、排序

**用資料庫：**
```python
# 存在資料庫（SQLite/PostgreSQL）
```

**好處：**
- ✅ 永久儲存
- ✅ 快速查詢
- ✅ 能搜尋、排序、過濾
- ✅ 多人同時使用

---

## 🎯 資料庫類型

### SQLite（初學推薦）
- 檔案型資料庫（一個 .db 檔案）
- Python 內建支援
- 適合：學習、小專案

### PostgreSQL/MySQL（正式環境）
- 伺服器型資料庫
- 功能強大
- 適合：正式專案、多人協作

**我們先學 SQLite！**

---

## 📚 SQL 核心概念

### 1. 資料表（Table）

**想像 Excel 試算表：**

| id | name | age | email |
|----|------|-----|-------|
| 1  | John | 25  | john@example.com |
| 2  | Mary | 30  | mary@example.com |

- **欄位（Column）**：name, age, email
- **資料列（Row）**：每一筆資料
- **主鍵（Primary Key）**：id（唯一識別）

---

### 2. SQL 四大操作（CRUD）

| 操作 | SQL 指令 | 說明 |
|------|---------|------|
| **C**reate | `INSERT` | 新增資料 |
| **R**ead | `SELECT` | 讀取資料 |
| **U**pdate | `UPDATE` | 修改資料 |
| **D**elete | `DELETE` | 刪除資料 |

---

## 🚀 第一步：創建資料庫

**創建 `test.py`，自己打以下代碼：**

```python
import sqlite3

# 連接資料庫（沒有會自動創建）
conn = sqlite3.connect('test.db')

# 創建游標（用來執行 SQL）
cursor = conn.cursor()

# 創建資料表
cursor.execute('''
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
''')

# 儲存變更
conn.commit()

# 關閉連線
conn.close()

print("資料庫創建成功！")
```

---

## 📖 逐行解釋

### 第 1 行：引入 sqlite3
```python
import sqlite3
```
**做什麼：** 引入 Python 內建的 SQLite 模組

---

### 第 2 行：連接資料庫
```python
conn = sqlite3.connect('test.db')
```
**做什麼：** 連接（或創建）資料庫檔案
**結果：** 產生 `test.db` 檔案

---

### 第 3 行：創建游標
```python
cursor = conn.cursor()
```
**做什麼：** 創建一個「執行 SQL 的工具」
**比喻：** conn 是資料庫，cursor 是操作資料庫的「游標」

---

### 第 4 行：執行 SQL
```python
cursor.execute('''SQL 語句''')
```
**做什麼：** 執行 SQL 指令

**SQL 語句：**
```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
```
**意思：** 創建一個叫 `users` 的表，有 3 個欄位

---

### 第 5 行：儲存
```python
conn.commit()
```
**做什麼：** 確認並儲存變更
**重要：** 沒有這行，資料不會真的寫入！

---

### 第 6 行：關閉
```python
conn.close()
```
**做什麼：** 關閉資料庫連線

---

## ✍️ 現在的任務

**創建 `test.py`，自己打上面的代碼**

**理解：**
- `connect()` - 連接資料庫
- `cursor()` - 創建執行工具
- `execute()` - 執行 SQL
- `commit()` - 儲存
- `close()` - 關閉

**運行：**
```bash
python test.py
```

**應該看到：**
- 顯示「資料庫創建成功！」
- 產生 `test.db` 檔案

---

**完成後告訴我，我教您怎麼新增資料！** 💪

一步一步來，不急！
