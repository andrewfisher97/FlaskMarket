from shop import app, db
from flask import render_template, redirect, url_for, flash, get_flashed_messages
from shop.models import Item, User
from shop.forms import RegisterForm

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/shop')
def shop_page():
    items = Item.query.all()
    return render_template('shop.html', items=items)

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data, email_address=form.email_address.data, password_hash=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('shop_page'))
    if form.errors != {}: # if there are no errors from validations
        for err_msg in form.errors.values():
            flash(f'There was an error with account creation: {err_msg}', category='danger')

    return render_template('register.html', form=form)
