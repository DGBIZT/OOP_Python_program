class Product:
    """Продукты"""

    name: str
    description: str
    price: float
    quantity: int  # Количество

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    # def __str__(self):
    #     return f"{self.name} ({self.quantity} шт.) - {self.price} руб."
