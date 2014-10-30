from pymongo import MongoClient


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
            "id": self.count
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

        print(all_products_info)

