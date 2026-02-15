import pytest
from unittest.mock import patch
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_all_items(client):
    response = client.get("/inventory")
    assert response.status_code == 200
    assert isinstance(response.json, list)

@patch("app.fetch_product_by_name")
def test_add_item(mock_fetch, client):
    mock_fetch.return_value = None  # Prevent enrichment

    new_item = {
        "product_name": "Test Product",
        "brand": "Test Brand",
        "price": 9.99,
        "stock": 5
    }
    response = client.post("/inventory", json=new_item)
    assert response.status_code == 201
    assert response.json["product_name"] == "Test Product"

@patch("app.fetch_product_by_name")
def test_update_item(mock_fetch, client):
    mock_fetch.return_value = None

    new_item = {"product_name": "Update Me", "brand": "Brand", "price": 1.0, "stock": 1}
    add_response = client.post("/inventory", json=new_item)
    item_id = add_response.json["id"]

    update_data = {"price": 2.5}
    response = client.patch(f"/inventory/{item_id}", json=update_data)
    assert response.status_code == 200
    assert response.json["price"] == 2.5

@patch("app.fetch_product_by_name")
def test_delete_item(mock_fetch, client):
    mock_fetch.return_value = None

    new_item = {"product_name": "Delete Me", "brand": "Brand", "price": 1.0, "stock": 1}
    add_response = client.post("/inventory", json=new_item)
    item_id = add_response.json["id"]

    response = client.delete(f"/inventory/{item_id}")
    assert response.status_code == 200
    assert "message" in response.json
