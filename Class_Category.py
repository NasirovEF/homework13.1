class Category:
    """Класс категории товаров"""

    total_category = 0
    unique_product = 0

    def __init__(self, name, description, products):  # Задание 2
        self.name = name
        self.description = description
        self._products = products

        Category.total_category += 1
        Category.unique_product += len(list(set(self.get_uniq_prod())))

    def get_uniq_prod(self):
        name_prod = []
        for product in self._products:
            name_prod.append(product.get("name"))

        return name_prod

    @property
    def get_product(self):
        return self._products

    @get_product.setter
    def get_product(self, product):
        return self._products.append(product)

    @property
    def get_list(self):
        product_list = ""
        for product in self._products:
            product_list += f'\n{product.get("name")}, {product.get("price")} руб. Остаток: {product.get("quantity")} шт.'

        return product_list
