from abc import ABC, abstractmethod


class Base(ABC):
    """Абстрактный класс"""

    @property
    @abstractmethod
    def get_price(self):
        pass

    @classmethod
    @abstractmethod
    def get_product(cls, prod_dict):
        pass


class MixinInform:
    def __init__(self, *args):
        print(repr(self))

    def __repr__(self):
        lst_values = []

        for values in self.__dict__:
            lst_values.append(str(values))
        values_str = ", ".join(lst_values)

        return f'{self.__class__.__name__}({values_str})'


class Product(Base, MixinInform):
    """Класс товара"""

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

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
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
        super().__init__(name, description, price, quantity)


class LawnGrass(Product):
    """класс Трава газонная"""

    def __init__(self, name, description, price, quantity, country, germination, color):
        self.country = country
        self.germination = germination
        self.color = color
        super().__init__(name, description, price, quantity)
