import json
from dto.veiculo_dto import VeiculoDto

def select_all() -> bool:
    try:

        veiculo: dict = json.loads(open("data/veiculo.json").read())

        for i in veiculo:
            print(f"placa: {i} || modelo: {veiculo[i]["modelo"]} || Qtd Portas {veiculo[i]["qtd_portas"]} || Ano Fabricação {veiculo[i]["ano_fabricacao"]} || Valor ao dia: {veiculo[i]["valor_dia"]}\n")

        return True
    
    except Exception as ex:

        print(f"Error: {ex}")
        return False
    
def select_object(placa: str) -> VeiculoDto:
    try:
    
        print("chegou aqui 1")
        veiculo: dict = json.loads(open("data/veiculo.json").read())

        newveiculo = VeiculoDto(placa, veiculo[placa]["modelo"], veiculo[placa]["ano_fabricacao"], veiculo[placa]["qtd_portas"], veiculo[placa]["valor_dia"])

        print("chegou aqui 3")
        print(newveiculo.placa)

        return newveiculo

    except Exception as ex:
        print(f"Error: {ex}")
        return False
    
def select_one(placa: str) -> bool:
    try:

        veiculo: dict = json.loads(open("data/veiculo.json").read())

        print(f"placa: {placa} || modelo: {veiculo[placa]["modelo"]} || Qtd Portas {veiculo[placa]["qtd_portas"]} || Ano Fabricação {veiculo[placa]["ano_fabricacao"]} || Valor ao dia: {veiculo[placa]["valor_dia"]}\n")
            
        return True
    
    except Exception as ex:

        print(f"Error: {ex}  +  veiculo inexistente")
        return False

def insert_update(v : VeiculoDto) -> bool:
    try:

        veiculo: dict = json.loads(open("data/veiculo.json").read())
        
        veiculo[v.placa] = {
                "modelo": v.modelo,
                "qtd_portas": v.qtd_portas,
                "ano_fabricacao": v.ano_fabricacao,
                "valor_dia": v.valor_dia
            }
        
        veiculo = json.dumps(veiculo)

        with open("data/veiculo.json", "w") as save:
            save.writelines(veiculo)

        return True
    
    except Exception as ex:

        print(f"Error: {ex}")
        return False

def delet(placa: str) -> bool:
    try:

        veiculo: dict = json.loads(open("data/veiculo.json").read())

        veiculo.pop(f"{placa}")

        veiculo = json.dumps(veiculo)

        with open("data/veiculo.json", "w") as save:
            save.writelines(veiculo)

        return True

    except Exception as ex:
        
        print(f"Error: {ex}")
        return False
