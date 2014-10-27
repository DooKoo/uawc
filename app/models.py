__author__ = 'dookoo'
import json

class Product:
    def __init__(self, n_name="", n_description="", n_price=0, n_path_photo=""):
        self.name = n_name
        self.description = n_description
        self.path_photo = n_path_photo
        self.price = n_price

    def to_json(self):
        return "{" \
                    "name: \""+self.name+"\"," \
                    "description: \""+self.description+"\"," \
                    "price: \""+str(self.price)+"\"," \
                    "photo: \""+self.path_photo+"\"," \
               "}"

    def from_json(self, inp_json):
        parsed = json.load(inp_json)
        self.name = parsed['name']
        self.description = parsed['description']
        self.path_photo = parsed['photo']
        self.price = parsed['price']
