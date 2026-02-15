# cli.py
import requests

API_URL = "http://localhost:5000/inventory"

def list_items():
    response = requests.get(API_URL)
    if response.ok:
        items = response.json()
        print("\n--- Current Inventory ---")
        for item in items:
            name = item.get('product_name', 'Unknown')
            brand = item.get('brand', 'N/A')
            price = item.get('price', 0.0)
            stock = item.get('stock', 0)
            print(f"ID {item['id']}: {name} ({brand}) - ${price} | Stock: {stock}")
    else:
        print("Error fetching inventory.")

def add_item():
    print("\n--- Add New Item ---")
    name = input("Product Name: ")
    brand = input("Brand: ")
    try:
        price = float(input("Price: "))
        stock = int(input("Stock: "))
        payload = {"product_name": name, "brand": brand, "price": price, "stock": stock}
        response = requests.post(API_URL, json=payload)
        if response.status_code == 201:
            print("Successfully added!")
    except ValueError:
        print("Invalid input for price or stock.")

def delete_item():
    item_id = input("\nEnter ID to delete: ")
    response = requests.delete(f"{API_URL}/{item_id}")
    if response.ok:
        print(f"Item {item_id} deleted.")

def main():
    while True:
        print("\n1. View Inventory\n2. Add Item\n3. Delete Item\n4. Exit")
        choice = input("Selection: ")
        if choice == "1": list_items()
        elif choice == "2": add_item()
        elif choice == "3": delete_item()
        elif choice == "4": break

if __name__ == "__main__":
    main()