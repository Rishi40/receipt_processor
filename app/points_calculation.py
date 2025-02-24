import math

def calculate_points(receipt):
    points = 0
    retailer = receipt["retailer"]
    total = float(receipt["total"])
    purchase_date = int(receipt["purchaseDate"].split("-")[-1])
    purchase_time = int(receipt["purchaseTime"].split(":")[0])
    
    for c in retailer:
        if c.isalnum():
            points += 1

    if total.is_integer():
        points += 50

    if total % 0.25 == 0:
        points += 25

    points += (len(receipt["items"]) // 2) * 5

    for item in receipt["items"]:
        if len(item["shortDescription"].strip()) % 3 == 0:
            points += math.ceil(float(item["price"]) * 0.2)

    if purchase_date % 2 == 1:
        points += 6

    if 14 <= purchase_time < 16:
        points += 10

    return points
