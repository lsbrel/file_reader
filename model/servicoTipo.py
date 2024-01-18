from model.model import Model

class ServicoTipo(Model):

    table = 'servico_tipo'
    attr = ['servico_id', 'tipo_servico_id']

    def __init__(self) -> None:
        pass
