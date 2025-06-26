from flask import Flask
from config import Config
from models.user import db
from views.user_views import user_bp
from flasgger import Swagger

app = Flask(__name__)
app.config.from_object(Config)

# 註冊 Flasgger
swagger = Swagger(app)

# 初始化資料庫
db.init_app(app)

# 註冊藍圖
app.register_blueprint(user_bp)

# 啟動伺服器
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)
