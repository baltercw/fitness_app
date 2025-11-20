os 模組提供與作業系統互動的工具，例如路徑處理。
`__file__` 代表目前檔案本身的路徑，用 `os.path.abspath(__file__)` 取得絕對路徑。
`os.path.dirname(...)` 可拿到所在資料夾並存成 `BASE_DIR`，當作其他檔案的起點。
`os.path.join(BASE_DIR, 'xxx')` 讓檔案路徑永遠以專案所在資料夾為基準，不怕換工作目錄。

