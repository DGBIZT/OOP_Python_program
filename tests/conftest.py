import pytest

from src.category import Category
from src.products import Product


@pytest.fixture
def product():
    return Product(
        name="Samsung Galaxy S23 Ultra", description="256GB, Серый цвет, 200MP камера", price=180000.0, quantity=5
    )


@pytest.fixture
def category():
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