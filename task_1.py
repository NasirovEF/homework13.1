class Category:
    """Класс категории товаров"""

    total_category = 0
    unique_product = 0

    def __init__(self, name, description, products):  # Задание 2
        self.name = name
        self.description = description
        self._products = products

        Category.total_category += 1
        Category.unique_product += len(set(self._products))

    def get_product(self, product):
        return self._products.append(product)

    @property
    def get_list(self):
        for product in self._products:
            return f'{product.get("name")}, {product.get("price")} руб. Остаток: {product.get("quantity")} шт.'


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



