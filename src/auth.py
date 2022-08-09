from flask import request, Flask, Blueprint, flash, g, redirect, render_template,  session, url_for
from flask_login import login_user, logout_user
from numpy import half
from werkzeug.security import check_password_hash, generate_password_hash
import os
from . import login_manager
bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login', methods=('GET', 'POST'))
def login():
    salt = '123456uwu654321'
    with open(f'{os.path.dirname(__file__)}/password.txt', 'r') as f:
        h = f.read()
    if request.method == 'POST':
        password = request.form['password']
        
        if check_password_hash(h, salt+password):
            session['logged_in'] = True
            login_user(User())
            return redirect(url_for('index'))
    
    return render_template('auth/login.html')

@bp.route('/logout')
def logout():
    session['logged_in'] = False
    logout_user()
    return redirect(url_for('index'))

class User:
    def __init__(self):
        pass
    def is_authenticated(self):
        return True
    def is_active(self):
        return True
    def is_anonymous(self):
        return False
    def get_id(self):
        return 1

@login_manager.user_loader
def load_user(user_id):
    return User()

@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('auth.login'))

