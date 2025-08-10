from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data (in-memory store)
items = [
    {"id": 1, "name": "Item One"},
    {"id": 2, "name": "Item Two"}
]

# GET all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items), 200

# GET single item by ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item:
        return jsonify(item), 200
    return jsonify({"error": "Item not found"}), 404

# POST - Create new item
@app.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    if not data or "name" not in data:
        return jsonify({"error": "Name is required"}), 400

    new_item = {
        "id": items[-1]["id"] + 1 if items else 1,
        "name": data["name"]
    }
    items.append(new_item)
    return jsonify(new_item), 201

# PUT - Update item by ID
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if not item:
        return jsonify({"error": "Item not found"}), 404

    data = request.get_json()
    if not data or "name" not in data:
        return jsonify({"error": "Name is required"}), 400

    item["name"] = data["name"]
    return jsonify(item), 200

# DELETE - Remove item by ID
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item["id"] != item_id]
    return jsonify({"message": "Item deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
