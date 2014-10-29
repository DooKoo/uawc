from app import models, db
from operator import itemgetter
from collections import OrderedDict
import random

test = db.DBwork()

cart = models.Cart()
#test.remove(0)

prod0 = models.Product.from_json(test.get_product(0))
prod1 = models.Product.from_json(test.get_product(1))
cart.add(prod0)
cart.add(prod1)
cart.buy()
test.update_product(0, prod0)
test.update_product(1, prod1)
