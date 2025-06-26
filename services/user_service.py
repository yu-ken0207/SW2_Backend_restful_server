from models.user import User, db

def create_user(name, age):
    if User.query.filter_by(name=name).first():
        return None  # 使用者已存在
    new_user = User(name=name, age=age)
    db.session.add(new_user)
    db.session.commit()
    return new_user

def delete_user(name):
    user = User.query.filter_by(name=name).first()
    if user:
        db.session.delete(user)
        db.session.commit()
        return user
    return None

def get_all_users():
    return User.query.all()

def upload_users_from_csv(df):
    for _, row in df.iterrows():
        name = row['name']
        age = int(row['age'])
        if not User.query.filter_by(name=name).first():
            db.session.add(User(name=name, age=age))
    db.session.commit()
