import json
from flask import Blueprint, abort
from flask_restful import Resource, reqparse
from my_app.serie.models import Serie
from my_app import api, db

serie = Blueprint('serie', __name__)

parser = reqparse.RequestParser()
parser.add_argument('titulo', type = str)
parser.add_argument('genero', type = str)
parser.add_argument('ativa', type = bool)
parser.add_argument('media_no_imdb', type = int)
parser.add_argument('total_de_temporadas', type = int)

@serie.route("/")
@serie.route("/home")
def home():
    return "Catálogo de series"

class SerieAPI(Resource):
    def get(self, id=None, page=1):
        if not id:
            series = Serie.query.paginate(page, 20).items
        else:
            series = [Serie.query.get(id)]
        if not series:
            abort(404)
        res = {}
        if len(series) != 0  and series[0] != None:
            for con in series:
                res[con.id] = {
                    'titulo' : con.titulo,
                    'genero' : con.genero,
                    'ativa' : con.ativa,
                    'media_no_imdb' : str(con.media_no_imdb),
                    'total_de_temporadas' : con.total_de_temporadas,
                }
            
        return json.dumps(res)

    def post(self):
        args = parser.parse_args()
        titulo = args['titulo']
        genero = args['genero']
        ativa = args['ativa']
        media_no_imdb = args['media_no_imdb']
        total_de_temporadas = args['total_de_temporadas']

        con = Serie(titulo, genero, ativa, media_no_imdb, total_de_temporadas)
        db.session.add(con)
        db.session.commit()
        res = {}
        res[con.id] = {
                'titulo': con.titulo,
                'genero': con.genero,
                'ativa': con.ativa,
                'media_no_imdb': str(con.media_no_imdb),
                'total_de_temporadas': con.total_de_temporadas,
        }
        return json.dumps(res)

api.add_resource(
    SerieAPI,
    '/api/serie',
    '/api/serie/<int:id>',
    '/api/serie/<int:id>/<int:page>'
)
