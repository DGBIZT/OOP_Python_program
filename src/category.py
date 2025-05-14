

from src.products import Product, Smartphone, LawnGrass


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
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product: Product) :
        """Добавление продукта в категорию """
        if not isinstance(product, Product):
            raise TypeError(f"Необходимо добавить объект типа Product или его наследника")
        if product in self.__products:
            raise ValueError("Продукт уже существует в категории")
        self.__products.append(product)
        Category.product_count += 1  # Увеличиваем только product_count


    @property
    def products(self):
        prod_str = ""
        for product in self.__products:
            prod_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт. \n"
        return prod_str

    def __str__(self):
        return f"{self.name}, количество продуктов: {sum(prod.quantity for prod in self.__products)}"
