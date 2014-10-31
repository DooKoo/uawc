from pymongo import MongoClient
import math


class DBwork:
    def __init__(self):
        self.host = MongoClient('127.0.0.1:27017')
        try:
            self.host.shop.authenticate('dy23r876238vbce3', 'd92387gc7dy2398uc32')
        except Exception:
            print("Error. Database not found :(")

        self.db = self.host.shop
        self.count = self.db.products.count()

    def close(self):
        self.host.close()

    def add(self, new_product):
        product_id = {
            "id": self.db.products.count()
        }
        self.db.products.insert(dict(list(product_id.items()) + list(new_product.to_json().items())))
        self.count += 1

    def remove(self, product_id):
        self.db.products.remove({"id": product_id})
        self.count -= 1

    def get_product(self, product_id):
        return self.db.products.find({"id": product_id})[0]

    def update_product(self, product_id, up_product):
        self.db.products.update({"id": product_id},
                                dict(list({"id": product_id}.items()) + list(up_product.to_json().items())))

    def get_catalog_products(self, page):
        tmp = self.db.products.find()
        all_products_info = []
        for i in tmp:
            all_products_info.append({'id': i['id'], 'buys': i['buys'], 'views': i['views'], 'carts': i['carts']})

        sorted_list = sorted(all_products_info, key=lambda k: (k['buys'], k['views'], k['carts']), reverse=True)
        result = []

        for i in range(page*9-9, page*9):
            try:
                result.append(sorted_list[i]['id'])
            except Exception:
                break

        return result

    def last_page(self):
        return math.ceil(self.db.products.count()/9)


