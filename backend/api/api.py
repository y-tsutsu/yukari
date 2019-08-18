from flask import Blueprint, abort
from flask_restful import Api, Resource

from models.character import CharacterTable

api = Blueprint('api', __name__, url_prefix='/api')


class CharacterInfo(Resource):
    def get(self):
        characters = CharacterTable.get_characters_all()
        return [{'name': x['name'], 'cv': x['cv'], 'note': x['note'],
                 'pos': f'({int(x["x"]) + int(x["width"]) // 2}, {int(x["y"]) + int(x["height"]) // 2})'}
                for x in characters]

    def post(self):
        abort(404)

    def put(self):
        abort(404)

    def delete(self):
        abort(404)


rest_api = Api(api)
rest_api.add_resource(CharacterInfo, '/characters')
