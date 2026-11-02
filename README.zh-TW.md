# RESTful API 範例

[English](README.md) | **繁體中文**

用 Flask 寫的簡單 RESTful API 範例，可以新增、查詢、刪除使用者資料（CRUD），附 Docker 設定。可以：

- 新增使用者
- 刪除已存在的使用者
- 取得所有使用者的清單
- 上傳 CSV 檔案批次新增使用者
- 計算每個首字母群組的平均年齡

## 快速開始

### 需要準備

需要安裝 Python 3.10 以上版本。建議使用虛擬環境來管理相依套件。

### 設定步驟

1. **建立虛擬環境（建議）**

    ```bash
    conda create -n restful_server python=3.10
    conda activate restful_server
    ```

2. **安裝需要的套件**

    透過 `requirements.txt` 安裝必要的 Python 套件：

    ```bash
    pip install -r requirements.txt
    ```

### 執行應用程式

1. **執行伺服器**

    用下面的指令在本機執行：

    ```bash
    python3 app.py
    ```

    API 會開在 `http://127.0.0.1:5000`。
    API 文件（Swagger UI）在 `http://127.0.0.1:5000/apidocs/`。

2. **用 Docker 執行**

    要用 Docker 執行的話：

    - **建置 Docker 映像檔：**

      ```bash
      docker build -t restful-api .
      ```

    - **執行 Docker 容器：**

      ```bash
      docker run -p 5000:5000 -v $(pwd):/app restful-api
      ```

    應用程式一樣會開在 `http://127.0.0.1:5000`。

## API 端點

### 1. 新增使用者
   - **端點：** `POST /user`
   - **參數：**
     - `name`（字串，必填）
     - `age`（整數，必填）
   - **回應：**
     - `200 OK` 表示新增成功
     - `400 Bad Request` 表示輸入無效或使用者已存在

### 2. 刪除指定名稱的使用者
   - **端點：** `DELETE /user/<string:name>`
   - **參數：**
     - `name`（字串，必填）– 要刪除的使用者名稱
   - **回應：**
     - `200 OK` 表示成功刪除
     - `404 Not Found` 表示找不到使用者

### 3. 列出所有使用者
   - **端點：** `GET /users`
   - **回應：**
     - `200 OK` 回傳所有使用者的清單

### 4. 上傳 CSV 檔案批次新增使用者
   - **端點：** `POST /users/upload_csv`
   - **參數：**
     - `file`（檔案，必填）– 包含 `name` 和 `age` 欄位的 CSV 檔案
   - **回應：**
     - `200 OK` 表示上傳成功並新增使用者

### 5. 計算每個首字母群組的平均年齡
   - **端點：** `GET /users/average-age`
   - **回應：**
     - `200 OK` 回傳各群組的平均年齡

## 專案結構

```plaintext
.
├── app.py               # Flask 應用程式的主程式
├── config.py            # 設定參數
├── models/              # 資料庫模型和架構
│   └── user.py
├── services/            # 使用者相關的處理邏輯
│   └── user_service.py
├── views/               # API 視圖/路由處理
│   └── user_views.py
├── tests/               # 單元測試
│   └── test_app.py
├── requirements.txt     # Python 相依套件
└── Dockerfile           # 用於容器化應用程式的 Dockerfile
