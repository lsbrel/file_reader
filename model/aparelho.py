from model.model import Model

class Aparelho(Model):

    table = 'aparelho'
    attr = ['nome', 'descricao', 'usuario_id', 'tipo_aparelho_id', 'ativo']

    def __init__(self):
        pass
