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
