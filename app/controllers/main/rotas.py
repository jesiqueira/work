from flask import render_template, redirect, flash, url_for, Blueprint

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
@main.route('/index')
def home():
    return render_template('index.html', tile='Index')
