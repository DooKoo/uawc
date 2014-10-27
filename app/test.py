from app import models, db

test = db.DBwork()
test.add(models.Product("iPhone 4", "Some details of iPhone 4", 3500, "/static/images/products/img_423675.png"))
#prod = models.Product()
#prod.from_json(test.get_product(1))
#print(prod.to_json())