from flask_login import (login_user, UserMixin,
                            login_required, logout_user,
                            current_user, current_app)
from flask_wtf import Form
from flask import Blueprint, render_template, request, redirect, url_for, flash
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from server.common import tryton, login_manager
import trytond.security
from trytond.transaction import Transaction
import trytond

auth_endpoint = Blueprint('auth_endpoint', __name__,
                            template_folder='templates')

user_model = tryton.pool.get('res.user')

@login_manager.user_loader
def load_user(user_id):
    return User(uid=user_id)

class LoginForm(Form):
    """The login form
    """
    username = StringField('Username', [DataRequired()])
    password = PasswordField('Password', [DataRequired()])
    submit=SubmitField('Login')

@tryton.transaction()
def get_user_id(uid=None, username=None, password=None):
    """Return user info from tryton
    """
    if uid is not None:
        user=user_model.search([('id', '=', uid)])
        if user:
            return unicode(user[0].id)
    if username is not None and password is not None:
        user_id = user_model.get_login(username, password)
        if user_id:
            return unicode(user_id)
    return None

class User(UserMixin):
    """The user class
    """

    def __init__(self, uid=None, username=None, password=None):
        self.id=None

        ident = get_user_id(uid, username, password)
        if ident is not None:
            self.id = ident

    def get_id(self):
        return self.id

@auth_endpoint.route("/login", methods=["GET", "POST"])
def login():
    """Login view"""
    if current_user.is_authenticated:
        return redirect(url_for('auth_endpoint.home'))
    form = LoginForm()
    if form.validate_on_submit():
        u = User(username=request.form['username'], password=request.form['password'])
        login_user(u, remember=True)
        flash('Logged in')
        n = request.args.get('next', url_for('auth_endpoint.home'))
        return redirect(n)
    return render_template("login.html", form=form)

@auth_endpoint.route("/logout", methods=["GET"])
@login_required
def logout():
    """Logout view"""
    logout_user()
    flash('Logged out')
    return redirect(url_for('auth_endpoint.login'))

@auth_endpoint.route("/home", methods=["GET"])
@login_required
def home():
    """Home view"""
    return render_template('home.html')
