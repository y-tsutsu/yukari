from flask import Blueprint, render_template

spa = Blueprint('spa', __name__, url_prefix='/')


@spa.route('/', defaults={'path': ''})
@spa.route('/<path:path>')
def index(path):
    return render_template('index.html')
