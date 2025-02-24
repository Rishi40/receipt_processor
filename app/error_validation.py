import re
from datetime import datetime

def validate_receipt(data: dict):
    required_fields = ['retailer', 'purchaseDate', 'purchaseTime', 'items', 'total']
    for field in required_fields:
        if field not in data:
            return None, f"Missing required field '{field}'."

    retailer = data['retailer']
    if not isinstance(retailer, str) or not re.fullmatch(r'^[\w\s\-&]+$', retailer):
        return None, "Invalid retailer format."

    purchaseDate = data['purchaseDate']
    if not isinstance(purchaseDate, str):
        return None, "purchaseDate must be a string."
    try:
        datetime.strptime(purchaseDate, "%Y-%m-%d")
    except ValueError:
        return None, "purchaseDate must be in YYYY-MM-DD format."

    purchaseTime = data['purchaseTime']
    if not isinstance(purchaseTime, str):
        return None, "purchaseTime must be a string."
    try:
        datetime.strptime(purchaseTime, "%H:%M")
    except ValueError:
        return None, "purchaseTime must be in HH:MM 24-hour format."

    total = data['total']
    if not isinstance(total, str) or not re.fullmatch(r'^\d+\.\d{2}$', total):
        return None, "Invalid total format."

    items = data['items']
    if not isinstance(items, list) or len(items) == 0:
        return None, "Items must be a non-empty list."

    for idx, item in enumerate(items):
        if not isinstance(item, dict):
            return None, f"Item at index {idx} is not an object."
        if 'shortDescription' not in item or 'price' not in item:
            return None, f"Item at index {idx} is missing required fields."

        short_desc = item['shortDescription']
        if not isinstance(short_desc, str) or not re.fullmatch(r'^[\w\s\-]+$', short_desc):
            return None, f"Invalid shortDescription format for item at index {idx}."

        price = item['price']
        if not isinstance(price, str) or not re.fullmatch(r'^\d+\.\d{2}$', price):
            return None, f"Invalid price format for item at index {idx}."

    return data, None
