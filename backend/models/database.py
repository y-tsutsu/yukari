from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_db(app):
    from .character import CharacterTable

    db.init_app(app)
    with app.app_context():
        db.create_all()
    CharacterTable.init_db(app)
