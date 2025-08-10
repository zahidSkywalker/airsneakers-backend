from django.shortcuts import get_object_or_404
from .models import Product

def calculate_total(items):
    total = 0
    for item in items:
        prod = get_object_or_404(Product, pk=item['product_id'])
        total += float(prod.price) * int(item.get('qty', 1))
    return round(total,2)
