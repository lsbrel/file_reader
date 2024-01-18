from model.model import Model

class Aparelho(Model):

    table = 'aparelho'
    attr = ['nome', 'modelo', 'usuario_id']

    def __init__(self):
        pass
