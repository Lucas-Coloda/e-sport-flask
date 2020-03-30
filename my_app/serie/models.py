from my_app import db

class Serie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100))
    genero = db.Column(db.String(100))
    ativa =  db.Column(db.Boolean) # vira um tinyint(1)
    media_no_imdb = db.Column(db.Float(asdecimal=True))
    total_de_temporadas = db.Column(db.Integer)

    def __init__(self, titulo, genero, ativa, media_no_imdb, total_de_temporadas):
        self.titulo = titulo
        self.genero = genero
        self.ativa = ativa
        self.media_no_imdb = media_no_imdb
        self.total_de_temporadas = total_de_temporadas

    def __repr__(self):
        return 'Série {0}'.format(self.id)