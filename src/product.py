class Product:
    name: str
    description: str
    price: float | int
    quantity: int

    def __init__(self, name: str, description: str, price: float | int, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
