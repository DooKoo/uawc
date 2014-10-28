import os
from app import app
from flask import request, render_template, sessions, flash
from app import models
from app import db


database = db.DBwork()

# APP_ROOT = os.path.join(os.path.abspath(__file__))
UPLOADER_FOLDER = '/static/images/products'
app.config['UPLOAD_FOLDER'] = UPLOADER_FOLDER
app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html')


@app.route('/')
def index():
    return render_template('admin.html')

'''@app.route('/product')
def product():
    return render_template('product.html')

@app.route('/basket')
def basket():
    return render_template('basket.html')

@app.route('/checkout')
def checkout():
    return render_template('check.out.html')'''

@app.route('/add', methods=['POST'])
def add():
    # photos = UploadSet('photos'. IMAGES)
    if request.method == 'POST':
        image = request.files["add_to_shop_image"]
        print(image)
        print(image.filename)
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], image.filename))
        print(image)
        '''
        if image and allowed_file(image):
            filename = image
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        database.add(models.Product(request.form["add_to_shop_name"], request.form["add_to_shop_about"],
                         request.form["add_to_shop_price"], UPLOAD_FOLDER+filename))'''
    return 'ok'

@app.route('/admin')
def admin():
    return render_template('admin.html')
