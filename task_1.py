class Category:
    """Класс категории товаров"""

    name: str
    description: str
    products: list
    total_category = 0
    unique_product = 0

    def __init__(self, name, description, product):  # Задание 2
        self.name = name
        self.description = description
        self.product = product

        Category.total_category += 1
        Category.unique_product += len(set(self.product))


class Product:
    """Класс товара"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):  # Задание 2
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

