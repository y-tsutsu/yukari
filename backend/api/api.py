from flask import Blueprint, abort
from flask_restful import Api, Resource

from models.character import get_characters_all

api_bp = Blueprint('api', __name__, url_prefix='/api')
api = Api(api_bp)


class Info(Resource):
    def get(self):
        characters = get_characters_all()
        return [{'name': x['name'], 'cv': x['cv'], 'note': x['note'],
                 'pos': f'({int(x["x"]) + int(x["width"]) // 2}, {int(x["y"]) + int(x["height"]) // 2})'}
                for x in characters]

    def post(self):
        abort(404)

    def put(self):
        abort(404)

    def delete(self):
        abort(404)


api.add_resource(Info, '/infos')
