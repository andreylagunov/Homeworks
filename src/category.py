from src.product import Product


class Category:
    name: str
    description: str
    __products: list[Product]
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self) -> str:
        total_quantity = 0
        for prod in self.__products:
            total_quantity += prod.quantity
        # total_quantity = sum(prod.quantity for prod in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    @property
    def products(self) -> list:
        prod_list = []
        for prod in self.__products:
            prod_list.append(f"{prod.name}, {prod.price} руб, Остаток: {prod.quantity} шт.")
            # print(f"{prod.name}, {prod.price} руб, Остаток: {prod.quantity} шт.")
        return prod_list

    def add_product(self, new_product: Product) -> None:
        if isinstance(new_product, Product):
            # Проверяем наличие имени нового товара в имеющемся списке:
            for prod in self.__products:
                if prod.name == new_product.name:
                    prod.quantity += new_product.quantity

                    if prod.price < new_product.price:
                        prod.price = new_product.price
                    return
            # Если дубликата товара не было, просто добавляем новый товар и увеличиваем кол-во.
            self.__products.append(new_product)
            # self.product_count += 1
            self.__class__.product_count += 1
        else:
            raise TypeError("Попытка добавления в категорию объекта не типа Product.")

    def middle_price(self) -> float:
        try:
            average_price = sum(prod.price for prod in self.__products) / len(self.__products)
        except ZeroDivisionError:
            average_price = 0
        return round(average_price, 2)


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category_1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )
    assert category_1.product_count == 3

    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category_1.add_product(product4)
    assert category_1.product_count == 4

    product5 = Product('55" QLED 4K', "Фоновая подсветка", 140000.0, 93)
    category_1.add_product(product5)
    assert category_1.product_count == 4

    product6 = Product('65" QLED 8K', "Фоновая подсветка", 280000.0, 10)
    category_1.add_product(product6)
    assert category_1.product_count == 5
