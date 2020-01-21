from app import app
from flask import render_template

@app.route('/')

@app.route('/index')
def index():
    return render_template('index.html', title="Home")

@app.route('/cookies')
def cookies():
    return render_template('cookies.html', title="Cookies and Cupcakes")

@app.route('/dessert')
def dessert():
    return render_template('dessert.html', title="Desserts")


