from flask import Blueprint, render_template

app_bp = Blueprint('app', __name__, url_prefix='/')


@app_bp.route('/', defaults={'path': ''})
@app_bp.route('/<path:path>')
def catch_all(path):
    return render_template('index.html')
