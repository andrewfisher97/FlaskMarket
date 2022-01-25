from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/shop')
def shop_page():
    items = [
        {'id': 1, 'name': 'Charizard', 'barcode': '893212299897', 'price': 1000},
        {'id': 2, 'name': 'Blastoise', 'barcode': '123985473165', 'price': 500},
        {'id': 3, 'name': 'Venusaur', 'barcode': '231985128446', 'price': 250}
    ]
    return render_template('shop.html', items=items)

@app.route('/about/<username>')
def about_page(username):
    return f'<h1>This is the about page for {username}</h1>'
