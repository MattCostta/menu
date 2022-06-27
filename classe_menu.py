from agenda import *

class Menu:
    def __init__(self):
        agenda = Agenda()


        while True:
            entrada = input('1 - Novo Contato \n2 - Listar Contato \n3 - Modificar Contato \n0 - Sair')
            if entrada =='1':
                agenda.armazenar_contatos()
            elif entrada =='2':
                agenda.armazenar_contatos()
            elif entrada =='3':
                agenda.alterar()
            elif entrada =='0':
                break
            else:
                print('Opção inválida!')