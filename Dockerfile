# 使用官方 Python 3.10.18 基底映像檔
FROM python:3.10.18-slim

# 設定工作目錄
WORKDIR /app

# 複製要求檔案到容器中
COPY requirements.txt /app/requirements.txt

# 安裝必要的依賴包
RUN pip install --no-cache-dir -r requirements.txt

# 複製所有檔案到容器中
COPY . /app

# 修改 /app 目錄的權限，確保資料庫能夠創建和寫入
RUN chmod -R 777 /app

# 開放應用程式埠口
EXPOSE 5000

# 設定環境變數
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
# 設置環境變數來配置 SQLite 資料庫
ENV DATABASE_URL="sqlite:///users.db"

# 執行 Flask 應用程式
CMD ["flask", "run"]