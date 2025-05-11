import pytest

from src.category import Category
from src.products import Product

@pytest.fixture(autouse=True)
def reset_counters():
    Category.product_count = 0
    Category.category_count = 0

@pytest.fixture
def product():
    return Product(
        name="Samsung Galaxy S23 Ultra", description="256GB, Серый цвет, 200MP камера", price=180000.0, quantity=5
    )


@pytest.fixture
def category():
    Category.product_count = 0
    Category.category_count = 0
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, "
        "но и получения дополнительных функций для удобства жизни",
        products=["product1", "product2", "product3"],
    )


@pytest.fixture
def task():
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, " "но и получения дополнительных функций для удобства жизни",
        ["product1", "product2", "product3"],
    )


@pytest.fixture
def valid_product_info():
    return {
        "name": "Test Product",
        "price": 100.5,
        "description": "This is a test product",
        "quantity": 10
    }

@pytest.fixture
def product():
    # Создаем экземпляр Product с валидными тестовыми данными
    return Product(
        name="Test Product",
        description="This is a test product",
        price=100.0,
        quantity=10
    )

# Category
@pytest.fixture
def category_with_products():
 # Добавляем необходимые параметры при создании категории
 category = Category(
 name="Тестовая категория",
 description="Описание тестовой категории",
 products=[]
 )
 category.add_product(Product("Товар 1", "Описание 1", 100.0, 5))
 category.add_product(Product("Товар 2", "Описание 2", 200.0, 3))
 return category

# @pytest.fixture
# def category_str():
#     return Category("Продукты")
@pytest.fixture
def category_2():
    Category.product_count = 0
    Category.category_count = 0

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )
@property
def products(self):
    return self.__products

# @pytest.fixture
# def category():
#  Category.product_count = 0
#  Category.category_count = 0
#  return Category("Смартфоны", "Описание", [])