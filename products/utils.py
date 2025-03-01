import requests
#
#
# def fetch_products():
#     url = "https://api.example.com"
#
#     response = requests.get(url)
#     if response.status_code == 200:
#         return response.json()
#
#     return []


def fetch_products():
    # Simulate API response
    return [
        {
            "name": "Product 1",
            "description": "This is a great product.",
            "price": 29.99,
            "image_url": "https://via.placeholder.com/150",
            "affiliate_link": "https://example.com/product/1?ref=your-affiliate-id"
        },
        {
            "name": "Product 2",
            "description": "Another amazing product.",
            "price": 49.99,
            "image_url": "https://via.placeholder.com/150",
            "affiliate_link": "https://example.com/product/2?ref=your-affiliate-id"
        }
    ]