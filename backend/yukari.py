from flask import Flask

from api.api import api_bp
from app.views import app_bp
from config import BaseConfig
from models.character import CharacterTable
from videos.views import video_bp


def create_app():
    app = Flask(__name__, static_folder='../frontend/dist/static', template_folder='../frontend/dist')
    app.register_blueprint(api_bp)
    app.register_blueprint(video_bp)
    app.register_blueprint(app_bp)
    app.config.from_object(BaseConfig)
    return app


def main():
    app = create_app()
    CharacterTable.init_db(app)
    app.run(debug=True, host='0.0.0.0', port=80)


if __name__ == '__main__':
    main()
