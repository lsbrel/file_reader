from model.model import Model

class TipoServico(Model):

    table = 'tipo_servico'
    attr = ['nome', 'usuario_id', 'ativo']

    def __init__(self):
        pass
