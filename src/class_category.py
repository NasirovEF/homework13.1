from class_product import *


class Category:
    """Класс категории товаров"""

    total_category = 0
    unique_product = 0

    def __init__(self, name, description, products):  # Задание 2
        self.name = name
        self.description = description
        self.__products = products

        Category.total_category += 1
        Category.unique_product += len(set(self.get_product))

    @property
    def get_product(self):
        return self.__products

    @get_product.setter
    def get_product(self, product):
        if isinstance(product, (Smartphone, LawnGrass, Product)):
            if product.quantity > 0:
                self.__products.append(product)
            else:
                raise ValueError('товар с нулевым количеством не может быть добавлен')
        else:
            raise ValueError('товар не является продуктом одной из категории')

    @property
    def get_list(self):
        product_list = ""
        for product in self.get_product:
            exp_prod = Product(**product)
            product_list += str(exp_prod)

        return product_list

    def average_price(self):
        try:
            sum_price = 0
            for product in self.get_product:
                sum_price += product.get("price")
            avg_price = round(sum_price / len(self.get_product))
            return avg_price

        except ZeroDivisionError:
            return 0

    def __str__(self):
        amount_prod = 0
        for product in self.__products:
            amount_prod += product.get("quantity")

        return f'{self.name}, количество продуктов: {amount_prod} шт.'
