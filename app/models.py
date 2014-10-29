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
        self.bought_with = {}
        self.viewed_with = {}
        self.basket_with = {}

    def to_json(self):
        return {
            "name": self.name,
            "description": self.description,
            "price": str(self.price),
            "photo": self.path_photo,
            "buys": self.num_buys,
            "views": self.num_views,
            "bought_with": self.bought_with,
            "viewed_with": self.viewed_with,
            "basket_with": self.basket_with,
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
        result.bought_with = inp_json['bought_with']
        result.viewed_with = inp_json['viewed_with']
        result.basket_with = inp_json['basket_with']
        return result

    #type_dict define which dictionary we use.
    def add_with(self, type_dict, product_id):
        if type_dict is 1:
            tmp = self.bought_with
        elif type_dict is 2:
            tmp = self.viewed_with
        elif type_dict is 3:
            tmp = self.basket_with
        else:
            return 0

        for key in tmp.keys():
            if key is product_id:
                tmp[key] += 1
                break
        tmp[str(product_id)] = 1
        return 1

    def get_products_with(self, type_with):
        if type_with is 1:
            tmp = self.bought_with
        elif type_with is 2:
            tmp = self.viewed_with
        elif type_with is 3:
            tmp = self.basket_with
        else:
            return 0

        sorted_tmp = list(OrderedDict(sorted(tmp.items(), key=itemgetter(1))).keys())[:10]
        result = []
        for i in range(0, 4):
            choice = random.choice(sorted_tmp)
            result.append(choice)
            sorted_tmp.remove(choice)
        return result


class Basket:
    def __init__(self):
        self.num_of_items = 0
        self.items = []

    def add(self, new_item):
        self.items.append(new_item)
        for item in self.items:
            item.basket_with.append(new_item)
            new_item.basket_with.append(item)
        self.num_of_items += 1

    #will write
    def buy(self):
        pass

    #will write
    def remove(self):
        pass