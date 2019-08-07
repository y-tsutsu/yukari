from flask import Flask, render_template

from api.api import api_bp
from camera.camera import camera_bp
from config import BaseConfig

app = Flask(__name__, static_folder='../frontend/dist/static', template_folder='../frontend/dist')
app.register_blueprint(api_bp)
app.register_blueprint(camera_bp)
app.config.from_object(BaseConfig)

config = app.config


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")


def main():
    app.run(debug=True, host='0.0.0.0', port=80)


if __name__ == "__main__":
    main()
