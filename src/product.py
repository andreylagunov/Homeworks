from src.base_product import BaseProduct
from src.repr_mixin import ReprMixin


class Product(ReprMixin, BaseProduct):
    name: str
    description: str
    __price: float | int
    quantity: int

    def __init__(self, name: str, description: str, price: float | int, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__(name, description, price, quantity)

    def __repr__(self):
        print(f"{self.__class__.__name__}('{self.name}', '{self.description}', {self.__price}, {self.quantity})")

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        return self.__price * self.quantity + other.__price * other.quantity

    @classmethod
    def new_product(cls, prod: dict):
        return cls(prod["name"], prod["description"], prod["price"], prod["quantity"])

    @property
    def price(self) -> int | float:
        return self.__price

    @price.setter
    def price(self, new_price: int | float) -> None:
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if new_price < self.__price:
            answer = input(f"Вы собираетесь понизить цену товара {self.name}. \nПодтвердите, нажатием Y (Yes): ")
            if answer.lower() in ("y", "yes"):
                self.__price = new_price
                print(f"Вы изменили цену. Теперь она составляет: {self.__price} руб.")
            else:
                print(f"Цена товара осталась неизменна: {self.__price} руб.")


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
