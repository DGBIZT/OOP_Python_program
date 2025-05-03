def test_category(task):
    assert task.name == "Смартфоны"
    assert (
        task.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert task.products == ["product1", "product2", "product3"]
    assert task.product_count == 3
    assert task.category_count == 1
