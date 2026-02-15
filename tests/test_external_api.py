from unittest.mock import patch
from external_api import fetch_product_by_barcode, fetch_product_by_name

@patch("external_api.requests.get")
def test_fetch_product_by_barcode(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "status": 1,
        "product": {
            "product_name": "Mock Milk",
            "brands": "Mock Brand",
            "ingredients_text": "Water, Sugar"
        }
    }
    product = fetch_product_by_barcode("123456789")
    assert product["product_name"] == "Mock Milk"

@patch("external_api.requests.get")
def test_fetch_product_by_name(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "products": [
            {"product_name": "Mock Juice", "brands": "Mock Brand", "ingredients_text": "Apple, Water", "code": "987654321"}
        ]
    }
    product = fetch_product_by_name("Juice")
    assert product["product_name"] == "Mock Juice"
