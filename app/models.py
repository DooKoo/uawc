from operator import itemgetter
import random
from collections import OrderedDict


class Product:
    def __init__(self, n_name="Empty", n_description="Empty", n_price=0, n_path_photo="Empty"):
        self.id = 0
        self.name = n_name
        self.description = n_description
        self.path_photo = n_path_photo
        self.price = n_price
        self.num_buys = 0
        self.num_views = 0
        self.num_carts = 0
        self.bought_with = {}
        self.viewed_with = {}
        self.cart_with = {}

    def to_json(self):
        return {
            "name": self.name,
            "description": self.description,
            "price": str(self.price),
            "photo": self.path_photo,
            "buys": self.num_buys,
            "views": self.num_views,
            "carts": self.num_carts,
            "bought_with": self.bought_with,
            "viewed_with": self.viewed_with,
            "cart_with": self.cart_with,
        }

    def to_view(self):
        return {
            "name": self.name,
            "description": self.description,
            "price": str(self.price),
            "photo": self.path_photo
        }

    @staticmethod
    def from_json(inp_json):
        result = Product()
        result.id = inp_json['id']
        result.name = inp_json['name']
        result.description = inp_json['description']
        result.path_photo = inp_json['photo']
        result.price = inp_json['price']
        result.num_views = inp_json['views']
        result.num_buys = inp_json['buys']
        result.num_carts = inp_json['carts']
        result.bought_with = inp_json['bought_with']
        result.viewed_with = inp_json['viewed_with']
        result.cart_with = inp_json['cart_with']
        return result

    #type_dict define which dictionary we use.
    def add_cart_with(self, type_dict, product_id):
        if str(product_id) in self.cart_with.keys():
            self.cart_with[str(product_id)] += 1
        else:
            self.cart_with[str(product_id)] = 1

    def get_products_with(self, type_with):
        if type_with is 1:
            tmp = self.bought_with
        elif type_with is 2:
            tmp = self.viewed_with
        elif type_with is 3:
            tmp = self.cart_with
        else:
            return 0

        sorted_tmp = list(OrderedDict(sorted(tmp.items(), key=itemgetter(1))).keys())[:10]
        result = []
        for i in range(0, 4):
            choice = random.choice(sorted_tmp)
            result.append(choice)
            sorted_tmp.remove(choice)
        return result


class Cart:
    def __init__(self):
        self.num_of_items = 0
        self.items = []

    def add(self, new_item):
        self.items.append(new_item)
        for item in self.items:
            item.add_cart_with(3, new_item.id)
            new_item.add_cart_with(3,item.id)
        self.num_of_items += 1

    #need test
    def buy(self):
        for item in self.items:
            for item2 in self.items:
                if item != item2:
                    pass

    #will write
    def remove(self):
        pass