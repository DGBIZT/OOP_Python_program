class Employee:
    # Здесь мы пишем название атрибута и указываем тип
    first: str
    last: str
    pay: int
    email: str
    pass

emp_1 = Employee()
emp_2 = Employee()

# print(emp_1)
# print(emp_2)

emp_1.first = "Ivan"
emp_1.last = "Ivanov"
emp_1.email = "Ivan.Ivanov@email.com"
emp_1.py = 50000

# Сделаем то же самое для второго сотрудника
# Добавляем имя 2-му сотруднику
emp_2.first = 'Petr'
# Добавляем фамилию 2-му сотруднику
emp_2.last = 'Petrov'
# Добавляем email 2-му сотруднику
emp_2.email = 'Petr.Petrov@email.com'
# Добавляем зарплату 2-му сотруднику
emp_2.pay = 60000

# print(emp_1.email)
# print(emp_2.email)

class Employee2:
    """Класс для представления сотрудника."""
    first: str  # Атрибуты (свойства) класса
    last: str
    pay: float

    # Одно из свойств класса - коэффициент повышения зарплаты
    raise_amount = 1.04  # Атрибут класса

    # Переменная на уровне класса для подсчета количества сотрудников
    number_of_employees = 0

    # Создаем конструктор класса, который принимает данные для создания объекта
    #  инициализатор, или конструктор, —  __init__
    def __init__(self, first, last, pay):
        # Атрибуты (свойства) класса
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}.@email.com"

        Employee2.number_of_employees += 1

    # Функция в классе называется методом
    def fullname(self):
        """Метод, который возвращает полное имя сотрудника."""
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = self.pay * self.raise_amount
        return self.pay

emp_1 = Employee2("Ivan", "Ivanov", 50000)
emp_2 = Employee2("Petr", "Petrov", 60000)

# Вызываем метод fullname экземпляра emp_1 и выводим результат в консоль
# print(emp_1.fullname())

# Вызываем метод fullname экземпляра emp_2 и выводим результат в консоль
# print(emp_2.fullname())
#
# print(Employee2.number_of_employees)
# print(emp_1.apply_raise())
# print(emp_2.apply_raise())

class JavaDeveloper:
    """Класс для представления Java-разработчиков."""

    def __init__(self, name):
        """Метод, который инициализирует экземпляры класса."""
        self.name = name

    def info(self):
        """Метод для печати информации о Java-разработчике."""
        print(f'I am {self.name} - Java developer.')

    def code(self):
        """Метод для программирования на языке Java."""
        print("class HelloWorld { public static void main(String[] args)...")


class PythonDeveloper:
    """Класс для представления Python-разработчиков."""

    def __init__(self, name):
        """Метод, который инициализирует экземпляры класса."""
        self.name = name

    def info(self):
        """Метод для печати информации о Python-разработчике."""
        print(f'I am {self.name} - Python developer.')

    def code(self):
        """Метод для программирования на языке Python."""
        print("print('Hello, World!')")


# Создаем экземпляры разных классов
dev1 = JavaDeveloper('Ivan')
dev2 = PythonDeveloper('Petr')

# Но работаем с ними единым образом
for developer in (dev1, dev2):
    developer.info()  # Вызов метода info()
    developer.code()  # Вызов метода code()
    print()