from src.products import Product

# def test_init_products(product):
#     assert product.name == "Samsung Galaxy S23 Ultra"
#     assert product.description == "256GB, Серый цвет, 200MP камера"
#     assert product.price == 180000.0
#     assert product.quantity == 5


def test_new_product_valid_data(valid_product_info):
    """Тест создания продукта с валидными данными"""
    product = Product.new_product(valid_product_info)
    assert product.name == valid_product_info["name"]
    assert product.price == valid_product_info["price"]
    assert product.description == valid_product_info["description"]
    assert product.quantity == valid_product_info["quantity"]


def test_set_valid_price(product_2):
    """Тест установки корректной положительной цены"""
    product_2.price = 100
    assert product_2.price == 100


def test_set_zero_price(product, capsys):
    product.price = 0
    # captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная"


def test_str_method2():
    # Создаем продукт
    product = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

    # Проверяем строку представления
    expected_str = "Iphone 15, 210000.0. Остаток: 8)"
    assert str(product) == expected_str


def test_add_method():
    # Создаем два продукта
    product1 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product2 = Product("Samsung S23", "256GB, Black", 180000.0, 5)

    # Проверяем сложение
    expected_sum = 210000.0 * 8 + 180000.0 * 5
    assert product1 + product2 == expected_sum


def test_str_with_zero_quantity():
    # Проверяем случай с нулевым количеством
    product = Product("Iphone 15", "512GB, Gray space", 210000.0, 0)
    expected_str = "Iphone 15, 210000.0. Остаток: 0)"
    assert str(product) == expected_str


def test_add_with_zero_quantity():
    # Проверяем случай с нулевым количеством
    product1 = Product("Iphone 15", "512GB, Gray space", 210000.0, 0)
    product2 = Product("Samsung S23", "256GB, Black", 180000.0, 5)

    # При нулевом количестве результат должен быть равен стоимости второго продукта
    expected_sum = 180000.0 * 5
    assert product1 + product2 == expected_sum


def test_str_with_decimal_price():
    # Проверяем работу с дробной ценой
    product = Product("Iphone 15", "512GB, Gray space", 210000.55, 8)
    expected_str = "Iphone 15, 210000.55. Остаток: 8)"
    assert str(product) == expected_str


def test_add_with_decimal_prices():
    # Проверяем работу с дробными ценами
    product1 = Product("Iphone 15", "512GB, Gray space", 210000.55, 8)
    product2 = Product("Samsung S23", "256GB, Black", 180000.75, 5)

    expected_sum = 210000.55 * 8 + 180000.75 * 5
    assert product1 + product2 == expected_sum
