from app import models, db

test = db.DBwork()

cart = models.Cart()

test.get_catalog_products(1)
