from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Connect to the SQLite database
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# Create a table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT,
                  email TEXT)''')
conn.commit()

@app.route('/users', methods=['GET'])
def get_all_users():
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    return jsonify({'users': [dict(row) for row in users]})

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    cursor.execute('SELECT * FROM users WHERE id=?', (user_id,))
    user = cursor.fetchone()
    if user:
        return jsonify({'user': dict(user)})
    else:
        return jsonify({'message': 'User not found'}), 404

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')

    if not name or not email:
        return jsonify({'message': 'Name and email are required'}), 400

    cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))
    conn.commit()
    return jsonify({'message': 'User created successfully'}), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')

    if not name and not email:
        return jsonify({'message': 'At least one field to update is required'}), 400

    cursor.execute('UPDATE users SET name=?, email=? WHERE id=?', (name, email, user_id))
    conn.commit()

    rows_affected = cursor.rowcount
    if rows_affected == 0:
        return jsonify({'message': 'User not found'}), 404
    else:
        return jsonify({'message': 'User updated successfully'})

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    cursor.execute('DELETE FROM users WHERE id=?', (user_id,))
    conn.commit()

    rows_affected = cursor.rowcount
    if rows_affected == 0:
        return jsonify({'message': 'User not found'}), 404
    else:
        return jsonify({'message': 'User deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)