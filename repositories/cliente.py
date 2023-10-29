import json

from dto.cliente_dto import ClienteDto

def select_all() -> bool:
    try:
        cliente: dict = json.loads(open("data/cliente.json").read())

        for i in cliente:
            print(f"CPF: {i} || Nome: {cliente[i]["Nome"]} || sobrenome: {cliente[i]["Sobrenome"]} || Telefone: {cliente[i]["Telefone"]}\n")
        
        return True
    
    except Exception as ex:
        print(f"Error: {ex}")
        return False

def select_object(cpf: str) -> ClienteDto:
    try:
        cliente: dict = json.loads(open("data/cliente.json").read())

        cliente = ClienteDto(cpf, cliente[cpf]["Nome"], cliente[cpf]["Sobrenome"], cliente[cpf]["Telefone"])

        return cliente

    except Exception as ex:
        print(f"Error: {ex} erro ao encontrar o cliente")
        return False

def select_one(cpf: str) -> bool:
    try:
        cliente: dict = json.loads(open("data/cliente.json").read())

        print(f"CPF: {cpf} || Nome: {cliente[cpf]["Nome"]} || Sobrenome: {cliente[cpf]["Sobrenome"]} || Telefone: {cliente[cpf]["Telefone"]}")

    except Exception as ex:
        print(f"Error: {ex}")
        return False
    
def insert_update(c : ClienteDto) -> bool:
    try:
        cliente: dict = json.loads(open("data/cliente.json").read())

        cliente[c.cpf] = {
            "Nome": c.Nome,
            "Sobrenome": c.Sobrenome,
            "Telefone" : c.telefone
        }

        cliente = json.dumps(cliente)

        with open("data/cliente.json", "w") as save:
            save.writelines(cliente)

        return True
        
    except Exception as ex:
        print(f"Error: {ex}")
        return False
    
def delet(cpf: str) -> bool:
    try:
        cliente: dict = json.loads(open("data/cliente.json").read())

        cliente.pop(cpf)

        cliente = json.dumps(cliente)

        with open("data/cliente.json", "w") as save:
            save.writelines(cliente)

        return True

    except Exception as ex:
        print(f"Error: {ex}")
        return False