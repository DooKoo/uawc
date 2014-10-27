__author__ = 'dookoo'
from app import models
prod = models.Product("iPhone", "the most value phone", 8000 ,"/static/images/iphone.png")
print(prod.to_json())
test = models.Product()
test.from_json(prod.to_json())
print(test.to_json())