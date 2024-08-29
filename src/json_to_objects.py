import json
import os

from src.category import Category
from src.product import Product


def read_json(file_path: str) -> list:
    """
    :param file_path:   Путь до файла с данными json.
    :return:            Список (или пустой список, если данные в json некорректны).
    """
    if os.path.exists(file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                json_categories_list = json.load(file)

            if type(json_categories_list) is list:
                return json_categories_list

        except Exception:
            pass
    return []


def validate_json_data(json_categories_list: list) -> list:
    """
    :param json_categories_list:    Список данных, считанных с json.
    :return:                        Возвращается этот же список, если типы в списке - ожидаемые.
    """
    for category in json_categories_list:
        if type(category) is not dict:
            raise TypeError("При проверке json-данных (категории), ожидался словарь.")

        for key, value in category.items():
            if key not in ("name", "description", "products"):
                raise ValueError("При проверке json-данных, в словаре-категории - несоответствие ключей.")

            if type(value) not in (str, list):
                raise TypeError("При проверке json-данных, в словаре-категории - несоответствие типов значений.")

        for prod in category["products"]:
            if type(prod) is not dict:
                raise TypeError("При проверке json-данных (продукта), ожидался словарь.")

            for key, value in prod.items():
                if key not in ("name", "description", "price", "quantity"):
                    raise ValueError("При проверке json-данных, в словаре-продукте - несоответствие ключей.")

                if type(value) not in (str, float, int):
                    raise TypeError("При проверке json-данных, в словаре-продукте - несоответствие типов значений.")

    return json_categories_list


def get_objects_based_on(json_categories_list: list) -> list:
    """
    :param json_categories_list:    Список словарей-категорий, внутри которых - словари-продукты.
    :return:                        Список с объектами Category и Product, на основе принятого списка.
    """
    list_ = []

    for category_dict in json_categories_list:

        products_list = []
        for prod in category_dict["products"]:
            products_list.append(Product(prod["name"], prod["description"], prod["price"], prod["quantity"]))

        list_.append(Category(category_dict["name"], category_dict["description"], products_list))

    return list_


if __name__ == "__main__":

    directory = os.getcwd().split("/")[-1]
    if directory == "Homeworks":
        file_path = os.path.abspath("data/products.json")
        print("Homeworks")
    elif directory in ("src", "tests"):
        file_path = os.path.abspath("../data/products.json")
        print("src", "tests")
    else:
        file_path = "/home/lav/PycharmProjects/Homeworks/no_dir/products.json"

    print(file_path)
    data = read_json(file_path)
    print(type(data), len(data))
    assert type(read_json(file_path)) == list
