# Line Bot + Gemini 學習路線圖（6 小時速成版）

> 目標：6 小時內從零開始，建立一個每天自動向 Gemini 3.0 提問並把結果透過 LINE Bot 推給自己的私人資訊小幫手。  
> 前提：完全沒申請過 LINE Messaging API 或 Google AI Studio，也沒部署經驗。

---

## 準備概念：需先理解的知識點
1. **HTTP / Webhook 基礎**：知道什麼是 POST 請求、headers、JSON。  
2. **LINE Messaging API 架構**：Bot 由 Channel Secret + Access Token 驅動，訊息由 webhook 收/由 Messaging API push。  
3. **Google Gemini API**：用 API Key 呼叫 `models/gemini-1.5-flash` 或 `gemini-3.0`，傳送 prompt 得到回覆。  
4. **環境與安全**：Python 虛擬環境、env 變數儲存金鑰、ngrok/Render 等讓 LINE 伺服器能回呼你的程式。  
5. **排程**：Windows Task Scheduler 或 cron（若放雲端）讓腳本每日自動執行。

---

## 6 小時學習時程（可依自身節奏微調）

### 第 1 小時：開戶 + 讀規格
- 建 LINE Developers 帳號，建立 Messaging API Channel，記下 Channel Secret 與 Long-Lived Channel Access Token。  
- 進入 Google AI Studio 建立 Gemini API Key。  
- 速讀官方文件：LINE Messaging API Quickstart、Gemini REST API Quickstart，了解整體流程。

### 第 2 小時：環境設置與安全
- 在 `linebot_gemini/` 裡建立虛擬環境、安裝 `line-bot-sdk`, `flask`, `requests`, `python-dotenv`。  
- 建 `config/.env`（不進 Git）儲存 `LINE_CHANNEL_SECRET`, `LINE_CHANNEL_TOKEN`, `GEMINI_API_KEY`。  
- 認識 `.gitignore`、為什麼不要把金鑰放在程式碼裡。

### 第 3 小時：LINE Bot 入門
- 用 Flask（或 FastAPI）寫最小 webhook：收到 LINE 訊息就回「收到」。  
- 使用 ngrok 暫時公開本機 URL，貼到 LINE Console 的 Webhook URL → 測試收到訊息。  
- 理解 `signature` 驗證與 `linebot` 套件的 handler 概念。

### 第 4 小時：Gemini 呼叫練習
- 寫一支獨立 Python 腳本呼叫 Gemini 3.0：固定 prompt（例如「給我今日國際要聞摘要」），確認回傳 JSON。  
- 處理回傳格式，擷取文字並做簡單格式化，例如加上標題或 bullet。

### 第 5 小時：串接 LINE Bot + Gemini
- 在 webhook 內增加 `/daily_news` 路由或背景任務：定義一個函式呼叫 Gemini，然後用 LINE `push_message` 把文字發給自己。  
- 測試：手動觸發腳本（或呼叫 API）確定 message 可送到 LINE。  
- 若暫不部署雲端，可寫另一個 `scheduler.py`，直接調用 Gemini + push，不用 webhook。

### 第 6 小時：自動化與實際運用
- **排程**：  
  - 本機：Windows Task Scheduler 每天早上 08:00 執行 `python scheduler.py`（內含 Gemini 呼叫 + push）。  
  - 雲端：若要長期運作，可將程式部署到 Render/Heroku，並用平台提供的 cron job。  
- **安全**：確認 `.env` 未被提交；若上雲端，把金鑰設為平台環境變數。  
- **實戰檢查**：  
  - 測試每天任意時間手動執行是否能拿到最新新聞。  
  - 設計 prompt 時寫清楚：包含來源範圍、語言、想要的格式（例如三則要聞 + 一則延伸閱讀）。

---

## 學習成果（依完成度誠實評估）
| 項目 | 期待深度 | 實際掌握 |
| ---- | -------- | -------- |
| LINE Messaging API 帳號設定 | 能建立 Channel、配置 Webhook/Token | ✅ 可達成；文件簡單 |
| Gemini API 呼叫 | 能用 `requests` 發送 prompt | ✅ 基礎示範即可 |
| Flask Webhook | 了解 handler 流程、簽章驗證 | ⚠️ 需照文件一步步跟 | 
| 排程與部署 | 能在本機 Task Scheduler 跑每日任務；理解上雲需環境變數 | ⚠️ 若沒雲端經驗，可能只能先本機排程 |
| 安全與維運 | 知道 `.env`、GitHub 不留金鑰、必要時 rotate key | ✅ 觀念即可 |

> 若 6 小時內 Primarily 完成「本機排程 + push message」，即已達可用 MVP；雲端常駐與完整 webhook 可視時間延伸。

---

## 後續延伸建議
- 改善每日 prompt：加入 RSS/新聞 API 來源，或讓 Gemini 參考你整理的要點。  
- 增加使用者互動：例如輸入 `/world` / `/tech` 取得不同主題。  
- 將程式部署到安全的雲端環境（如 Render Free plan），並使用平台 Secrets 儲存金鑰。  
- 加上錯誤通知（Logging + 如果推送失敗，LINE bot 主動提醒）。


