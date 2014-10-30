from app import models, db

test = db.DBwork()

cart = models.Cart()
#test.remove(0)

test.get_catalog_products(1)
