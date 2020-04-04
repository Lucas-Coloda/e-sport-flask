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
            players = Player.query.paginate(page, 20).items
        else:
            players = [Player.query.get(id)]
        if not player:
            abort(404)

        res = {}

        if len(players) != 0  and players[0] != None:
            for con in players:
                res[con.id] = {
                    'nome_do_jogador': con.nome_do_jogador,
                    'nickname': con.nickname,
                    'nome_do_time': con.nome_do_time,
                    'role': con.role,
                    'total_de_abatimentos': con.total_de_abatimentos,
                    'total_de_assistencias': con.total_de_assistencias,
                    'total_de_mortes': con.total_de_mortes,
                    'total_de_partidas_jogadas': con.total_de_partidas_jogadas,
                    'total_de_vitorias': con.total_de_vitorias,
                    'kda': con.kda(),
                    'porcentagem_vitorias': con.porcentagem_vitorias(),
                }
            
        return json.dumps(res)

    def post(self):
        args = parser.parse_args()

        player = Player(
            args['id'],
            args['nome_do_jogador'],
            args['nickname'],
            args['nome_do_time'],
            args['role'],
            args['total_de_abatimentos'],
            args['total_de_assistencias'],
            args['total_de_mortes'],
            args['total_de_partidas_jogadas'],
            args['total_de_vitorias']
        )
        
        db.session.add(player)
        db.session.commit()
        
        res = {}
        res[player.id] = {
                'nome_do_jogador': player.nome_do_jogador,
                'nickname': player.nickname,
                'nome_do_time': player.nome_do_time,
                'role': player.role,
                'total_de_abatimentos': player.total_de_abatimentos,
                'total_de_assistencias': player.total_de_assistencias,
                'total_de_mortes': player.total_de_mortes,
                'total_de_partidas_jogadas': player.total_de_partidas_jogadas,
                'total_de_vitorias': player.total_de_vitorias,
        }
        return json.dumps(res)


api.add_resource(
    PlayerAPI,
    '/api/player/<int:id>',
    '/api/players',
    '/api/players/<int:page>'
)
