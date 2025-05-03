
def test_category(task):
    assert task.name == "Смартфоны"
    assert task.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    assert task.products == ["product1", "product2", "product3"]