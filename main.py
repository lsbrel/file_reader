#!/bin/env/python3

# LIBS
import sys
# LIBS

# MODELS
from model.aparelho import Aparelho
from model.cliente import Cliente
from model.pagamento import Pagamento
from model.servico import Servico
from model.servicoTipo import ServicoTipo
from model.tipoServico import TipoServico
from model.telefone import Telefone
from model.clienteTelefone import ClienteTelefone
from model.endereco import Endereco
from model.clienteEndereco import ClienteEndereco
# MODELS

# CONTROLLER
from controller.fileController import FileController
from controller.timeController import TimeController
from controller.inputController import InputController
# CONTROLLER


# POSICOES DE INSERCAO
field_position = {
    "d":{
        "data_servico": 0,
        "orem_servico": 2,
        "aparelho": 3,
        "cliente": 4,
        "telefone": 5,
        "tipo_servico": 6,
        "data_pagamento": 8,
        "rua": 9,
        "numero": 10,
        "cidade": 11
    },
    "e": {

    },
    "f":{

    }
}
# POSICOES DE INSERCAO


# INSTANCIANDO MODELS
aparelho = Aparelho()
cliente = Cliente()
pagamento = Pagamento()
servico = Servico()
servico_tipo = ServicoTipo()
tipo_servico = TipoServico()
telefone = Telefone()
cliente_telefone = ClienteTelefone()
endereco = Endereco()
cliente_endereco = ClienteEndereco()
# INSTANCIANDO MODELS



def chooseFluxo():

    if sys.argv[2] == '--service':
        pass

    elif sys.argv[2] == '--client':
        client()

    elif sys.argv[2] == '--city':
        city()

    elif sys.argv[2] == '--type-sevice':
        type_service()

    elif sys.argv[2] == '--equipment':
        equipment()

    else:
        print("no mode selected")
        sys.exit()



def client():
    aux = file_controller.print(csv_line['Cliente'])

    id = cliente.findByName(aux)

    if id:
        file_controller.setData(index=item, value=id, position='Cliente')

    else:
        input_value = input(f"[{item}/{file_controller.getNumLines()}] {aux} => ")

        if(input_value == 's'):
            cliente.create([aux, 1, 2])
            file_controller.setData(index=item, value=cliente.getId(), position='Cliente')

        else:
            file_controller.setData(index=item, value=input_value, position='Cliente')


def city():
    aux = file_controller.print(csv_line['Cidade'])

    if aux == "PL":
        file_controller.setData(index=item, value='10', position='Cidade')

    elif aux == 'CBom' or aux == 'C Bom' or aux == 'C bom' or aux == 'Cbom':
        file_controller.setData(index=item, value='5', position='Cidade')

    elif aux == 'Ivoti':
        file_controller.setData(index=item, value='2', position='Cidade')

    elif aux == 'LCollor':
        file_controller.setData(index=item, value='4', position='Cidade')

    elif aux == 'EV':
        file_controller.setData(index=item, value='9', position='Cidade')

    elif aux == 'NH':
        file_controller.setData(index=item, value='6', position='Cidade')

    else:
        input_value = input(f"[{item}/{file_controller.getNumLines()}] {aux} => ")
        file_controller.setData(index=item, value=int(input_value), position='Cidade')

def type_service():

    aux = file_controller.print(csv_line['Servico'])

    if aux == "Higienização":
        file_controller.setData(index=item, value='2', position='Servico')

    elif aux == "Higienizar, Desinstalar":
        file_controller.setData(index=item, value='2,6', position='Servico')

    elif aux == "Instalação":
        file_controller.setData(index=item, value='5', position='Servico')

    elif aux == "Desinstalar":
        file_controller.setData(index=item, value='6', position='Servico')

    elif aux == "Desinstalar, higienizar e instalar" or aux == 'Higienizar, Desinstalar e Instalar':
        file_controller.setData(index=item, value='2,5,6', position='Servico')

    elif aux == "Venda e Instalação":
        file_controller.setData(index=item, value='5,7', position='Servico')


    else:
        input_value = input(f"[{item}/{file_controller.getNumLines()}] {aux} => ")
        file_controller.setData(index=item, value=int(input_value), position='Servico')


def equipment():

    aux = file_controller.print(csv_line['Aparelho'])

    if aux == "Ar Split":
        file_controller.setData(index=item, value=1, position='Aparelho')

    else:
        input_value = input(f"[{item}/{file_controller.getNumLines()}] {aux} => ")
        file_controller.setData(index=item, value=int(input_value), position='Aparelho')


if __name__ == '__main__':

    # VALIDAR INPUTS
    # InputController()
    # VALIDAR INPUTS

    # INSTANCIANDO CONTROLLERS
    file_controller = FileController(sys.argv[1])
    time_controller = TimeController()
    # INSTANCIANDO CONTROLLERS

    # MAIN LOOP
    for item in range(file_controller.getNumLines()):
        csv_line = file_controller.getData(index=item)

        chooseFluxo()


    file_controller.saveFile(sys.argv[1])