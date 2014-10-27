import json


class Product:
    def __init__(self, n_name="Empty", n_description="Empty", n_price=0, n_path_photo="Empty"):
        self.id = 0
        self.name = n_name
        self.description = n_description
        self.path_photo = n_path_photo
        self.price = n_price

    def to_json(self):
        return {
            "name": self.name,
            "description": self.description,
            "price": str(self.price),
            "photo": self.path_photo
        }

    def from_json(self, inp_json):
        self.id = inp_json['id']
        self.name = inp_json['name']
        self.description = inp_json['description']
        self.path_photo = inp_json['photo']
        self.price = inp_json['price']


class Basket:
    def __init__(self):
        self.num_of_items = 0
        self.items = []

    def add(self, new_item):
        self.items.append(new_item)
        self.num_of_items += 1