from config import db

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @staticmethod
    def from_dict(source):
        return Product(source['name'], source['price'])

    def to_dict(self):
        return {
            'name': self.name,
            'price': self.price
        }

    def __repr__(self):
        return f'Product(name={self.name}, price={self.price})'

class Purchase:
    def __init__(self, product_id, quantity):
        self.product_id = product_id
        self.quantity = quantity

    @staticmethod
    def from_dict(source):
        return Purchase(source['product_id'], source['quantity'])

    def to_dict(self):
        return {
            'product_id': self.product_id,
            'quantity': self.quantity
        }

    def __repr__(self):
        return f'Purchase(product_id={self.product_id}, quantity={self.quantity})'
