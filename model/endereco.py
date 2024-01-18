from model.model import Model

class Endereco(Model):

    table = 'endereco'
    attr = ['nome', 'rua', 'numero', 'bairro', 'cep', 'latitude', 'longitude']

    def __init__(self):
        pass
