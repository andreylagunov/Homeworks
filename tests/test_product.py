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
