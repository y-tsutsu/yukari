from flask import Blueprint, abort
from flask_restful import Api, Resource

api_bp = Blueprint('api', __name__, url_prefix="/api",)
api = Api(api_bp)


class Info(Resource):
    def get(self):
        return [
            {
                'name': '野々原 ゆずこ',
                'cv': '大久保 瑠美',
                'note': '天真爛漫な性格で元気で無邪気な少女。いたずら好きでよく唯にしており、また奇妙な言動や発想も多い。しかし、成績は優秀で、時々急に真面目になることもある。'
            },
            {
                'name': '日向 縁',
                'cv': '種田 梨沙',
                'note': '家はお金持ち。天然でほんわかとしているが、時々勘が鋭いこともある。'
            },
            {
                'name': '櫟井 唯',
                'cv': '津田 美波',
                'note': '情報処理部の部員3人の中では一番の常識人でしっかり者。サバサバとした性格で言動もやや男性的であり、毎回暴走しがちなゆずこと天然な縁に対するツッコミ役でもある。高校2年から胸が急成長している。'
            }
        ]

    def post(self):
        abort(404)

    def put(self):
        abort(404)

    def delete(self):
        abort(404)


api.add_resource(Info, '/infos')
