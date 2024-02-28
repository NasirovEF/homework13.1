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
            return "Введена не корректная цена"
        if price < self.__price:
            print("Заявленная цена ниже существующей, вы действительно хотите снизить цену")
            user_input = input("Введите 'y' для подтверждения")
            if user_input.lower() == "y":
                self.__price = price
            else:
                return "Цена сохранена прежняя"

        else:
            self.__price = price

    def __str__(self):
        return f'\n{self.name}, {self.get_price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        return self.__price * self.quantity + other.__price * other.quantity
