import os
from src.json_to_objects import read_json
from src.json_to_objects import validate_json_data
from src.json_to_objects import get_objects_based_on
from src.product import Product
from src.category import Category
from pytest import raises


directory = os.getcwd().split("/")[-1]
if directory == "Homeworks":
    file_path = os.path.abspath("data/products.json")
    file_path_to_faulty_json = os.path.abspath("data/faulty_products.json")
    file_path_to_faulty_json_2 = os.path.abspath("data/faulty_products_2.json")
    # print("Homeworks")
elif directory in ("src", "tests"):
    file_path = os.path.abspath("../data/products.json")
    file_path_to_faulty_json = os.path.abspath("../data/faulty_products.json")
    file_path_to_faulty_json_2 = os.path.abspath("../data/faulty_products_2.json")
    # print("src", "tests")


def test_read_json___for_list_returned():
    data = read_json(file_path)
    assert type(data) is list
    assert type(data[0]) is dict
    assert "name" in data[0]


def test_read_json___with_faulty_path():
    file_path = "/home/lav/PycharmProjects/Homeworks/no_dir/products.json"
    data = read_json(file_path)
    assert type(data) is list and len(data) == 0


def test_validate_json_data___for_same_value_returned():
    data = read_json(file_path)
    assert validate_json_data(data) == data


def test_validate_json_data___with_faulty_products_json():
    with raises(ValueError) as exception_info:
        # В json файле в словаре-категории вместо ключа "name" - "nnnnnnnnnnnn...".
        data = read_json(file_path_to_faulty_json)
        validate_json_data(data)
    assert str(exception_info.value) == "При проверке json-данных, в словаре-категории - несоответствие ключей."


def test_validate_json_data___with_faulty_products_2_json():
    with raises(TypeError) as exception_info:
        # В json файле в словаре-продукте вместо значения 5 - [5, 5].
        data = read_json(file_path_to_faulty_json_2)
        validate_json_data(data)
    assert str(exception_info.value) == "При проверке json-данных, в словаре-продукте - несоответствие типов значений."


def test_get_objects_based_on():
    data = read_json(file_path)
    objects_list = get_objects_based_on(data)
    assert type(objects_list) is list
    assert type(objects_list[0]) is Category
    assert type(objects_list[0].products[0]) is Product