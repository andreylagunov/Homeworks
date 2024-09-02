class Product:
    name: str
    description: str
    __price: float | int
    quantity: int

    def __init__(self, name: str, description: str, price: float | int, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

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
