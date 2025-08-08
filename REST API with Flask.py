from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory user storage
users = {}
user_id_counter = 1

# GET all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(list(users.values())), 200

# GET a specific user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404

# POST to create a new user
@app.route('/users', methods=['POST'])
def create_user():
    global user_id_counter
    data = request.get_json()
    
    if not data or not data.get('name') or not data.get('email'):
        return jsonify({"error": "Name and email are required"}), 400
        
    user = {
        "id": user_id_counter,
        "name": data['name'],
        "email": data['email']
    }
    
    users[user_id_counter] = user
    user_id_counter += 1
    return jsonify(user), 201

# PUT to update an existing user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
        
    data = request.get_json()
    if not data or not data.get('name') or not data.get('email'):
        return jsonify({"error": "Name and email are required"}), 400
        
    users[user_id].update({
        "name": data['name'],
        "email": data['email']
    })
    return jsonify(users[user_id]), 200

# DELETE a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
        
    deleted_user = users.pop(user_id)
    return jsonify(deleted_user), 200

if __name__ == '__main__':
    app.run(debug=True)