from e_sport_app import db

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    nome_do_jogador = db.Column(db.String)
    nickname = db.Column(db.String)
    nome_do_time = db.Column(db.String)
    role = db.Column(db.String)

    total_de_abatimentos = db.Column(db.Integer)
    total_de_assistencias = db.Column(db.Integer)
    total_de_mortes = db.Column(db.Integer)
    total_de_partidas_jogadas = db.Column(db.Integer)
    total_de_vitorias = db.Column(db.Integer)

    def __init__(self, id, nome_do_jogador, nickname, nome_do_time, role, total_de_abatimentos, total_de_assistencias, total_de_mortes, total_de_partidas_jogadas, total_de_vitorias):
        self.id = id
        self.nome_do_jogador = nome_do_jogador
        self.nickname = nickname
        self.nome_do_time = nome_do_time
        self.role = role
        self.total_de_abatimentos = total_de_abatimentos
        self.total_de_assistencias = total_de_assistencias
        self.total_de_mortes = total_de_mortes
        self.total_de_partidas_jogadas = total_de_partidas_jogadas
        self.total_de_vitorias = total_de_vitorias

    def kda(self):
        if self.total_de_mortes == 0:
            return self.total_de_abatimentos + self.total_de_assistencias
        return (self.total_de_abatimentos + self.total_de_assistencias) / self.total_de_mortes

    def porcentagem_vitorias(self):
        return self.total_de_vitorias / self.total_de_partidas_jogadas * 100
        
    def __repr__(self):
        return 'Player {0}'.format(self.id)
