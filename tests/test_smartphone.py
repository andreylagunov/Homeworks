import pytest


def test_smartphone_init(get_smartphone):
    phone = get_smartphone
    assert phone.name == "Samsung Galaxy S23 Ultra"
    assert phone.description == "256GB, Серый цвет, 200MP камера"
    assert phone.price == 180000.0
    assert phone.quantity == 5
    assert phone.efficiency == 95.5
    assert phone.model == "S23 Ultra"
    assert phone.memory == 256
    assert phone.color == "Серый"


def test_smartphone_add___normal(get_smartphone, get_smartphone_2):
    assert get_smartphone + get_smartphone_2 == 2580000.0


def test_smartphone_add___error(get_smartphone, get_lawngrass):
    with pytest.raises(TypeError) as exception_info:
        res = get_smartphone + get_lawngrass
    assert str(exception_info.value) == "Попытка сложения объектов различных типов."
