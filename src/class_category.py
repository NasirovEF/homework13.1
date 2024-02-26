class Category:
    """Класс категории товаров"""

    total_category = 0
    unique_product = 0

    def __init__(self, name, description, products):  # Задание 2
        self.name = name
        self.description = description
        self.__products = products

        Category.total_category += 1
        #Category.unique_product += len(set(list(self.get_product)))

    @property
    def get_product(self):
        return self.__products

    @get_product.setter
    def get_product(self, product):
        return self.__products.append(product)

    @property
    def get_list(self):
        product_list = ""
        for product in self.__products:
            product_list += (f'\n{product.get("name")}, '
                             f'{product.get("price")} руб. '
                             f'Остаток: {product.get("quantity")} шт.')

        return product_list
