from flask import Blueprint, request, jsonify
import pandas as pd
from services.user_service import create_user, delete_user, get_all_users, upload_users_from_csv

user_bp = Blueprint('user', __name__)

@user_bp.route('/user', methods=['POST'])
def create_user_route():
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

    user = create_user(name, age)
    if not user:
        return jsonify({"error": "User already exists"}), 400

    return jsonify(user.to_dict()), 200

@user_bp.route('/user/<string:name>', methods=['DELETE'])
def delete_user_route(name):
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
    user = delete_user(name)
    if user:
        return jsonify({"message": f"{name} deleted"}), 200
    return jsonify({"error": "User not found"}), 404

@user_bp.route('/users', methods=['GET'])
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
    users = get_all_users()
    return jsonify([user.to_dict() for user in users]), 200

@user_bp.route('/users/upload_csv', methods=['POST'])
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
    upload_users_from_csv(df)
    return jsonify({"message": "Users uploaded"}), 200

@user_bp.route('/users/average-age', methods=['GET'])
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
    users = get_all_users()
    df = pd.DataFrame([u.to_dict() for u in users])
    if df.empty:
        return jsonify({})
    df['group'] = df['name'].str[0].str.upper()
    result = df.groupby('group')['age'].mean().to_dict()
    return jsonify(result), 200
