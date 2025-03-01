from django.shortcuts import render
from django.http import JsonResponse
import random

def fetch_products(category=None):
    # Simulate API response with 30 products
    products = [
        {
            "name": "Organic Apples",
            "description": "Fresh and organic apples from local farms.",
            "price": 5.99,
            "image_url": "https://via.placeholder.com/150",
            "affiliate_link": "https://example.com/product/1?ref=your-affiliate-id",
            "rating": 4.5,
            "popularity": 8,
            "category": "groceries"
        },
        {
            "name": "Whole Grain Bread",
            "description": "Healthy whole grain bread with no preservatives.",
            "price": 3.99,
            "image_url": "https://via.placeholder.com/150",
            "affiliate_link": "https://example.com/product/2?ref=your-affiliate-id",
            "rating": 4.2,
            "popularity": 7,
            "category": "groceries"
        },
        {
            "name": "Organic Milk",
            "description": "Fresh organic milk from grass-fed cows.",
            "price": 4.49,
            "image_url": "https://via.placeholder.com/150",
            "affiliate_link": "https://example.com/product/3?ref=your-affiliate-id",
            "rating": 4.7,
            "popularity": 9,
            "category": "groceries"
        },
        {
            "name": "Free-Range Eggs",
            "description": "Farm-fresh free-range eggs.",
            "price": 6.99,
            "image_url": "https://via.placeholder.com/150",
            "affiliate_link": "https://example.com/product/4?ref=your-affiliate-id",
            "rating": 4.6,
            "popularity": 8,
            "category": "groceries"
        },
        {
            "name": "Organic Spinach",
            "description": "Fresh organic spinach packed with nutrients.",
            "price": 2.99,
            "image_url": "https://via.placeholder.com/150",
            "affiliate_link": "https://example.com/product/5?ref=your-affiliate-id",
            "rating": 4.4,
            "popularity": 7,
            "category": "groceries"
        },
        {
            "name": "Blender Pro 5000",
            "description": "High-performance blender for all your kitchen needs.",
            "price": 129.99,
            "image_url": "https://via.placeholder.com/150",
            "affiliate_link": "https://example.com/product/6?ref=your-affiliate-id",
            "rating": 4.8,
            "popularity": 9,
            "category": "machines"
        },
        {
            "name": "Coffee Maker Elite",
            "description": "Brew the perfect cup of coffee every time.",
            "price": 89.99,
            "image_url": "https://via.placeholder.com/150",
            "affiliate_link": "https://example.com/product/7?ref=your-affiliate-id",
            "rating": 4.6,
            "popularity": 8,
            "category": "machines"
        },
        {
            "name": "Air Fryer Deluxe",
            "description": "Healthy frying with less oil and more flavor.",
            "price": 99.99,
            "image_url": "https://via.placeholder.com/150",
            "affiliate_link": "https://example.com/product/8?ref=your-affiliate-id",
            "rating": 4.7,
            "popularity": 9,
            "category": "machines"
        },
        {
            "name": "Food Processor Max",
            "description": "Chop, slice, and dice with ease.",
            "price": 79.99,
            "image_url": "https://via.placeholder.com/150",
            "affiliate_link": "https://example.com/product/9?ref=your-affiliate-id",
            "rating": 4.5,
            "popularity": 8,
            "category": "machines"
        },
        {
            "name": "Stand Mixer Pro",
            "description": "Powerful stand mixer for baking enthusiasts.",
            "price": 199.99,
            "image_url": "https://via.placeholder.com/150",
            "affiliate_link": "https://example.com/product/10?ref=your-affiliate-id",
            "rating": 4.9,
            "popularity": 10,
            "category": "machines"
        },
        {
            "name": "Wireless Earbuds",
            "description": "High-quality sound with noise cancellation.",
            "price": 59.99,
            "image_url": "https://via.placeholder.com/150",
            "affiliate_link": "https://example.com/product/11?ref=your-affiliate-id",
            "rating": 4.3,
            "popularity": 7,
            "category": "accessories"
        },
        {
            "name": "Smartwatch X200",
            "description": "Track your fitness and stay connected.",
            "price": 149.99,
            "image_url": "https://via.placeholder.com/150",
            "affiliate_link": "https://example.com/product/12?ref=your-affiliate-id",
            "rating": 4.6,
            "popularity": 8,
            "category": "accessories"
        },
        {
            "name": "Bluetooth Speaker",
            "description": "Portable speaker with crystal-clear sound.",
            "price": 39.99,
            "image_url": "https://via.placeholder.com/150",
            "affiliate_link": "https://example.com/product/13?ref=your-affiliate-id",
            "rating": 4.4,
            "popularity": 7,
            "category": "accessories"
        },
        {
            "name": "Laptop Stand",
            "description": "Ergonomic stand for your laptop.",
            "price": 29.99,
            "image_url": "https://via.placeholder.com/150",
            "affiliate_link": "https://example.com/product/14?ref=your-affiliate-id",
            "rating": 4.2,
            "popularity": 6,
            "category": "accessories"
        },
        {
            "name": "Wireless Charger",
            "description": "Fast and convenient wireless charging.",
            "price": 19.99,
            "image_url": "https://via.placeholder.com/150",
            "affiliate_link": "https://example.com/product/15?ref=your-affiliate-id",
            "rating": 4.5,
            "popularity": 8,
            "category": "accessories"
        },
        {
            "name": "Organic Bananas",
            "description": "Sweet and organic bananas.",
            "price": 1.99,
            "image_url": "https://via.placeholder.com/150",
            "affiliate_link": "https://example.com/product/16?ref=your-affiliate-id",
            "rating": 4.7,
            "popularity": 9,
            "category": "groceries"
        },
        {
            "name": "Organic Carrots",
            "description": "Fresh and crunchy organic carrots.",
            "price": 2.49,
            "image_url": "https://via.placeholder.com/150",
            "affiliate_link": "https://example.com/product/17?ref=your-affiliate-id",
            "rating": 4.6,
            "popularity": 8,
            "category": "groceries"
        },
        {
            "name": "Organic Strawberries",
            "description": "Juicy and sweet organic strawberries.",
            "price": 4.99,
            "image_url": "https://via.placeholder.com/150",
            "affiliate_link": "https://example.com/product/18?ref=your-affiliate-id",
            "rating": 4.8,
            "popularity": 9,
            "category": "groceries"
        },
        {
            "name": "Organic Tomatoes",
            "description": "Fresh and ripe organic tomatoes.",
            "price": 3.49,
            "image_url": "https://via.placeholder.com/150",
            "affiliate_link": "https://example.com/product/19?ref=your-affiliate-id",
            "rating": 4.5,
            "popularity": 7,
            "category": "groceries"
        },
        {
            "name": "Organic Potatoes",
            "description": "Versatile and organic potatoes.",
            "price": 2.99,
            "image_url": "https://via.placeholder.com/150",
            "affiliate_link": "https://example.com/product/20?ref=your-affiliate-id",
            "rating": 4.4,
            "popularity": 7,
            "category": "groceries"
        },
        {
            "name": "Rice Cooker Pro",
            "description": "Cook perfect rice every time.",
            "price": 49.99,
            "image_url": "https://via.placeholder.com/150",
            "affiliate_link": "https://example.com/product/21?ref=your-affiliate-id",
            "rating": 4.6,
            "popularity": 8,
            "category": "machines"
        },
        {
            "name": "Juicer Max",
            "description": "Extract fresh juice from fruits and vegetables.",
            "price": 79.99,
            "image_url": "https://via.placeholder.com/150",
            "affiliate_link": "https://example.com/product/22?ref=your-affiliate-id",
            "rating": 4.5,
            "popularity": 7,
            "category": "machines"
        },
        {
            "name": "Toaster Oven",
            "description": "Compact toaster oven for quick meals.",
            "price": 59.99,
            "image_url": "https://via.placeholder.com/150",
            "affiliate_link": "https://example.com/product/23?ref=your-affiliate-id",
            "rating": 4.4,
            "popularity": 7,
            "category": "machines"
        },
        {
            "name": "Electric Kettle",
            "description": "Boil water quickly and efficiently.",
            "price": 29.99,
            "image_url": "https://via.placeholder.com/150",
            "affiliate_link": "https://example.com/product/24?ref=your-affiliate-id",
            "rating": 4.7,
            "popularity": 8,
            "category": "machines"
        },
        {
            "name": "Hand Mixer",
            "description": "Lightweight and powerful hand mixer.",
            "price": 39.99,
            "image_url": "https://via.placeholder.com/150",
            "affiliate_link": "https://example.com/product/25?ref=your-affiliate-id",
            "rating": 4.3,
            "popularity": 6,
            "category": "machines"
        },
        {
            "name": "Phone Case",
            "description": "Durable and stylish phone case.",
            "price": 14.99,
            "image_url": "https://via.placeholder.com/150",
            "affiliate_link": "https://example.com/product/26?ref=your-affiliate-id",
            "rating": 4.2,
            "popularity": 6,
            "category": "accessories"
        },
        {
            "name": "Laptop Bag",
            "description": "Sleek and functional laptop bag.",
            "price": 49.99,
            "image_url": "https://via.placeholder.com/150",
            "affiliate_link": "https://example.com/product/27?ref=your-affiliate-id",
            "rating": 4.5,
            "popularity": 7,
            "category": "accessories"
        },
        {
            "name": "Power Bank",
            "description": "Portable charger for your devices.",
            "price": 24.99,
            "image_url": "https://via.placeholder.com/150",
            "affiliate_link": "https://example.com/product/28?ref=your-affiliate-id",
            "rating": 4.4,
            "popularity": 7,
            "category": "accessories"
        },
        {
            "name": "Headphones",
            "description": "Comfortable and high-quality headphones.",
            "price": 69.99,
            "image_url": "https://via.placeholder.com/150",
            "affiliate_link": "https://example.com/product/29?ref=your-affiliate-id",
            "rating": 4.6,
            "popularity": 8,
            "category": "accessories"
        },
        {
            "name": "Tablet Stand",
            "description": "Adjustable stand for your tablet.",
            "price": 19.99,
            "image_url": "https://via.placeholder.com/150",
            "affiliate_link": "https://example.com/product/30?ref=your-affiliate-id",
            "rating": 4.3,
            "popularity": 6,
            "category": "accessories"
        }
    ]

    if category:
        return [product for product in products if product["category"] == category]
    return products

def product_list(request):
    category = request.GET.get('category', None)
    products = fetch_products(category)
    return render(request, 'products/product_list.html', {'products': products})

def load_more_products(request):
    offset = int(request.GET.get('offset', 0))
    limit = 6  # Number of products to load per request
    category = request.GET.get('category', None)
    products = fetch_products(category)[offset:offset + limit]
    return JsonResponse({"products": products})