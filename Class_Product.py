class Product:
    """Класс товара"""

    def __init__(self, name, description, price, quantity):  # Задание 2
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @classmethod
    def get_product(cls, name, description, price, quantity):
        return [name, description, price, quantity]

    @property
    def get_price(self):
        if self.price <= 0:
            return "Введена некорректная цена"