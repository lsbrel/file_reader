from model.model import Model
from controller.fileController import FileController

class Cliente(Model):

    table = 'cliente'
    attr = ['nome', 'status_cliente_id', 'usuario_id']

    def __init__(self):
        pass
