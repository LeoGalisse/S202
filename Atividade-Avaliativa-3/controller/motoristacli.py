from bson import ObjectId
from database.database import Database
from entity.corrida import Corrida
from model.motoristadao import MotoristaDAO

class MotoristaCLI:
    def __init__(self, database: Database):
        self.db = database
        self.dao = MotoristaDAO(database)

    def menu(self):
        while True:
            print("\nMenu:")
            print("1. Criar motorista")
            print("2. Ler motorista")
            print("3. Atualizar motorista")
            print("4. Deletar motorista")
            print("5. Sair")

            choice = input("Escolha uma opção: ")

            if choice == "1":
                self.criar_motorista()
            elif choice == "2":
                self.ler_motorista()
            elif choice == "3":
                self.atualizar_motorista()
            elif choice == "4":
                self.deletar_motorista()
            elif choice == "5":
                print("Saindo...")
                break
            else:
                print("Opção inválida. Tente novamente.")

    def criar_motorista(self):
        nome_passageiro = input("Nome do passageiro: ")
        documento_passageiro = input("Documento do passageiro: ")
        passageiro_data = {"nome": nome_passageiro, "documento": documento_passageiro}


        corridas = []
        while True:
            nota = int(input("Nota da corrida: "))
            distancia = float(input("Distância percorrida: "))
            valor = float(input("Valor da corrida: "))
            corrida_data = {"nota": nota, "distancia": distancia, "valor": valor, "passageiro": passageiro_data}
            corrida = Corrida(**corrida_data)
            corridas.append(corrida.__dict__)


            another = input("Deseja adicionar outra corrida? (S/N): ")
            if another.lower() != "s":
                break

        nota_motorista = int(input("Nota do motorista: "))
        motorista_data = {"nota": nota_motorista, "corridas": corridas}

        self.dao.criar_motorista(motorista_data)

    def ler_motorista(self):
        _id = input("Digite o ID do motorista: ")
        motorista = self.dao.ler_motorista({"_id": ObjectId(_id)})
        if motorista:
            print("Motorista encontrado:", motorista)
        else:
            print("Motorista não encontrado.")

    def atualizar_motorista(self):
        _id = input("Digite o ID do motorista que deseja atualizar: ")
        nota = int(input("Nova nota do motorista: "))
        novos_dados = {"nota": nota}
        self.dao.atualizar_motorista({"_id": _id}, novos_dados)

    def deletar_motorista(self):
        _id = input("Digite o ID do motorista que deseja deletar: ")
        self.dao.deletar_motorista({"_id": _id})
        print("Motorista deletado com sucesso!")