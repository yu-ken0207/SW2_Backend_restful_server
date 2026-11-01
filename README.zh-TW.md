# RESTful API 範例

[English](README.md) | **繁體中文**

這個專案提供一個簡單的基於 Flask 的 RESTful API，允許使用者執行 CRUD 操作來管理使用者資料。此應用程式允許你：

- 創建一個新的使用者
- 刪除已存在的使用者
- 取得所有使用者的列表
- 上傳 CSV 檔案批量創建使用者
- 計算每個首字母群組的平均年齡

## 快速開始

### 前置條件

需要安裝 Python 3.10 以上版本。建議使用虛擬環境來管理相依套件。

### 設定步驟

1. **建立虛擬環境（建議）**

    ```bash
    conda create -n restful_server python=3.10
    conda activate restful_server
    ```

2. **安裝所需的依賴套件**

    透過 `requirements.txt` 安裝必要的 Python 套件：

    ```bash
    pip install -r requirements.txt
    ```

### 執行應用程式

1. **運行伺服器**

    你可以在本地運行 Flask 應用程式，使用以下指令：

    ```bash
    python3 app.py
    ```

    API 將會在 `http://127.0.0.1:5000` 可供訪問。
    API 文件（Swagger UI）在 `http://127.0.0.1:5000/apidocs/`。

2. **使用 Docker 運行應用程式**

    若想在 Docker 容器中運行應用程式，可以按照以下步驟操作：

    - **建構 Docker 映像檔：**

      ```bash
      docker build -t restful-api .
      ```

    - **運行 Docker 容器：**

      ```bash
      docker run -p 5000:5000 -v $(pwd):/app restful-api
      ```

    這樣應用程式將會在 `http://127.0.0.1:5000` 可供訪問。

## API 端點

### 1. **創建一個新的使用者**  
   - **端點：** `POST /user`
   - **參數：**
     - `name`（字串，必填）
     - `age`（整數，必填）
   - **回應：**
     - `200 OK` 表示成功創建
     - `400 Bad Request` 表示輸入無效或使用者已存在

### 2. **刪除指定名稱的使用者**  
   - **端點：** `DELETE /user/<string:name>`
   - **參數：**
     - `name`（字串，必填）– 要刪除的使用者名稱
   - **回應：**
     - `200 OK` 表示成功刪除
     - `404 Not Found` 表示找不到使用者

### 3. **列出所有使用者**  
   - **端點：** `GET /users`
   - **回應：**
     - `200 OK` 返回所有使用者的列表

### 4. **上傳 CSV 檔案來批量新增使用者**  
   - **端點：** `POST /users/upload_csv`
   - **參數：**
     - `file`（檔案，必填）– 包含 `name` 和 `age` 欄位的 CSV 檔案
   - **回應：**
     - `200 OK` 表示成功上傳並創建使用者

### 5. **計算每個首字母群組的平均年齡**  
   - **端點：** `GET /users/average-age`
   - **回應：**
     - `200 OK` 返回各群組的平均年齡

## 專案結構

```plaintext
.
├── app.py               # Flask 應用程式的主程式
├── config.py            # 設定參數
├── models/              # 資料庫模型和架構
│   └── user.py
├── services/            # 用戶操作的邏輯
│   └── user_service.py
├── views/               # API 視圖/路由處理
│   └── user_views.py
├── tests/               # 單元測試
│   └── test_app.py
├── requirements.txt     # Python 相依套件
└── Dockerfile           # 用於容器化應用程式的 Dockerfile
