import pytest

from src.product import Product

def test_product_obj_init(get_product_obj):
    assert get_product_obj.name == "name"
    assert get_product_obj.description == "des"
    assert get_product_obj.price == 10_000
    assert get_product_obj.quantity == 1

def test_new_product___classmethod():
    new_product = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
         "quantity": 5})
    assert new_product.name == "Samsung Galaxy S23 Ultra"
    assert new_product.description == "256GB, Серый цвет, 200MP камера"
    assert new_product.price == 180000.0
    assert new_product.quantity == 5


def test_price___getter():
    new_product = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
         "quantity": 5})
    assert new_product.price == 180000.0


def test_price___setter_with_zero_price():
    new_product = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 280000.0,
         "quantity": 5})
    assert new_product.price == 280000.0
    new_product.price = 0.0
    assert new_product.price == 280000.0


def test_price___setter_with_negative_price():
    new_product = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 280000.0,
         "quantity": 5})
    assert new_product.price == 280000.0
    new_product.price = -500_000.0
    assert new_product.price == 280000.0


def test__str__method():
    product1 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product2 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    assert str(product1) == "Iphone 15, 210000.0 руб. Остаток: 8 шт."
    assert str(product2) == "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."


def test__add__method():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 100_000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 200_000.0, 5)

    assert (product1 + product2) == 1_500_000.0


def test_product_creation_with_zero_quantity():
    with pytest.raises(ValueError) as exception_info:
        product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)
    assert str(exception_info.value) == "Товар с нулевым количеством не может быть добавлен."

