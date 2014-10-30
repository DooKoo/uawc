from app import models, db

test = db.DBwork()
print(test.get_catalog_products(1))

