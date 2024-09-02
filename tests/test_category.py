from src.product import Product
from src.category import Category
import pytest


def test_category_obj_init(get_category_obj):
    assert get_category_obj.name == "Смартфоны"
    assert get_category_obj.description == ("Смартфоны, как средство не только коммуникации, "
                                            "но и получения дополнительных функций для удобства жизни")
    assert len(get_category_obj.products) == 10


def test_product_count_attr():
    Category.product_count = 0
    prod_1 = Product("1", "1", 1, 1)
    prod_2 = Product("1", "1", 1, 1)
    prod_3 = Product("1", "1", 1, 1)
    categ_1 = Category("2", "2", [prod_1, prod_2, prod_3])
    assert Category.product_count == 3


def test_category_count_attr():
    Category.category_count = 0
    categ_1 = Category("11", "11", [1, 2, 3])
    categ_2 = Category("22", "22", [11, 22, 33])
    assert Category.category_count == 2


def test_add_product___add_different_product(get_category_obj):
    Category.product_count = 0
    category1 = get_category_obj
    assert Category.product_count == 0
    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)
    assert Category.product_count == 1
    product5 = Product("55\" QLED 8K", "Фоновая подсветка", 223000.0, 7)
    category1.add_product(product5)
    assert Category.product_count == 2
    Category.product_count = 0


def test_add_product___add_the_same_product(get_category_obj):
    category1 = get_category_obj
    assert Category.product_count == 10
    product4 = Product("name_1", "des_1", 10_000, 1)
    category1.add_product(product4)
    assert Category.product_count == 10
    Category.product_count = 0


def test_add_product___add_not_a_product(get_category_obj):
    with pytest.raises(TypeError) as exception_info:
        category1 = get_category_obj
        category1.add_product("not a product")
    assert str(exception_info.value) == "Попытка добавления в категорию объекта не типа Product."
    Category.product_count = 0


def test_add_product___add_obj_of_product_class(get_category_obj, get_smartphone):
    assert Category.product_count == 10
    category1 = get_category_obj
    category1.add_product(get_smartphone)
    assert Category.product_count == 11
    Category.product_count = 0


def test_products_property():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    # product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category2 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1]
    )
    assert category2.products == [
      'Samsung Galaxy S23 Ultra, 180000.0 руб, Остаток: 5 шт.',
      # 'Iphone 15, 210000.0 руб, Остаток: 8 шт.',
      # 'Xiaomi Redmi Note 11, 31000.0 руб, Остаток: 14 шт.'
    ]
    category2.add_product(product2)
    assert category2.products == [
      'Samsung Galaxy S23 Ultra, 180000.0 руб, Остаток: 5 шт.',
      'Iphone 15, 210000.0 руб, Остаток: 8 шт.',
      # 'Xiaomi Redmi Note 11, 31000.0 руб, Остаток: 14 шт.'
    ]

def test__str__method(get_category_obj):
    category = get_category_obj
    assert str(category) == "Смартфоны, количество продуктов: 45 шт."
