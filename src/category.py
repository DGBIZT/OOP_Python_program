from src.products import Product


class Category:
    """Категория продуктов"""

    name: str
    description: str
    products: list[Product]

    # Переменная на уровне класса для подсчета количества товаров
    product_count = 0

    # Переменная на уровне класса для подсчета количества категорий
    category_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products

        Category.category_count += 1
        Category.product_count = len(self.products)
