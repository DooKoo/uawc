from app import models, db
from operator import itemgetter
from collections import OrderedDict
import random

test = db.DBwork()
prod = models.Product()
prod.from_json(test.get_product(5))
test.update_product(5, prod)


