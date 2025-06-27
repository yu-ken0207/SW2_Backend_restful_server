from flask import Flask
from config import Config
from views.user_views import user_bp
from flasgger import Swagger
from models.user import create_tables

app = Flask(__name__)
app.config.from_object(Config)

# 註冊 Flasgger
swagger = Swagger(app)

# 初始化 SQLite 資料表
create_tables()

# 註冊藍圖
app.register_blueprint(user_bp)

# 啟動伺服器
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
