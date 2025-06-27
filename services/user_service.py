from models.user import get_db, to_dict

def create_user(name, age):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM user WHERE name = ?', (name,))
    existing_user = cursor.fetchone()
    if existing_user:
        conn.close()
        return None  # 使用者已存在
    cursor.execute('INSERT INTO user (name, age) VALUES (?, ?)', (name, age))
    conn.commit()
    conn.close()
    return {"name": name, "age": age}

def delete_user(name):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM user WHERE name = ?', (name,))
    user = cursor.fetchone()
    if user:
        cursor.execute('DELETE FROM user WHERE name = ?', (name,))
        conn.commit()
        conn.close()
        return to_dict(user)
    conn.close()
    return None

def get_all_users():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM user')
    users = cursor.fetchall()
    conn.close()
    return [to_dict(user) for user in users]

def upload_users_from_csv(df):
    conn = get_db()
    cursor = conn.cursor()
    for _, row in df.iterrows():
        name = row['Name']
        age = int(row['Age'])
        cursor.execute('SELECT * FROM user WHERE name = ?', (name,))
        if not cursor.fetchone():
            cursor.execute('INSERT INTO user (name, age) VALUES (?, ?)', (name, age))
    conn.commit()
    conn.close()
