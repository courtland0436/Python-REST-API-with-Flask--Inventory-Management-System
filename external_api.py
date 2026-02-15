# external_api.py
import requests

OPENFOODFACTS_SEARCH_URL = "https://world.openfoodfacts.org/cgi/search.pl"

def fetch_product_by_barcode(barcode):
    url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"
    response = requests.get(url)
    if response.ok and response.json().get("status") == 1:
        return response.json()["product"]
    return None

def fetch_product_by_name(name):
    params = {
        "search_terms": name,
        "search_simple": 1,
        "action": "process",
        "json": 1
    }
    response = requests.get(OPENFOODFACTS_SEARCH_URL, params=params)
    if response.ok:
        products = response.json().get("products", [])
        return products[0] if products else None
    return None
