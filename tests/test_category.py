from src.category import Category
from src.products import Product
import pytest

# def test_category(task):
#     assert task.name == "Смартфоны"
#     assert (
#         task.description
#         == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
#     )
#     assert task.products == ["product1", "product2", "product3"]
#     assert task.product_count == 3
#     assert task.category_count == 1

def test_category_counters():
    # запоминаем сколько есть на начало теста
    current_products_counter = Category.product_count
    current_category_counter = Category.category_count

    # сейчас меняем счётчики создав пару продуктов и категорию
    products = [
        Product('a', 'b', 1, 2), # просто номинальные продукты
        Product('c', 'd', 3, 4),
    ]
    category = Category('a', 'b', products) # это действие поменяло счётчики

    # проверяем что изменилось ровно на столько, на сколько мы планировали
    assert Category.product_count == current_products_counter + 2
    assert Category.category_count  == current_category_counter + 1


def test_products_property(category_with_products):
 # Проверяем, что свойство products возвращает корректную строку
 expected_output = (
 "Товар 1, 100.0 руб. Остаток: 5 шт. \n"
 "Товар 2, 200.0 руб. Остаток: 3 шт. \n"
 )
 # Получаем результат
 actual_output = category_with_products.products

 # Проверяем, что результат соответствует ожидаемому
 assert actual_output == expected_output


