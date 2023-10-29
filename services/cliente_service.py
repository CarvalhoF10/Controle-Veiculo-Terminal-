from repositories.cliente import *
from dto.cliente_dto import ClienteDto


def cliente_service():

    service = True

    while service:
        escolha = int(input("Oque deseja fazer:\n[1] Cadastrar novo cliente\n[2] Atualizar Cliente\n[3] Consultar cliente\n[4] Ver todos os clientes\n[5] Excluir cliente\n[0] Voltar ao menu\n: "))

        if escolha == 0:
            service = False

        elif escolha == 1 or escolha == 2:
            cpf = input("Digire o CPF:\n")
            nome = input("Digite o nome:\n")
            sobrenome = input("Digite o sobrenome:\n")
            telefone = input("Digite o telefone de contato:\n")

            cliete = ClienteDto(cpf, nome, sobrenome, telefone)

            insert_update(cliete)

        elif escolha == 3:
            cpf = input("Digire o CPF:\n")
            select_one(cpf)

        elif escolha  == 4:
            select_all()

        elif escolha == 5:
            cpf = input("Digire o CPF:\n")

            dec = input(f"Tem certeza que deseja excluir o cliente de cpf {cpf}:\n[S] Sim\n[N] Não\n: ")

            if dec == "S" or dec == "s":
                delet(cpf)
        else:
            print("Escolha invalida!!")