# app.py
from flask import Flask, jsonify, request, render_template
from inventory import get_all_items, get_item_by_id, add_item, update_item, delete_item
from external_api import fetch_product_by_name

app = Flask(__name__)

# --- Frontend Route ---
@app.route("/")
def index():
    """Serves the index.html file from the /templates folder"""
    return render_template("index.html")

# --- API Routes ---
@app.route("/inventory", methods=["GET"])
def list_inventory():
    return jsonify(get_all_items()), 200

@app.route("/inventory", methods=["POST"])
def create_item():
    data = request.json
    
    # Enrichment Logic: Use the product name to find more details
    external_data = fetch_product_by_name(data.get("product_name"))
    if external_data:
        # Map OpenFoodFacts 'brands' to our internal 'brand'
        if "brands" in external_data and not data.get("brand"):
            data["brand"] = external_data["brands"]
        # Map ingredients
        if "ingredients_text" in external_data:
            data["ingredients"] = external_data["ingredients_text"]
            
    item = add_item(data)
    return jsonify(item), 201

@app.route("/inventory/<int:item_id>", methods=["PATCH"])
def modify_item(item_id):
    data = request.json
    item = update_item(item_id, data)
    if item:
        return jsonify(item), 200
    return jsonify({"error": "Item not found"}), 404

@app.route("/inventory/<int:item_id>", methods=["DELETE"])
def remove_item(item_id):
    delete_item(item_id)
    return jsonify({"message": "Item deleted"}), 200

if __name__ == "__main__":
    # Standard Flask port. Ensure this matches your CLI.py constant.
    app.run(debug=True, port=5000)