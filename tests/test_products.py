
def test_init_products(product_task):
    assert product_task.name == "Samsung Galaxy S23 Ultra"
    assert product_task.description == "256GB, Серый цвет, 200MP камера"
    assert product_task.price == 180000.0
    assert product_task.quantity == 5