from flask_restful import Resource, reqparse
from flask import Blueprint, abort

from e_sport_app import api, db
from e_sport_app.player.models import Player

import json


player = Blueprint('player', __name__)


parser = reqparse.RequestParser()

parser.add_argument('id', type = int)
parser.add_argument('nome_do_jogador', type = str)
parser.add_argument('nickname', type = str)
parser.add_argument('nome_do_time', type = str)
parser.add_argument('role', type = str)
parser.add_argument('total_de_abatimentos', type = int)
parser.add_argument('total_de_assistencias', type = int)
parser.add_argument('total_de_mortes', type = int)
parser.add_argument('total_de_partidas_jogadas', type = int)
parser.add_argument('total_de_vitorias', type = int)


@player.route("/")
@player.route("/home")
def home():
    return "List of players"


class PlayerAPI(Resource):
    def get(self, id=None, page=1):
        if id == None:
            players = Player.query.paginate(page, 5).items
        else:
            players = [Player.query.get(id)]
        
        if len(players) == 0 or players[0] == None:
            return json.dumps({})

        res = {}
        for player in players:
            res.update(player.toJson())
            
        return json.dumps(res)

    def post(self):
        args = parser.parse_args()

        player = Player()
        player.selfUpdateFromArgs(args)

        db.session.add(player)
        db.session.commit()

        return json.dumps(player.toJson())

    def put(self, id):
        player = Player.query.get(id)
        
        if not player:
            abort(404)
        
        args = parser.parse_args()

        player.selfUpdateFromArgs(args)

        db.session.commit()

        return json.dumps(player.toJson())
    
    def delete(self, id):
        player = Player.query.get(id)
        
        if not player:
            abort(404)

        db.session.delete(player)
        db.session.commit()

        res = {'id': id}
        return json.dumps(res)

api.add_resource(
    PlayerAPI,
    '/api/player/<int:id>',
    '/api/players',
    '/api/players/<int:page>'
)
