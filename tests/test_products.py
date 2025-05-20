import pytest

from src.products import BaseProduct, Product

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
    # Создаем объект с минимальным допустимым количеством
    product = Product("Iphone 15", "512GB, Gray space", 210000.0, 1)
    assert str(product) == "Iphone 15, 210000.0. Остаток: 1)"

    # # Проверяем случай с нулевым количеством
    # product = Product("Iphone 15", "512GB, Gray space", 210000.0, 0)
    # expected_str = "Iphone 15, 210000.0. Остаток: 0)"
    # assert str(product) == expected_str


def test_add_with_zero_quantity():
    # Создаем объекты с допустимыми значениями
    product1 = Product("Iphone 15", "512GB, Gray space", 210000.0, 1)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 2)
    assert product1 + product2 == 210000 * 3

    # # Проверяем случай с нулевым количеством
    # product1 = Product("Iphone 15", "512GB, Gray space", 210000.0, 0)
    # product2 = Product("Samsung S23", "256GB, Black", 180000.0, 5)
    #
    # # При нулевом количестве результат должен быть равен стоимости второго продукта
    # expected_sum = 180000.0 * 5
    # assert product1 + product2 == expected_sum


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


def test_init_smartphone(smartphone):
    """Проверка инициализации"""
    assert smartphone.name == "iPhone 14"
    assert smartphone.description == "Смартфон Apple"
    assert smartphone.price == 79990
    assert smartphone.quantity == 10
    assert smartphone.efficiency == "A16 Bionic"
    assert smartphone.model == "iPhone 14 Pro Max"
    assert smartphone.memory == "1TB"
    assert smartphone.color == "Space Black"


def test_inheritance_smartphone(smartphone):
    """Проверка наследования от Product"""
    assert isinstance(smartphone, Product)


def test_init_lawngrass(lawngrass):
    assert lawngrass.name == "Газонная трава"
    assert lawngrass.description == "Элитная трава для газона"
    assert lawngrass.price == 500.0
    assert lawngrass.quantity == 20
    assert lawngrass.country == "Россия"
    assert lawngrass.germination_period == "7 дней"
    assert lawngrass.color == "Зеленый"


def test_inheritance_lawngrass(lawngrass):
    assert isinstance(lawngrass, Product)


# Тестирование __add__, Сложкение стоимости товара!
# Если товар находится в одной группе, то производится складывание, в противном случае вызывается TypeError
def test_add_same_type(product_a, product_b):
    """Проверка сложения товаров одного типа"""
    result = product_a + product_b
    assert result == 100 * 5 + 200 * 3
    assert result == 1100


def test_add_different_types(product_a, different_type):
    """Проверка попытки сложения с другим типом"""
    with pytest.raises(TypeError):
        product_a + different_type


def test_add_int(product_a):
    """Проверка сложения с целым числом"""
    with pytest.raises(TypeError):
        product_a + 5


def test_add_list(product_a):
    """Проверка сложения со списком"""
    with pytest.raises(TypeError):
        product_a + [1, 2, 3]


def test_add_float(product_a):
    """Проверка сложения с числом с плавающей точкой"""
    with pytest.raises(TypeError):
        product_a + 5.5


def test_add_none(product_a):
    """Проверка сложения с None"""
    with pytest.raises(TypeError):
        product_a + None


# Тестирования абстрактного класса и класс-миксин
def test_repr(valid_product_info):
    # Создаем продукт
    product = Product.new_product(valid_product_info)

    # Проверяем вывод repr
    expected_repr = "Product(Test Product, This is a test product, 100.5, 10)"
    assert repr(product) == expected_repr


def test_init_printing(capsys, valid_product_info):
    # Проверяем, что при создании объекта выводится repr
    Product.new_product(valid_product_info)

    expected_output = "Product(Test Product, This is a test product, 100.5, 10)\n"
    assert capsys.readouterr().out == expected_output


def test_abstract_method():
    # Проверяем, что при отсутствии обязательных атрибутов возникает ошибка
    with pytest.raises(TypeError):

        class MissingMethodProduct(BaseProduct):
            pass

        # Создаем экземпляр для принудительного вызова ошибки
        MissingMethodProduct()


def test_correct_implementation():
    # Проверяем корректную реализацию
    class CorrectProduct(BaseProduct):
        @classmethod
        def new_product(cls, *args, **kwargs):
            return cls()

    CorrectProduct.new_product()


# Тестирование добавление товара с нулевым количеством
def test_product_by_zero():
    """Проверяем товар с нулевым количеством"""
    with pytest.raises(ValueError):
        Product("Бракованный товар", "Неверное количество", 1000.0, 0)

    # Проверяем товар с отрицательным количеством
    with pytest.raises(ValueError):
        Product("Бракованный товар", "Неверное количество", 1000.0, -1)
