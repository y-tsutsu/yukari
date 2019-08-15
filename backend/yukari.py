from argparse import ArgumentParser

from app.factory import create_app
from models.character import CharacterTable


def create_arg_parser():
    parser = ArgumentParser(description='This is a web application that performs image processing on video from a '
                            'network camera, etc., and displays the processed video and information on the '
                            'browser in real time.')
    parser.add_argument('front_root', nargs='?', default='./', help='front-end root directory.')
    return parser


def main():
    parser = create_arg_parser()
    args = parser.parse_args()
    app = create_app(__name__, args.front_root)
    CharacterTable.init_db(app)
    app.run(debug=True, host='0.0.0.0', port=80)


if __name__ == '__main__':
    main()
