from services.cliente_service import cliente_service
from services.veiculo_service import veiculo_service
from services.aluguel_service import aluguel_service

from repositories.veiculo import select_object

print("##################################################################")
print("########## Bem vindo ao sistema de alugueis de veiculos ##########")
print("##################################################################\n")

actived = True

while actived:
    select = int(input("O que deseja fazer:\n[1] Clientes\n[2] Veiculos\n[3] Aluguel\n[4] Sair\n:"))

    if(select == 1):
        cliente_service()
    elif(select == 2):
        veiculo_service()
    elif(select == 3):
        aluguel_service()
    elif(select == 4):
        actived = False
    else:
        print("Escolha invalida")