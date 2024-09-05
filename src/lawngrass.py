from src.product import Product


class LawnGrass(Product):
    """Трава газонная"""

    country: str
    germination_period: str
    color: str

    def __init__(
        self,
        name: str,
        description: str,
        price: float | int,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        if type(self) is type(other):
            return super().__add__(other)
        else:
            raise TypeError("Попытка сложения объектов различных типов.")
