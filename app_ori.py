from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger
import pandas as pd
import os

app = Flask(__name__)
swagger = Swagger(app)

# 設定 SQLite 資料庫路徑
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'users.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# 使用者模型
class User(db.Model):
    """
    User 資料表模型
    用來儲存使用者資料，包括名稱與年齡
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        """
        將 User 實例轉換為字典格式，以便 JSON 回應
        """
        return {"name": self.name, "age": self.age}

# 初始化資料庫
with app.app_context():
    db.create_all()

@app.route('/user', methods=['POST'])
def create_user():
    """
    創建一個新的使用者
    ---
    parameters:
      - in: body
        name: user
        required: true
        schema:
          type: object
          required:
            - name
            - age
          properties:
            name:
              type: string
            age:
              type: integer
    responses:
      200:
        description: User created successfully
        schema:
          type: object
          properties:
            name:
              type: string
            age:
              type: integer
      400:
        description: Invalid input or user already exists
    """
    data = request.get_json()
    name = data.get("name", "").strip()
    age = data.get("age")

    if not name or not isinstance(age, int):
        return jsonify({"error": "Invalid input"}), 400

    if User.query.filter_by(name=name).first():
        return jsonify({"error": "User already exists"}), 400

    new_user = User(name=name, age=age)
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.to_dict()), 200

@app.route('/user/<string:name>', methods=['DELETE'])
def delete_user(name):
    """
    刪除指定名稱的使用者
    ---
    parameters:
      - in: path
        name: name
        required: true
        type: string
        description: The name of the user to delete
    responses:
      200:
        description: User deleted successfully
      404:
        description: User not found
    """
    user = User.query.filter_by(name=name).first()
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": f"{name} deleted"}), 200
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/users', methods=['GET'])
def list_users():
    """
    列出所有已經註冊的使用者
    ---
    responses:
      200:
        description: A list of all users
        schema:
          type: array
          items:
            type: object
            properties:
              name:
                type: string
              age:
                type: integer
    """
    all_users = User.query.all()
    return jsonify([user.to_dict() for user in all_users]), 200

@app.route('/users/upload_csv', methods=['POST'])
def upload_csv():
    """
    上傳 CSV 檔案並批量新增使用者
    CSV 檔案應包含 `name` 和 `age` 欄位
    ---
    parameters:
      - in: formData
        name: file
        type: file
        required: true
        description: The CSV file containing user data
    responses:
      200:
        description: Users uploaded successfully
    """
    file = request.files['file']
    df = pd.read_csv(file)
    for _, row in df.iterrows():
        name = row['name']
        age = int(row['age'])
        if not User.query.filter_by(name=name).first():
            db.session.add(User(name=name, age=age))
    db.session.commit()
    return jsonify({"message": "Users uploaded"}), 200

@app.route('/users/average-age', methods=['GET'])
def average_age():
    """
    計算每個首字母群組的平均年齡
    ---
    responses:
      200:
        description: Average age by group
        schema:
          type: object
          additionalProperties:
            type: number
    """
    users = User.query.all()
    df = pd.DataFrame([u.to_dict() for u in users])
    if df.empty:
        return jsonify({})
    df['group'] = df['name'].str[0].str.upper()
    result = df.groupby('group')['age'].mean().to_dict()
    return jsonify(result), 200

if __name__ == '__main__':
    """
    啟動 Flask 伺服器，允許來自所有 IP 的連線
    """
    app.run(host='0.0.0.0', port=5000, debug=True)
