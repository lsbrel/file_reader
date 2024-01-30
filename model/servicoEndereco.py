from model.model import Model

class ServicoEndereco(Model):

    table = 'servico_endereco'
    attr = ['servico_id', 'endereco_id']

    def __init__(self) -> None:
        pass
