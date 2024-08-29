from src.product import Product
from src.category import Category
import pytest


@pytest.fixture
def get_product_obj():
    return Product(f"name", f"des", 10_000, 1)


@pytest.fixture
def get_category_obj():
    return Category(
        "Смартфоны",
     "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
     [Product(f"name_{i}", f"des_{i}", i * 10_000, i) for i in range(10)]
    )

@pytest.fixture
def get_category_obj___for_product_iterator():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category_1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )
    return category_1
