class Product:
    """Класс товара"""

    def __init__(self, name, description, price, quantity):  # Задание 2
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
                print("Цена сохранена прежняя")

        else:
            self.__price = price
