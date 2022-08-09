from flask import request, Flask, Blueprint, flash, g, redirect, render_template,  session, url_for
from numpy import half
from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint('posts', __name__, url_prefix='/posts')

@bp.route('/<name>')
def post(name):
    return render_template(f'posts/{name}.html')

