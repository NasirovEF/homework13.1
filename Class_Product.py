class Product:
    """Класс товара"""

    def __init__(self, name, description, price, quantity):  # Задание 2
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @classmethod
    def get_product(cls, name, description, price, quantity):
        return cls(name, description, price, quantity)

    @property
    def get_price(self):
        return self.price

    @get_price.setter
    def get_price(self, price):
        if price <= 0:
            return "Введена не корректная цена"
        if price < self.price:
            print("Заявленная цена ниже существующей, вы действительно хотите снизить цену")
            user_input = input("Введите 'y' для подтверждения")
            if user_input.lower() == "y":
                self.price = price
            else:
                print("Цена сохранена прежняя")

        else:
            self.price = price
