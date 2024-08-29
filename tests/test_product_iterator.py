# from src.product import Product
# from src.category import Category
from src.product_iterator import ProductIterator


def test__iter__next__methods(get_category_obj___for_product_iterator):
    category_1 = get_category_obj___for_product_iterator

    prod_iterator = iter(ProductIterator(category_1))
    assert next(prod_iterator) == "Samsung Galaxy S23 Ultra, 180000.0 руб, Остаток: 5 шт."
    assert next(prod_iterator) == "Iphone 15, 210000.0 руб, Остаток: 8 шт."
    assert next(prod_iterator) == "Xiaomi Redmi Note 11, 31000.0 руб, Остаток: 14 шт."


def test_for_cycle(get_category_obj___for_product_iterator):
    category_1 = get_category_obj___for_product_iterator

    for prod in ProductIterator(category_1):
        assert type(str(prod)) is str
