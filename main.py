#!/bin/env/python3

# LIBS
import sys
import math
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
from model.servicoEndereco import ServicoEndereco
# MODELS

# CONTROLLER
from controller.fileController import FileController
from controller.timeController import TimeController
from controller.inputController import InputController
# CONTROLLER


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
servico_endereco = ServicoEndereco()
# INSTANCIANDO MODELS



def chooseFluxo():

    if sys.argv[2] == '--service':
        service()

    elif sys.argv[2] == '--client':
        client()

    elif sys.argv[2] == '--city':
        city()

    elif sys.argv[2] == '--type-service':
        type_service()

    elif sys.argv[2] == '--equipment':
        equipment()

    elif sys.argv[2] == '--payment':
        payment()

    else:
        print("no mode selected")
        sys.exit()



def service():

    # PAGAMENTO
    data_pagamento = file_controller.prettier(csv_line['Pagamento'])
    data_pagamento = f'{file_controller.getYear(sys.argv[1])}-{file_controller.transformDate(date=data_pagamento)}'

    try:
        forma_pagamento = file_controller.prettier(csv_line['Forma'])
    except:
        forma_pagamento = 9

    pagamento.create(data=(data_pagamento, 3, forma_pagamento))
    # PAGAMENTO

    # SERVICO
    data_servico = file_controller.prettier(csv_line['Data'])
    data_servico = f'{file_controller.getYear(sys.argv[1])}-{file_controller.transformDate(date=data_servico)}'

    ordem_servico = file_controller.prettier(csv_line['OS'])
    if ordem_servico != 'NaN' and ordem_servico != '-':
        pass
    else:
        ordem_servico = '0'

    aparelho_id = file_controller.prettier(csv_line['Aparelho'])

    cliente_id = file_controller.prettier(csv_line['Cliente'])


    servico.create(data=(ordem_servico, data_servico, aparelho_id, 4, cliente_id, 2, pagamento.getId()))
    # SERVICO


    # ENDERECO
    rua = file_controller.prettier(csv_line['Rua'])
    if rua == '-':
        rua = ''

    num = file_controller.prettier(csv_line['Num'])
    if num == '-':
        num = ''

    bairro = file_controller.prettier(csv_line['Bairro'])
    if bairro == '-':
        bairro = ''

    cidade_id = file_controller.prettier(csv_line['Cidade'])

    addr_id = 0
    for i in cliente_endereco.findLinkData(id=cliente_id, field='cliente_id'):
        addr = endereco.findLinkData(id=i[2], field='id')
        if(addr[0][2] == rua and addr[0][3] == num and addr[0][4] == bairro):
            addr_id = addr[0][0]
            break

    if(addr_id == 0):
        endereco.create(data=(rua ,num, bairro, cidade_id))
        cliente_endereco.create(data=(cliente_id, endereco.getId()))
        servico_endereco.create(data=(servico.getId(), endereco.getId()))

    else:
        servico_endereco.create(data=(servico.getId(), addr_id))

    # ENDERECO

    # TELEFONE
    numero = file_controller.prettier(csv_line['Telefone'])

    if(numero == '-' or numero == 'NaN'):
        pass

    else:
        if(int(numero[0]) > 1 and int(numero[0]) < 6 and len(numero) == 9):
            tipo_telefone_id = 1

        else:
            tipo_telefone_id = 2


        id = telefone.findByAttr(attr='numero', value=numero)

        if id:
            pass
            # cliente_telefone.create(data=(cliente_id, id))

        else:
            telefone.create(data=(numero, tipo_telefone_id))
            cliente_telefone.create(data=(cliente_id, telefone.getId()))

    # TELEFONE



def client():
    aux = file_controller.prettier(csv_line['Cliente'])

    id = cliente.findByName(aux)

    if id:
        file_controller.setData(index=item, value=id, position='Cliente')

    else:
        input_value = input(f"[{item}/{file_controller.getNumLines()}] {aux} => ")

        if(input_value == 's'):
            cliente.create(data=(aux, 1,2))
            file_controller.setData(index=item, value=cliente.getId(), position='Cliente')

        else:
            file_controller.setData(index=item, value=input_value, position='Cliente')


def city():
    aux = file_controller.prettier(csv_line['Cidade'])

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

    aux = file_controller.prettier(csv_line['Servico'])

    if aux == "Higienização":
        file_controller.setData(index=item, value='2', position='Servico')

    elif aux == "Higienizar, Desinstalar":
        file_controller.setData(index=item, value='2,6', position='Servico')

    elif aux == "Instalação":
        file_controller.setData(index=item, value='5', position='Servico')

    elif aux == "Desinstalar":
        file_controller.setData(index=item, value='6', position='Servico')

    elif aux == "Desinstalar e Instalar" or aux == 'Desinstalar, Instalar' or aux == "Desinstalação e Instalação":
        file_controller.setData(index=item, value='6,5', position='Servico')

    elif aux == "Desinstalar, higienizar e instalar" or aux == 'Higienizar, Desinstalar e Instalar' or aux == ' Higienização, Desinstalação e Instalação':
        file_controller.setData(index=item, value='2,5,6', position='Servico')

    elif aux == "Venda e Instalação":
        file_controller.setData(index=item, value='5,7', position='Servico')


    else:
        input_value = input(f"[{item}/{file_controller.getNumLines()}] {aux} => ")
        file_controller.setData(index=item, value=input_value, position='Servico')


def equipment():

    aux = file_controller.prettier(csv_line['Aparelho'])

    if aux == "Ar Split":
        file_controller.setData(index=item, value=1, position='Aparelho')

    else:
        input_value = input(f"[{item}/{file_controller.getNumLines()}] {aux} => ")
        file_controller.setData(index=item, value=int(input_value), position='Aparelho')



def payment():
    aux = file_controller.prettier(csv_line['Forma'])

    if aux == 'Pix PJ':
        file_controller.setData(index=item, value=3 , position='Forma')

    elif aux == 'Pix PF':
        file_controller.setData(index=item, value=2 , position='Forma')

    elif aux == 'Cartão':
        file_controller.setData(index=item, value=6 , position='Forma')

    elif aux == 'Ted PJ':
        file_controller.setData(index=item, value=5 , position='Forma')

    elif aux == 'Boleto':
        file_controller.setData(index=item, value=1 , position='Forma')

    elif aux == 'R$':
        file_controller.setData(index=item, value=8 , position='Forma')

    else:
        input_value = input(f"[{item}/{file_controller.getNumLines()}] {aux} => ")
        file_controller.setData(index=item, value=int(input_value), position='Forma')


if __name__ == '__main__':

    # VALIDAR INPUTS
    # InputController()
    # VALIDAR INPUTS

    # INSTANCIANDO CONTROLLERS
    file_controller = FileController(sys.argv[1])
    time_controller = TimeController()
    # INSTANCIANDO CONTROLLERS

    # MAIN LOOP
    print(f'Running the file => {sys.argv[1]}')

    for item in range(file_controller.getNumLines()):
        csv_line = file_controller.getData(index=item)

        # HEADER
        print(f'Inserting row => [{item+1}/{file_controller.getNumLines()}]')
        # HEADER


        chooseFluxo()


    print(f'Finished in => {time_controller.getRunTime()} segundos')
    # file_controller.saveFile(sys.argv[1])