import os
from app import app
from flask import request, render_template, session, flash, redirect, escape
from app import models
from app import db
from werkzeug.exceptions import HTTPException, NotFound
from werkzeug.wsgi import responder
from werkzeug.wrappers import BaseRequest

DATABASE = db.DBwork()
USERS_ON_SITE = 0
CARTS = {}

# APP_ROOT = os.path.join(os.path.abspath(__file__))
UPLOADER_FOLDER = './app/static/images/products/'
app.config['UPLOAD_FOLDER'] = UPLOADER_FOLDER
app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg', 'gif'])


def validate(user, passw):
    if user == 'admin' and passw == '000':
        return True
    else:
        return False


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


def view(request):
    raise NotFound()


def sign_in():
    global USERS_ON_SITE
    global CARTS
    if 'id' not in session:
        session['id'] = USERS_ON_SITE

        USERS_ON_SITE += 1
        CARTS = {session['id']: models.Cart()}
        return redirect('/catalog')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html')


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


@app.route('/product=<int:product_id>', methods=['GET'])
def product(product_id):
    sign_in()

    global CARTS
    cart = CARTS[session['id']]

    product_db = DATABASE.get_product(product_id)
    product_db['views'] += 1
    DATABASE.update_product(product_id, models.Product.from_json(product_db))
    return render_template('product.html',
                           name=product_db['name'],
                           address=product_db['photo'],
                           description=product_db['description'],
                           price=product_db['price'],
                           number_of_items=cart.num_of_items,
                           id=product_db['id'])


@app.route('/logout')
def logout():
    global USERS_ON_SITE
    global CARTS

    USERS_ON_SITE -= 1

    del CARTS[session['id']]
    session.clear()

    return redirect('/catalog')


@app.route('/cart')
def basket():

    sign_in()
    cart = CARTS
    return render_template('cart.html')


@app.route('/checkout')
def checkout():
    return render_template('check.out.html')


@app.route('/add', methods=['POST'])
def add():

    if request.method == 'POST':
        image = request.files["add_to_shop_image"]
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], image.filename))

        DATABASE.add(models.Product(request.form["add_to_shop_name"], request.form["add_to_shop_about"],
                     request.form["add_to_shop_price"], app.config['UPLOAD_FOLDER'][5:]+image.filename))

    return redirect('/product=5')


@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    global CARTS
    if request.method == 'POST':
        product_id = request.form['id']
        CARTS.get(session['id']).add(models.Product.from_json(DATABASE.get_product(product_id)))


@app.route('/catalog')
def catalog():
    sign_in()
    return render_template('catalog.html')


@app.route('/test')
def test():
    session.clear()
    return "ok"


@app.route('/')
@app.route('/admin')
def admin():
    if 'username' in session:
        return render_template('admin.html', invisible_overwrite='')
    else:
        return render_template('login.html', invisible_overwrite='')

