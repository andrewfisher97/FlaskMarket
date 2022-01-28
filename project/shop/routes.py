from shop import app
from flask import render_template
from shop.models import Item

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/shop')
def shop_page():
    items = Item.query.all()
    return render_template('shop.html', items=items)

@app.route('/about/<username>')
def about_page(username):
    return f'<h1>This is the about page for {username}</h1>'
