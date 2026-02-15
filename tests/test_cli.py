from unittest.mock import patch
import cli

@patch("cli.requests.get")
def test_list_items(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [
        {"id": 1, "product_name": "Test Item", "brand": "Brand", "price": 5.0, "stock": 2}
    ]
    cli.list_items()  # Should run without errors

@patch("cli.requests.post")
def test_add_item(mock_post):
    mock_post.return_value.status_code = 201
    mock_post.return_value.json.return_value = {"id": 1, "product_name": "New Product"}

    with patch("builtins.input", side_effect=["New Product", "Brand", "3.5", "10"]):
        cli.add_item()  # Should call post without errors
