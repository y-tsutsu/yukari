from datetime import datetime

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Character(db.Model):
    __tablename__ = 'characters'

    pk = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    cv = db.Column(db.Text)
    note = db.Column(db.Text)
    x = db.Column(db.Integer)
    y = db.Column(db.Integer)
    width = db.Column(db.Integer)
    height = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)


class CharacterTable:
    _app = None

    @classmethod
    def init_db(cls, app):
        cls._app = app

        with cls._app.app_context():
            db.init_app(app)
            db.create_all()

            characters = Character.query.order_by(Character.pk).all()
            if not characters:
                yuzuko = Character(name='野々原 ゆずこ', cv='大久保 瑠美', note='天真爛漫な性格で元気で無邪気な少女。いたずら好きでよく唯にしており、また奇妙な言動や発想も多い。しかし、成績は優秀で、時々急に真面目になることもある。')
                yukari = Character(name='日向 縁', cv='種田 梨沙', note='家はお金持ち。天然でほんわかとしているが、時々勘が鋭いこともある。')
                yui = Character(name='櫟井 唯', cv='津田 美波', note='情報処理部の部員3人の中では一番の常識人でしっかり者。サバサバとした性格で言動もやや男性的であり、毎回暴走しがちなゆずこと天然な縁に対するツッコミ役でもある。高校2年から胸が急成長している。')
                db.session.add_all([yuzuko, yukari, yui])
                db.session.commit()

            CharacterTable.update_positons([(i + 1, 0, 0, 0, 0) for i in range(len(characters))])

    @classmethod
    def get_characters_all(cls):
        with cls._app.app_context():
            characters = Character.query.order_by(Character.pk).all()
            return [{'name': x.name, 'cv': x.cv, 'note': x.note, 'x': x.x, 'y': x.y, 'width': x.width, 'height': x.height} for x in characters]

    @classmethod
    def update_positon(cls, pk, x, y, width, height):
        with cls._app.app_context():
            character = Character.query.filter(Character.pk == pk).first()
            character.x = x
            character.y = y
            character.width = width
            character.height = height
            db.session.commit()

    @classmethod
    def update_positons(cls, rows):
        with cls._app.app_context():
            for pk, x, y, width, height in rows:
                character = Character.query.filter(Character.pk == pk).first()
                character.x = x
                character.y = y
                character.width = width
                character.height = height
            db.session.commit()
