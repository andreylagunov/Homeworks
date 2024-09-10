from src.smartphone import Smartphone
from src.lawngrass import LawnGrass
from src.product import Product


def test_repr_mixin___for_smartphone(capsys):
    Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
               "S23 Ultra", 256, "Серый")
    message = capsys.readouterr()
    assert message.out.strip("\n") == "Smartphone('Samsung Galaxy S23 Ultra', '256GB, Серый цвет, 200MP камера', 180000.0, 5)"


def test_repr_mixin___for_lawngrass(capsys):
    LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    message = capsys.readouterr()
    assert message.out.strip("\n") == "LawnGrass('Газонная трава', 'Элитная трава для газона', 500.0, 20)"


def test_repr_mixin___for_product(capsys):
    Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    message = capsys.readouterr()
    assert message.out.strip("\n") == "Product('Xiaomi Redmi Note 11', '1024GB, Синий', 31000.0, 14)"
