from app import app
from flask import request, render_template, sessions, flash
from app import models


@app.route('/')
def index():
    return render_template('shop.html')

@app.route('/product')
def product():
    return render_template('product.html')

@app.error_handler(404)
def page_not_found():
    return render_template('page_not_found.html')

@app.route('/basket')
def basket():
    return render_template('basket.html')

@app.route('/checkout')
def checkout():
    return render_template('check.out.html')

@app.route('/add', methods=['POST'])
def add():
    product = request.form[""]

@app.route('/admin')
def admin():
    return render_template('admin.html')
