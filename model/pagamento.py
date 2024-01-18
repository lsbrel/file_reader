from model.model import Model

class Pagamento(Model):

    table = 'pagamento'
    attr = ['data_pagamento', 'status_pagamento_id', 'forma_pagamento_id']

    def __init__(self):
        pass
