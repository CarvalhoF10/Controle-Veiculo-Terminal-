from repositories.veiculo import *
from dto.veiculo_dto import VeiculoDto

def veiculo_service():
    service = True

    while service:
        escolha = int(input("Oque deseja fazer:\n[1] Cadastrar novo veiculo\n[2] Atualizar veiculo\n[3] Consultar veiculo\n[4] Ver todos os veiculos\n[5] Excluir veiculo\n[0] Voltar ao menu\n: "))

        if escolha == 0:
            service = False
        
        elif escolha == 1 or escolha == 2:
            placa = input("Digite a placa do veiculo:\n")
            modelo = input("Digite o modelo do veiculo:\n")
            ano_fabricacao = input("Digite o ano de fabricação do veiculo:\n")
            qtd_portas = int(input("Digite a quantidade de portas o veiculo possui:\n"))
            valor_diario = float(input("Digite o valor diario do aluguel do veiculo:\n"))

            veiculo = VeiculoDto(placa, modelo, ano_fabricacao, qtd_portas, valor_diario)

            insert_update(veiculo)
        
        elif escolha == 3:
            placa = input("Digite a placa do veiculo:\n")

            select_one(placa)
        
        elif escolha == 4:
            select_all()
        
        elif escolha == 5:
            placa = input("Digite a placa do veiculo:\n")

            esc = print("Tem certeza que deseja excluir este veiculo?\n[S] Sim\n[N] Não\n: ")

            if esc == "S" or esc == "s":
                delet(placa)