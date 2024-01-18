from model.model import Model

class ClienteEndereco(Model):

    table = 'cliente_endereco'
    attr = ['cliente_id', 'endereco_id']

    def __init__(self):
        pass
