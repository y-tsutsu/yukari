from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_db(app):
    from .character import CharacterTable

    db.init_app(app)
    CharacterTable.init_db(app)
