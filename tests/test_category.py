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
