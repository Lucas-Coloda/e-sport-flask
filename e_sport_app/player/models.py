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

    def __init__(self, id = None, nome_do_jogador = None, nickname = None, nome_do_time = None, role = None, total_de_abatimentos = None, total_de_assistencias = None, total_de_mortes = None, total_de_partidas_jogadas = None, total_de_vitorias = None):
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
        
    def selfUpdateFromArgs(self, args):
        self.id = args[id] if self.id == None else self.id
        self.nome_do_jogador = args['nome_do_jogador']
        self.nickname = args['nickname']
        self.nome_do_time = args['nome_do_time']
        self.role = args['role']
        self.total_de_abatimentos = args['total_de_abatimentos']
        self.total_de_assistencias = args['total_de_assistencias']
        self.total_de_mortes = args['total_de_mortes']
        self.total_de_partidas_jogadas = args['total_de_partidas_jogadas']
        self.total_de_vitorias = args['total_de_vitorias']
    
    def toJson(self):
        return {
            self.id: {
                    'nome_do_jogador': self.nome_do_jogador,
                    'nickname': self.nickname,
                    'nome_do_time': self.nome_do_time,
                    'role': self.role,
                    'total_de_abatimentos': self.total_de_abatimentos,
                    'total_de_assistencias': self.total_de_assistencias,
                    'total_de_mortes': self.total_de_mortes,
                    'total_de_partidas_jogadas': self.total_de_partidas_jogadas,
                    'total_de_vitorias': self.total_de_vitorias,
                    'porcentagem_vitorias': self.porcentagem_vitorias(),
                    'kda': self.kda(),
            }
        }
    
    def __repr__(self):
        return 'Player {0}'.format(self.id)
