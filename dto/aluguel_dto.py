from datetime import datetime, timedelta

from .veiculo_dto import VeiculoDto
from .cliente_dto import ClienteDto

class AluguelDto:
    def __init__(self, veiculo : VeiculoDto, cliente : ClienteDto, qtd_dias: int) -> None:
        self.placa = veiculo.placa
        self.cpf = cliente.cpf
        self.qtd_dias = qtd_dias
        self.valor_dia = veiculo.valor_dia
        self.valor_total = self.qtd_dias*self.valor_dia
        self.data_locacao = datetime.today().strftime('%d-%m-%Y')
        self.data_devolucao = (datetime.today() + timedelta(days=self.qtd_dias)).strftime("%d-%m-%Y")