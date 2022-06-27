from classe_contato import *

class Agenda:
    def __init__(self):
        self.listaContatos = []



    def armazenar_contatos(self):
        self.listaContatos.append(Contato())



    def listar_contatos(self):
        for i in range(len(self.listaContatos[i])):
            print('Cod:',self.listaContatos[i]. cod,
                  'Nome:', self.listaContatos[i].nome,
                  'Telefone:', self.listaContatos[i].telefone)

    def alterar(self):
        modificar = input("Informe o código da pessoa")
        for i in range(len(self.listaContatos)):
            if modificar == self.listaContatos[i].cod
             self.listaContatos[i].telefone = input('Digite o novo telefone')