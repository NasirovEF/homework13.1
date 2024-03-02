from class_product import Product


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
        self.__products.append(product)

    @property
    def get_list(self):
        product_list = ""
        for product in self.get_product:
            exp_prod = Product(**product)
            product_list += str(exp_prod)

        return product_list

    def __str__(self):
        amount_prod = 0
        for product in self.__products:
            amount_prod += product.get("quantity")

        return f'{self.name}, количество продуктов: {amount_prod} шт.'
