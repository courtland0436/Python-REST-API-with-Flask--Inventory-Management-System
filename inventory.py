# inventory.py

inventory = [
    {
        "id": 1,
        "product_name": "Organic Almond Milk",
        "brand": "Silk",
        "ingredients": "Filtered water, almonds, cane sugar",
        "price": 3.99,
        "stock": 10,
        "barcode": "1234567890123"
    }
]

def get_all_items():
    return inventory

def get_item_by_id(item_id):
    return next((item for item in inventory if item["id"] == item_id), None)

def add_item(item_data):
    # Ensure we generate a unique ID
    new_id = max([item["id"] for item in inventory], default=0) + 1
    item_data["id"] = new_id
    inventory.append(item_data)
    return item_data

def update_item(item_id, update_data):
    item = get_item_by_id(item_id)
    if item:
        # Don't allow the ID to be changed via PATCH
        update_data.pop("id", None)
        item.update(update_data)
        return item
    return None

def delete_item(item_id):
    global inventory
    # [:] modifies the list in-place so app.py sees the change
    inventory[:] = [item for item in inventory if item["id"] != item_id]
    return True