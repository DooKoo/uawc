from app import models, db
from operator import itemgetter
from collections import OrderedDict
import random

test = db.DBwork()

cart = models.Cart()
#test.remove(0)

prod = models.Product.from_json(test.get_product(0))
prod.add_cart_with(1, 5)
prod.add_cart_with(1, 5)
prod.add_cart_with(1, 5)
prod.add_cart_with(1, 5)
print(prod.cart_with.items())
#cart.add(prod)
#test.update_product(0, prod)
