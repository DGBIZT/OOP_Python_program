import pytest

from src.products import Product
from src.category import Category

@pytest.fixture
def product():
   return Product(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5
    )

@pytest.fixture
def category():
   return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        products=["product1", "product2", "product3"]
    )
@pytest.fixture
def task():
    return Category("Смартфоны", "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни", ["product1", "product2", "product3"] )

@pytest.fixture
def category_fixture():
    # Очищаем счетчики перед каждым тестом
    Category.category_count = 0
    Category.product_count = 0
    return Category