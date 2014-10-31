from app import models, db
test = db.DBwork()

prod = models.Product.from_json(test.get_product(14))
print(prod.get_products_with(2))
