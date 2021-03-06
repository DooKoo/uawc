import os
from app import app
from flask import request, render_template, session, redirect
from app import models
from app import db


#------------------------
#   GLOBAL VARIABLES    |
#------------------------


DATABASE = db.DBwork()
USERS_ON_SITE = 0
CARTS = {}
VIEWS = {}
UPLOADER_FOLDER = './app/static/images/products/'

#--------------------
#      CONFIGS      |
#--------------------

app.config['UPLOAD_FOLDER'] = UPLOADER_FOLDER
app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg', 'gif'])

#--------------------
#       PAGES       |
#--------------------


@app.route('/')
@app.route('/catalog')
def main():
    return redirect('/catalog=1')


@app.route('/catalog=<int:page>')
def catalog(page):

    sign_in()
    global CARTS
    cart_session = CARTS.get(session['id'])
    id_products = DATABASE.get_catalog_products(page)

    products__ = []
    for i in id_products:
        products__.append(models.Product.from_json(DATABASE.get_product(i)))

    products_line_1 = products__[:3]
    products_line_2 = products__[3:6]
    products_line_3 = products__[6:]
    return render_template('catalog.html',
                           line_1=products_line_1,
                           line_2=products_line_2,
                           line_3=products_line_3,
                           id_current_page=page,
                           id_last_page=DATABASE.last_page(),
                           number_of_items=cart_session.num_of_items)


@app.route('/product=<int:_id>', methods=['GET'])
def product(_id):
    sign_in()

    global CARTS
    cart_session = CARTS.get(session['id'])

    try:
        product_db = DATABASE.get_product(_id)
    except IndexError:
        return render_template('page_not_found.html')

    product_db['views'] += 1

    global VIEWS
    obj_product = models.Product.from_json(product_db)
    for i in VIEWS.get(session['id']):
        i.add_viewed_with(_id)
        DATABASE.update_product(i.id, i)
        obj_product.add_viewed_with(i.id)

    VIEWS.get(session['id']).append(obj_product)

    list_bought = []
    list_viewed = []
    list_put = []

    product_db = dict(list({'id': _id}.items()) + list(obj_product.to_json().items()))

    for product_id in models.Product.from_json(product_db).get_products_with(1):
        list_bought.append(DATABASE.get_product(int(product_id)))
    for product_id in models.Product.from_json(product_db).get_products_with(2):
        list_viewed.append(DATABASE.get_product(int(product_id)))
    for product_id in models.Product.from_json(product_db).get_products_with(3):
        list_put.append(DATABASE.get_product(int(product_id)))

    DATABASE.update_product(_id, models.Product.from_json(product_db))
    return render_template('product.html',
                           name=product_db['name'],
                           address=product_db['photo'],
                           description=product_db['description'],
                           price=product_db['price'],
                           number_of_items=cart_session.num_of_items,
                           id=product_db['id'],
                           list_bought=list_bought,
                           list_viewed=list_viewed,
                           list_put=list_put)


@app.route('/cart')
def cart():
    global CARTS
    sign_in()
    cart_session = CARTS.get(session['id'])
    total_price = 0
    for item in cart_session.items:
        total_price += int(item.price)
    return render_template('cart.html',
                           cart=cart_session,
                           total_price=total_price,
                           number_of_items=cart_session.num_of_items,
                           user_id=session['id'])


@app.route('/checkout')
def checkout():
    global CARTS
    cart_session = CARTS.get(session['id'])
    return render_template('checkout.html',
                           number_of_items=cart_session.num_of_items)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html')


#----------------
#      API      |
#----------------


def sign_in():
    global USERS_ON_SITE
    global CARTS
    global VIEWS
    if 'id' not in session:
        session['id'] = USERS_ON_SITE

        USERS_ON_SITE += 1
        CARTS = {session['id']: models.Cart()}
        VIEWS = {session['id']: []}


@app.route('/remove_from_cart/id=<int:product_id>', methods=['GET'])
def remove_from_cart(product_id):
    global CARTS
    CARTS.get(session['id']).remove(int(product_id))
    return redirect('/cart')


@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    global CARTS
    if request.method == 'POST':
        product_id = request.form['id']
        CARTS.get(session['id']).add(models.Product.from_json(DATABASE.get_product(int(product_id))))
    return redirect(request.form['from'])


@app.route('/buy')
def buy():
    global CARTS

    CARTS.get(session['id']).buy()
    return redirect('/catalog')


@app.route('/in_cart', methods=['POST'])
def in_cart():
    global CARTS
    return str(CARTS[session['id']].num_of_items)

#---------------------------------
#   FUNCTION OF ADMINISTRATION   |
#---------------------------------


def check_for_price(price):
    try:
        price_of_item = float(price)
    except ValueError:
        print('not a float number') # <---- error wrong input


def validate(user, passw):
    if user == 'admin' and passw == '000':
        return True
    else:
        return False


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


@app.route('/admin')
def admin(alert=''):
    if 'username' in session:
        return render_template('admin.html', invisible_overwrite='',
                               alert=alert)
    else:
        pass
    return render_template('login.html', invisible_overwrite='')


@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        image = request.files["add_to_shop_image"]
        if image and allowed_file(image.filename):
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], image.filename))
        else:
            return admin("Product wasn't added due to wrong extension of image or no image file was found")
        if request.form["add_to_shop_name"] != "" and request.form["add_to_shop_about"] != "" and request.form["add_to_shop_price"] != "":
            if check_for_price(request.form['add_to_shop_price']):
                DATABASE.add(models.Product(request.form["add_to_shop_name"], request.form["add_to_shop_about"],
                             request.form["add_to_shop_price"], app.config['UPLOAD_FOLDER'][5:]+image.filename))
                return admin("ok")
            else:
                return admin("Product wasn't added due to wrong type of input, price should be a number")
        else:
            return admin("Product wasn't added, one of the fields to input is empty")
    else:
        return admin("Invalid method")


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if validate(username, password):
            session['username'] = username
            return redirect('/admin')
    else:
        return redirect('/test')


@app.route('/logout')
def logout():
    global USERS_ON_SITE
    global CARTS

    USERS_ON_SITE -= 1

    del CARTS[session['id']]
    session.clear()

    return redirect('/catalog')