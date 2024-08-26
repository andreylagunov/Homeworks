
def test_product_obj_init(get_product_obj):
    assert get_product_obj.name == "name"
    assert get_product_obj.description == "des"
    assert get_product_obj.price == 10_000
    assert get_product_obj.quantity == 1