from .models import Product
from django.core.cache import cache


def get_products_by_category(category_id):
    """Возвращает все продукты в указанной категории."""
    return Product.objects.filter(category_id=category_id)

def get_products_by_category(category_id):
    """Возвращает продукты с кешированием."""
    cache_key = f"products_by_category_{category_id}"
    products = cache.get(cache_key)

    if products is None:
        products = list(Product.objects.filter(category_id=category_id))
        cache.set(cache_key, products, timeout=60 * 10)  # 10 минут

    return products
