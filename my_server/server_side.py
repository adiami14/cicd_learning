from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database
users = []

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({'error': 'Invalid data'}), 400
   
    users.append(data)
    return jsonify({'message': f"New user '{data['name']}' added successfully"}), 201


@app.route('/update_user', methods=['POST'])
def update_user():
    data = request.json
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({'error': 'Invalid data'}), 400
    
    name_to_remove = data['name']  # The last added data['name'], i.e., "asdas"
    if not any(user["name"] == name_to_remove for user in users):
        return jsonify({'error': 'User Do not exist'}), 404
        

    users = [user for user in users if user["name"] != name_to_remove]
    return jsonify({'message': f"New user '{data['name']}' updated successfully"}), 201

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({'users': users})



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
