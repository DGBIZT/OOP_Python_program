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

def test_add_valid_product(category_2):
    new_product = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    category_2.add_product(new_product)
    assert Category.product_count == 4

def test_add_wrong_type():
    wrong_product = "Неверный тип"
    category_2 = Category("Смартфоны", "Описание", [])  # Передаем пустой список
    with pytest.raises(TypeError) as excinfo:
        category_2.add_product(wrong_product)
    assert str(excinfo.value) == "Необходимо добавить объект типа Product или его наследника"
    assert Category.product_count == 0


def test_add_existing_product():
    # Создаем продукт
    existing_product = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

    # Создаем категорию с одним продуктом
    category = Category("Смартфоны", "Описание", [existing_product])

    # Проверяем, что продукт уже есть в категории
    assert existing_product in category._Category__products  # Исправлено __products

    # Проверяем, что при попытке добавить существующий продукт возникает ValueError
    with pytest.raises(ValueError) as excinfo:
        category.add_product(existing_product)

    # Проверяем сообщение об ошибке
    assert str(excinfo.value) == "Продукт уже существует в категории"

    # Проверяем, что счетчик продуктов не увеличился
    assert Category.product_count == 1

    # Проверяем, что продукт все еще один в категории
    assert len(category._Category__products) == 1  # Исправлено __products


def test_str_method(category_2):
    # Проверяем строку без добавления новых продуктов
    assert str(category_2) == "Смартфоны, количество продуктов: 3"

    # Добавляем новый продукт и проверяем
    category_2.add_product(Product("iPhone 15", 89990, 15, 1))
    assert str(category_2) == "Смартфоны, количество продуктов: 4"

    # Добавляем еще один продукт и проверяем
    category_2.add_product(Product("OnePlus 11", 59990, 12, 2))
    assert str(category_2) == "Смартфоны, количество продуктов: 5"


def test_reset_counters():
    Category.product_count = 0
    Category.category_count = 0
    assert Category.product_count == 0
    assert Category.category_count == 0


def test_multiple_categories():
    Category.product_count = 0
    Category.category_count = 0

    category1 = Category("Смартфоны", "Описание", [])
    category2 = Category("Планшеты", "Описание", [])

    assert str(category1) == "Смартфоны, количество продуктов: 0"
    assert str(category2) == "Планшеты, количество продуктов: 0"


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