class Product:
    """Класс товара"""

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def get_product(cls, prod_dict):
        return cls(**prod_dict)

    @property
    def get_price(self):
        return self.__price

    @get_price.setter
    def get_price(self, price):
        if price <= 0:
            print("Введена не корректная цена")
        if price < self.__price:
            print("Заявленная цена ниже существующей, вы действительно хотите снизить цену?")
            user_input = input("Введите 'y' для подтверждения")
            if user_input.lower() == "y":
                self.__price = price
            else:
                print("Цена сохранена прежняя")

        else:
            self.__price = price

    def __str__(self):
        return f'\n{self.name}, {self.get_price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        if type(self.__class__) is type(other.__class__):
            return self.get_price * self.quantity + other.get_price * other.quantity
        else:
            raise PermissionError('Невозможно сложить разные типы продуктов')


class Smartphone(Product):
    """класс Смартфоны"""

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """класс Трава газонная"""

    def __init__(self, name, description, price, quantity, country, germination, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination = germination
        self.color = color

