from src.category import Category
from src.product import Product


class ProductIterator:

    def __init__(self, category_obj: Category):
        self.category_obj = category_obj

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.category_obj.products):
            prod_info = self.category_obj.products[self.index]
            self.index += 1
            return prod_info
        else:
            raise StopIteration


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category_1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    prod_iterator = ProductIterator(category_1)
    for prod in prod_iterator:
        print(prod)
