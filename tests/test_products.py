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

def test_set_valid_price(product):
    """Тест установки корректной положительной цены"""
    product.price = 100
    assert product.price == 100

def test_set_zero_price(product, capsys):
    product.price = 0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная"