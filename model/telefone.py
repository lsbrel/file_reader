from model.model import Model

class Telefone(Model):

    table = 'telefone'
    attr = ['numero', 'tipo_telefone_id', 'ativo']

    def __init__(self):
        pass
