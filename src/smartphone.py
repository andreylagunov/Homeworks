from src.product import Product


class Smartphone(Product):
    """Смартфон"""

    efficiency: int | float
    model: str
    memory: int
    color: str

    def __init__(
        self,
        name: str,
        description: str,
        price: float | int,
        quantity: int,
        efficiency: int | float,
        model: str,
        memory: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        if type(self) is type(other):
            return super().__add__(other)
        else:
            raise TypeError("Попытка сложения объектов различных типов.")


if __name__ == "__main__":
    phone = Smartphone("nokia", "Не актуальная марка", 12000, 2, 400, "3310", 128, "Red")

    assert phone.name == "nokia"
    assert phone.description == "Не актуальная марка"
    assert phone.price == 12000
    assert phone.quantity == 2
    assert phone.efficiency == 400
    assert phone.model == "3310"
    assert phone.memory == "4 GB"
    assert phone.color == "Red"
