import os
from app import app
from flask import request, render_template, session, flash, redirect, escape
from app import models
from app import db

database = db.DBwork()

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
    product_db = database.get_product(product_id)

    return render_template('product.html',
                           name=product_db['name'],
                           address=product_db['photo'],
                           description=product_db['description'],
                           price=product_db['price'])


@app.route('/basket')
def basket():
    return render_template('basket.html')


@app.route('/checkout')
def checkout():
    return render_template('check.out.html')


@app.route('/add', methods=['POST'])
def add():

    if request.method == 'POST':
        image = request.files["add_to_shop_image"]
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], image.filename))

        database.add(models.Product(request.form["add_to_shop_name"], request.form["add_to_shop_about"],
                     request.form["add_to_shop_price"], app.config['UPLOAD_FOLDER'][5:]+image.filename))
    return redirect('/product/0')


@app.route('/test')
def test():
    return render_template('outlay.html')


@app.route('/')
@app.route('/admin')
def admin():
    if 'username' in session:
        return render_template('admin.html', invisible_overwrite='')
    else:
        return render_template('login.html', invisible_overwrite='')

