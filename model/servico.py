from model.model import Model

class Servico(Model):

    table = 'servico'
    attr = ['ordem_servico', 'data_servico', 'aparelho_id', 'status_servico_id', 'cliente_id', 'usuario_id', 'pagamento_id']

    def __init__(self):
        pass
