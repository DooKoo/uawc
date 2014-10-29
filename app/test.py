from app import models, db
from operator import itemgetter
from collections import OrderedDict
import random

test = db.DBwork()

cart = models.Cart()
prod = models.Product.from_json(test.get_product(0))
print(prod)
cart.add(prod)
print(cart.items)
cart.buy()



