import json


class Product:
    def __init__(self, n_id = 0, n_name="", n_description="", n_price=0, n_path_photo=""):
        self.id = n_id
        self.name = n_name
        self.description = n_description
        self.path_photo = n_path_photo
        self.price = n_price

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": str(self.price),
            "photo": self.path_photo
        }

    def from_json(self, inp_json):
        parsed = json.loads(inp_json)
        self.id = parsed['id']
        self.name = parsed['name']
        self.description = parsed['description']
        self.path_photo = parsed['photo']
        self.price = parsed['price']


class Basket:
    def __init__(self):
        self.num_of_items = 0
        self.items = []

    def add(self, new_item):
        self.items.append(new_item)
        self.num_of_items += 1