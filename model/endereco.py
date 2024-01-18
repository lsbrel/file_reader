from model.model import Model

class Endereco(Model):

    table = 'endereco'
    attr = ['rua', 'numero', 'bairro', 'cidade_id']

    def __init__(self):
        pass
