from argparse import ArgumentParser
from os import path

from flask import Flask

from api.api import api
from config import BaseConfig
from models.character import CharacterTable
from spa.views import spa
from videos.views import video


def create_arg_parser():
    parser = ArgumentParser(description='This is a web application that performs image processing on video from a '
                            'network camera, etc., and displays the processed video and information on the '
                            'browser in real time.')
    parser.add_argument('front_root', nargs='?', default='./', help='front-end root directory.')
    return parser


def create_app(name, front_root):
    app = Flask(name, static_folder=path.join(front_root, 'static'), template_folder=front_root)
    app.register_blueprint(api)
    app.register_blueprint(video)
    app.register_blueprint(spa)
    app.config.from_object(BaseConfig)
    return app


def main():
    parser = create_arg_parser()
    args = parser.parse_args()
    app = create_app(__name__, args.front_root)
    CharacterTable.init_db(app)
    app.run(debug=True, host='0.0.0.0', port=80)


if __name__ == '__main__':
    main()
