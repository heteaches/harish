from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data store
items = []
next_id = 1

# GET /items - List all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

# GET /items/<id> - Get one item by ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        return jsonify(item)
    return jsonify({'error': 'Item not found'}), 404

# POST /items - Create a new item
@app.route('/items', methods=['POST'])
def create_item():
    global next_id
    data = request.get_json()
    item = {
        'id': next_id,
        'name': data['name']
    }
    items.append(item)
    next_id += 1
    return jsonify(item), 201

# PUT /items/<id> - Update an existing item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()
    for item in items:
        if item['id'] == item_id:
            item['name'] = data['name']
            return jsonify(item)
    return jsonify({'error': 'Item not found'}), 404

# DELETE /items/<id> - Delete an item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        items = [item for item in items if item['id'] != item_id]
        return jsonify({'message': 'Item deleted'})
    return jsonify({'error': 'Item not found'}), 404

# Run the server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
