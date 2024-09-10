class ReprMixin:
    """Дополнительный класс для печати в консоль информации __repr__ созданного объекта"""

    def __init__(self, name: str, description: str, price: float | int, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        self.__repr__()

    def __repr__(self):
        print(f"{self.__class__.__name__}('{self.name}', '{self.description}', {self.__price}, {self.quantity})")
