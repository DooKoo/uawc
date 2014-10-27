from pymongo import MongoClient
from app import models


class DBwork:
    def __init__(self):
        host = MongoClient('127.0.0.1:27017')
        host.shop.authenticate('dy23r876238vbce3', 'd92387gc7dy2398uc32')
        self.db = host.shop

    def add(self, new_product):
        self.db.products.insert(new_product.to_json())

    def remove(self, product):
        self.db.products.remove(product.to_json())

    def get_products(self):
        pass
