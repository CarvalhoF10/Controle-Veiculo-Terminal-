class VeiculoDto:
    def __init__(self, placa: str, modelo: str, ano_fabricacao: str, qtd_portas: int, valor_dia: float) -> None:
        self.placa = placa
        self.modelo = modelo
        self.ano_fabricacao = ano_fabricacao
        self.qtd_portas = qtd_portas
        self.valor_dia = valor_dia