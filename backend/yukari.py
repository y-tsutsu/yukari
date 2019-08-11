from app.factory import create_app
from models.character import CharacterTable


def main():
    app = create_app(__name__)
    CharacterTable.init_db(app)
    app.run(debug=True, host='0.0.0.0', port=80)


if __name__ == '__main__':
    main()
