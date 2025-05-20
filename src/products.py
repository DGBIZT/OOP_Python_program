from abc import ABC, abstractmethod
from statistics import quantiles


class BaseProduct(ABC):

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        pass


class PrintMixin:
    def __init__(self):
        print(repr(self))

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"


class Product(BaseProduct, PrintMixin):
    """Продукты"""

    name: str
    description: str
    price: float
    quantity: int  # Количество

    def __init__(self, name, description, price, quantity):
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    # def __str__(self):
    #     return f"{self.name} ({self.quantity} шт.) - {self.price} руб."

    @classmethod
    def new_product(cls, product_info):
        return cls(
            name=product_info["name"],
            price=product_info["price"],
            description=product_info["description"],
            quantity=product_info["quantity"],
        )

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        # else:
        #     self.__price = price
        #     return self.__price

    def __str__(self):
        return f"{self.name}, {self.__price}. Остаток: {self.quantity})"

    def __add__(self, other):
        """Сложкение стоимости товара!
        Если товар находится в одной группе, то производится складывание, в противном случае вызывается TypeError"""
        if type(self) is not type(other):
            raise TypeError
        try:
            return self.__price * self.quantity + other.__price * other.quantity
        except TypeError:
            print("Возникла ошибка TypeError при попытке сложения")


class Smartphone(Product):
    """Категория товара смартфон"""

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency  # Производительность
        self.model = model  # модель
        self.memory = memory  # Объем встроенной памяти
        self.color = color  # Цвет


class LawnGrass(Product):
    """Категория товара Трава газонная"""

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country  # Cтрана-производитель
        self.germination_period = germination_period  # Cрок прорастания
        self.color = color  # цвет
