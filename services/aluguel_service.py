from repositories.aluguel import *

from repositories.cliente import select_object as select_cliente
from repositories.veiculo import select_object as select_veiculo

from dto.aluguel_dto import AluguelDto

def aluguel_service():

    service = True

    while service:
        escolha = int(input("Digite qual operação deseja fazer:\n[1] Inserir aluguel\n[2] Atualizar um aluguel\n[3] Consultar um aluguel\n[4] Consultar todos os alugueis\n[5] Devolução de veiculos\n[0] Voltar ao menu\n: "))

        if escolha == 0:
            service = False

        elif escolha == 1 or escolha == 2:
            placa = input("Digite a placa do veiculo:\n")
            cpf = input("Digite o cpf do cliente:\n")
            qtd_dia = int(input("Digite a quantidade de dias:\n"))

            veiculo = select_veiculo(placa)
            cliente = select_cliente(cpf)

            aluguel = AluguelDto(veiculo, cliente, qtd_dia)
            create_update(aluguel)

        elif escolha == 3:
            pass
        
        elif escolha == 4:
            find_all()

        elif escolha == 5:
            placa = input("Digite a placa do veiculo para devolução:\n")
            delet(placa)