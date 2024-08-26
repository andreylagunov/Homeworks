from src.product import Product
from src.category import Category


def test_category_obj_init(get_category_obj):
    assert get_category_obj.name == "Смартфоны"
    assert get_category_obj.description == ("Смартфоны, как средство не только коммуникации, "
                                            "но и получения дополнительных функций для удобства жизни")
    assert len(get_category_obj.products) == 10


def test_product_count_attr():
    prod_1 = Product("1", "1", 1, 1)
    prod_2 = Product("1", "1", 1, 1)
    prod_3 = Product("1", "1", 1, 1)
    categ_1 = Category("2", "2", [prod_1, prod_2, prod_3])
    assert Category.product_count == 13


def test_category_count_attr():
    categ_1 = Category("11", "11", [1, 2, 3])
    categ_2 = Category("22", "22", [11, 22, 33])
    assert Category.category_count == 4


def test_add_product___add_different_product(get_category_obj):
    category1 = get_category_obj
    assert category1.product_count == 29
    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)
    assert category1.product_count == 30


def test_add_product___add_the_same_product(get_category_obj):
    category1 = get_category_obj
    assert category1.product_count == 39
    product4 = Product("name_1", "des_1", 10_000, 1)
    category1.add_product(product4)
    assert category1.product_count == 39


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
