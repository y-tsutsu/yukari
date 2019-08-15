from os import path

from flask import Flask

from api.api import api_bp
from config import BaseConfig
from videos.views import video_bp

from .views import app_bp


def create_app(name, front_root):
    app = Flask(name, static_folder=path.join(front_root, 'static'), template_folder=front_root)
    app.register_blueprint(api_bp)
    app.register_blueprint(video_bp)
    app.register_blueprint(app_bp)
    app.config.from_object(BaseConfig)
    return app
