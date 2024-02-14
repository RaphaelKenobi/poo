from avaliacao import Avaliacao

class Carro:
    carros = []

    def __init__(self, cor, ano, nome):
        self.nome = nome
        self.cor = cor
        self.ano = ano
        self.funcionando = True
        self.avaliacao = []
        Carro.carros.append(self)

    def __str__(self):
        return f"{self.nome} | {self.cor} | {self.ano}"

    @classmethod
    def listar_carros(cls):
        print(
            f'{"Nome do carro".ljust(25)} | {"Cor do carro".ljust(25)} | {"Ano do carro".ljust(25)} | {"Avaliação".ljust(25)} | {"Funcionando"}')
        for carro in cls.carros:
            print(
                f'{carro.nome.ljust(25)} | {carro.cor.ljust(25)} | {str(carro.ano).ljust(25)} | {str(carro.media_avaliacoes).ljust(25)} | {carro.ativo}')

    @property
    def ativo(self):
        return "x" if self.funcionando else "o"

    def alterar_estado(self):
        self.funcionando = not self.funcionando

    def receba_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self.avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self.avaliacao:
            return 0
        else:
            soma_das_notas = sum(avaliacao.nota for avaliacao in self.avaliacao)
            quantidade_de_avaliacoes = len(self.avaliacao)
            media = round(soma_das_notas / quantidade_de_avaliacoes,1)
            return media