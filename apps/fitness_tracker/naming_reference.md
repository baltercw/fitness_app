# 健身 App 命名參考

## 📊 資料表命名

### 核心表
- `exercises` - 動作表
- `workouts` - 訓練記錄表

### 未來擴充表
- `workout_sessions` - 訓練日（一次訓練可能包含多個動作）
- `body_measurements` - 體重/體脂記錄
- `exercise_categories` - 動作分類
- `training_programs` - 訓練計劃

---

## 📝 資料表欄位命名

### exercises 表
- `id` - 主鍵
- `name` - 動作名稱
- `muscle_group` - 訓練部位
- `description` - 動作說明（未來）
- `created_at` - 建立時間（未來）

### workouts 表
- `id` - 主鍵
- `date` - 訓練日期
- `exercise_id` - 動作 ID（外鍵）
- `sets` - 組數
- `reps` - 次數
- `weight` - 重量（kg）
- `notes` - 備註（未來）
- `created_at` - 建立時間（未來）

---

## 🛣️ 路由命名

### 主要路由
- `/` - 首頁（導向 workouts）
- `/workouts` - 訓練記錄列表
- `/workouts/add` - 新增訓練記錄
- `/workouts/<int:id>` - 查看單筆記錄
- `/workouts/<int:id>/edit` - 編輯記錄
- `/workouts/<int:id>/delete` - 刪除記錄

### 動作管理路由（未來）
- `/exercises` - 動作列表
- `/exercises/add` - 新增動作
- `/exercises/<int:id>/edit` - 編輯動作
- `/exercises/<int:id>/delete` - 刪除動作

### 統計路由（未來）
- `/workouts/stats` - 統計頁面
- `/workouts/stats/<exercise_name>` - 特定動作的統計

---

## 🔧 函數命名

### 資料庫相關
- `init_db()` - 初始化資料庫
- `init_exercises_table()` - 初始化動作表
- `init_workouts_table()` - 初始化訓練記錄表

### 路由處理函數
- `index()` - 首頁
- `list_workouts()` - 列出所有訓練記錄
- `add_workout()` - 新增訓練記錄
- `get_workout(id)` - 取得單筆記錄
- `edit_workout(id)` - 編輯記錄
- `update_workout(id)` - 更新記錄
- `delete_workout(id)` - 刪除記錄

### 動作管理函數（未來）
- `list_exercises()` - 列出所有動作
- `add_exercise()` - 新增動作
- `edit_exercise(id)` - 編輯動作
- `delete_exercise(id)` - 刪除動作

### 工具函數（未來）
- `get_exercise_by_id(id)` - 根據 ID 取得動作
- `get_workouts_by_date(date)` - 根據日期取得記錄
- `get_workouts_by_exercise(exercise_id)` - 根據動作取得記錄
- `calculate_total_volume(workouts)` - 計算總訓練量
- `get_pr_record(exercise_id)` - 取得個人最佳記錄

---

## 📦 變數命名

### 資料庫相關
- `conn` - 資料庫連線
- `cursor` - 資料庫游標
- `db_path` - 資料庫路徑（未來）

### 資料變數
- `exercise_id` - 動作 ID
- `workout_id` - 訓練記錄 ID
- `exercise_list` - 動作列表
- `workout_list` - 訓練記錄列表
- `workout` - 單筆訓練記錄
- `exercise` - 單筆動作

### 表單資料
- `date` - 日期
- `sets` - 組數
- `reps` - 次數
- `weight` - 重量
- `exercise_name` - 動作名稱
- `muscle_group` - 訓練部位

### 查詢結果
- `rows` - 查詢結果（多筆）
- `row` - 查詢結果（單筆）
- `record` - 記錄（單筆）
- `records` - 記錄（多筆）

### 統計相關（未來）
- `total_volume` - 總訓練量
- `pr_weight` - 個人最佳重量
- `pr_reps` - 個人最佳次數
- `workout_count` - 訓練次數
- `average_weight` - 平均重量

---

## 📄 模板檔案命名

### 主要模板
- `index.html` - 首頁
- `workouts.html` - 訓練記錄列表
- `add_workout.html` - 新增訓練記錄
- `edit_workout.html` - 編輯訓練記錄
- `workout_detail.html` - 查看單筆記錄（未來）

### 動作管理模板（未來）
- `exercises.html` - 動作列表
- `add_exercise.html` - 新增動作
- `edit_exercise.html` - 編輯動作

### 統計模板（未來）
- `stats.html` - 統計頁面
- `exercise_stats.html` - 動作統計

### 共用模板（未來）
- `base.html` - 基礎模板（導航列、頁尾）
- `layout.html` - 佈局模板

---

## 🎨 CSS 類別命名（未來）

### 表單相關
- `.form-container` - 表單容器
- `.form-group` - 表單群組
- `.form-label` - 表單標籤
- `.form-input` - 表單輸入框
- `.form-select` - 表單下拉選單
- `.btn-submit` - 提交按鈕
- `.btn-cancel` - 取消按鈕

### 列表相關
- `.workout-list` - 訓練記錄列表
- `.workout-item` - 單筆記錄項目
- `.workout-header` - 記錄標題
- `.workout-details` - 記錄詳情

### 統計相關
- `.stats-container` - 統計容器
- `.stat-card` - 統計卡片
- `.chart-container` - 圖表容器

---

## 📁 資料夾結構

```
fitness_app/
├── app.py                 # 主程式
├── config.py              # 設定檔（未來）
├── models.py              # 資料模型（未來，如果改用 ORM）
├── templates/             # HTML 模板
│   ├── index.html
│   ├── workouts.html
│   ├── add_workout.html
│   └── edit_workout.html
├── static/                # 靜態檔案（未來）
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── main.js
├── fitness.db             # 資料庫檔案
└── 命名參考.md            # 本檔案
```

---

## 🔑 命名原則總結

1. **小寫為主**：Python 慣例
2. **底線分隔**：`workout_list` 不是 `workoutList`
3. **複數用於集合**：`workouts`（多筆）、`workout`（單筆）
4. **動詞在前**：`add_workout`、`delete_workout`
5. **清楚表達用途**：`get_workout_by_id()` 比 `get()` 清楚
6. **資料表用複數**：`exercises`、`workouts`
7. **路由用複數**：`/workouts`、`/exercises`
8. **函數用動詞**：`add_`、`edit_`、`delete_`、`get_`、`list_`

---

## 📌 常用命名對照表

| 用途 | 命名範例 |
|------|---------|
| 資料表 | `workouts`, `exercises` |
| 欄位 | `exercise_id`, `muscle_group` |
| 函數 | `add_workout()`, `list_workouts()` |
| 路由 | `/workouts`, `/workouts/add` |
| 變數 | `workout_list`, `exercise_id` |
| 模板 | `workouts.html`, `add_workout.html` |

---

## ⚠️ 避免的命名

- ❌ `Workout`（應該用 `workout`）
- ❌ `workoutId`（應該用 `workout_id`）
- ❌ `AddWorkout()`（應該用 `add_workout()`）
- ❌ `workoutTable`（應該用 `workouts`）
- ❌ `/AddWorkout`（應該用 `/workouts/add`）
- ❌ `get()`（應該用 `get_workout()`）

---

**最後更新：2024**
**用途：開發健身 App 時的命名參考**
