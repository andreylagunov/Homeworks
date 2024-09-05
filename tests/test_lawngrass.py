import pytest


def test_lawngrass_init(get_lawngrass):
    grass = get_lawngrass
    assert grass.name == "Газонная трава 2"
    assert grass.description == "Выносливая трава"
    assert grass.price == 450.0
    assert grass.quantity == 15
    assert grass.country == "США"
    assert grass.germination_period == "5 дней"
    assert grass.color == "Темно-зеленый"


def test_lawngrass_add___normal(get_lawngrass, get_lawngrass_2):
    assert get_lawngrass + get_lawngrass_2 == 16750.0


def test_lawngrass_add___error(get_lawngrass_2, get_smartphone):
    with pytest.raises(TypeError) as exception_info:
        res = get_lawngrass_2 + get_smartphone
    assert str(exception_info.value) == "Попытка сложения объектов различных типов."
