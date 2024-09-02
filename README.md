# Домашнее задание 14.1


## Описание:

Учебный проект


## Необходимое ПО:

1. PyCharm IDE (или другая)
2. poetry
3. git
4. pytest
5. pytest-cov


## Для тестирования функций:

1. Клонируйте репозиторий:
```
git@github.com:andreylagunov/Homeworks.git
```

2. Установите зависимости:

```
poetry install 
```

3. Для запуска тестирования инструментом pytest:

```
pytest
pytest -v
pytest --verbose
```

4. Для формирования отчёта о покрытии тестами инструментом pytest-cov:

```
# Для проверки покрытия тестами:
pytest --cov

# Для формирования отчёта о покрытии:
pytest --cov=src --cov-report=html
```


## Описание работы функций:


### Модуль **main.py**
Проверяет работу созданных классов Category и Product:
```
# Примеры проверок:
product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

print(product1.name)
print(product1.description)
print(product1.price)
print(product1.quantity)
```


### Модуль **product.py**
Описывает класс Product
```
class Product:
    name: str
    description: str
    price: float | int
    quantity: int
    
def __init__(self, name: str, description: str, price: float | int, quantity: int):

@classmethod
def new_product(cls, prod: dict):

@property
def price(self):

@price.setter
def price(self, new_price: int | float):
```


### Модуль **category.py**
Описывает класс Category
```
class Category:
    name: str
    description: str
    products: list[Product]
    category_count = 0
    product_count = 0
    
def __init__(self, name: str, description: str, products: list[Product]):

@property
def products(self):

def add_product(self, new_product: Product):
```


### Модуль **json_to_objects.py**
Реализует функции проверки и конвертации json-данных в объекты Product и Category.
```
def read_json(file_path: str) -> list:
    """
    :param file_path:   Путь до файла с данными json.
    :return:            Список (или пустой список, если данные в json некорректны).
    """
    
def validate_json_data(json_categories_list: list) -> list:
    """
    :param json_categories_list:    Список данных, считанных с json.
    :return:                        Возвращается этот же список, если типы в списке - ожидаемые.
    """
    
def get_objects_based_on(json_categories_list: list) -> list:
    """
    :param json_categories_list:    Список словарей-категорий, внутри которых - словари-продукты.
    :return:                        Список с объектами Category и Product, на основе принятого списка.
    """
```

### Модуль **product_iterator.py**
Описывает класс ProductIterator. Класс служит для возможности перебора Продуктов в Категории.
```
class ProductIterator:

    def __init__(self, category_obj: Category):

    def __iter__(self):

    def __next__(self):
```


## Лицензия:

Проект распространяется под [лицензией MIT](LICENSE).