class NegValueExcept(Exception):
    pass


class Product:

    def __init__(self, type, name, price):
        self.type = type
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.type}, {self.name}, {self.price}'

    def __repr__(self):
        return f'Product({self.type}, {self.name}, {self.price})'


class ProductStore:
    product_shop = []
    profit = 0

    def add(self, product, amount):
        try:
            if amount <= 0:
                raise NegValueExcept('The number must be above zero')
            product.price += ((product.price / 100) * 30)
            product_list = dict(type=product.type, name=product.name, price=product.price, amount=amount)
            self.product_shop.append(product_list)
        except NegValueExcept as n:
            print(format(n))
        except TypeError as t:
            print('Enter only numbers'.format(t))

    def set_discount(self, identifier, percent, identifier_type='name'):
        try:
            if percent <= 0:
                raise NegValueExcept('The percent must be above zero')
            for product in self.product_shop:
                if identifier == product['name'] and identifier_type == 'name':
                    product['price'] -= product['price'] / 100 * percent
            return self.product_shop
        except NegValueExcept as n:
            print(format(n))
        except TypeError as t:
            print('Enter only numbers'.format(t))

    def sell_product(self, product_name, amount):
        try:
            if amount <= 0:
                raise NegValueExcept('The number must be above zero')
            for product in self.product_shop:
                if product_name == product['name']:
                    product['amount'] -= amount
                    self.profit += product['price'] * amount
            return self.product_shop
        except NegValueExcept as n:
            print(format(n))
        except TypeError as t:
            print('Enter only numbers'.format(t))

    def get_income(self):
        return self.profit

    def get_all_products(self):
        return self.product_shop

    def get_product_info(self, product_name):
        for product in self.product_shop:
            if product['name'] == product_name:
                return product['name'], product['amount']

    def __str__(self):
        return self.product_shop

    def __repr__(self):
        return self.product_shop


p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)

s = ProductStore()

s.add(p, 10)
s.add(p2, 300)

# print(repr(s.product_shop))

s.set_discount('Football T-Shirt', 30)

# print(repr(s.product_shop))

s.sell_product('Ramen', 10)

# print(repr(s.product_shop))
# print(repr(s.get_income()))
# print(repr(s.get_all_products()))

assert s.get_product_info('Ramen') == ('Ramen', 290)
