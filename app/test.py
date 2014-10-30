from app import models, db
test = db.DBwork()
for j in range(0, 100):
    try:
        test.db.products.find({'id': j})[1]
        print('ahtung')
    except Exception:
        print("ok")