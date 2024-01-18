from model.model import Model

class ClienteTelefone(Model):

    table = 'cliente_telefone'
    attr = ['cliente_id', 'telefone_id']

    def __init__(self):
        pass
