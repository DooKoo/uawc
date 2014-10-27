from pymongo import MongoClient
from app import models


class DBwork:
    def __init__(self):
        host = MongoClient('127.0.0.1:27017')
        host.shop.authenticate('dy23r876238vbce3', 'd92387gc7dy2398uc32')
        self.db = host.shop
        self.count = self.db.products.count()

    def add(self, new_product):
        product_id = {
            "id": self.count
        }
        self.db.products.insert(dict(list(product_id.items()) + list(new_product.to_json().items())))

    def remove(self, product):
        self.db.products.remove(product.to_json())

    def get_product(self, product_id):
        return self.db.products.find({"id": product_id})[0]
