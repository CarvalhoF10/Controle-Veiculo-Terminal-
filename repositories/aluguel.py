import json

import sys
sys.path.append("..")

from dto.aluguel_dto import AluguelDto

def verify(placa: str):
    alugueis = json.loads(open("data/alugueis.json").read())

    for i in alugueis["alugueis"]:
        if placa in i:
            return False
    
    return True
        

def find_all():
    alugueis = json.loads(open("data/alugueis.json").read())

    for i in alugueis["alugueis"]:
        print(f"ID: {i[0]} || Placa: {i[1]} || CPF: {i[2]} || Qtd de dias: {i[3]} || Valor total: {i[4]} || Data de locação: {i[5]} || Data para devolução: {i[6]}")


def create_update(aluguel : AluguelDto) -> bool:

    disponivel = verify(aluguel.placa)

    if disponivel == True:
        alugueis : dict = json.loads(open("data/alugueis.json").read())

        if aluguel.cpf == None:
            return print("O cliente não existe")
        
        if aluguel.placa == None:
            return print("O veiculo não existe")

        alugueis.update({"id_count": alugueis["id_count"] + 1})

        alugueis["alugueis"].append([alugueis["id_count"], aluguel.placa, aluguel.cpf, aluguel.qtd_dias, aluguel.valor_dia, aluguel.valor_total, aluguel.data_locacao, aluguel.data_devolucao])

        alugueis = json.dumps(alugueis)

        with open("data/alugueis.json", "w") as save:
            save.writelines(alugueis)

        return True
    
    else:
        print("Veiculo não está disponivel")

def delet(placa):
    try:
        
        alugueis : dict = json.loads(open("data/alugueis.json").read())

        for i in alugueis["alugueis"]:
            if placa == i[1]:
                print(i)
                alugueis["alugueis"].remove(i) 

        alugueis = json.dumps(alugueis)

        with open("data/alugueis.json", "w") as save:
            save.writelines(alugueis)

    except Exception as ex:
        print(f"Error: {ex}")