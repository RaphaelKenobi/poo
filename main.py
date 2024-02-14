from carros import Carro

carro_1 = Carro("vermelho", 2020, "Fusca")
carro_2 = Carro("azul", 2019, "Gol")
carro_3 = Carro("preto", 2018, "Celta")

carro_1.receba_avaliacao("João", 5)
carro_1.receba_avaliacao("Maria", 4)
carro_1.receba_avaliacao("José", 8)
carro_2.receba_avaliacao("Pedro", 9)
carro_2.receba_avaliacao("Ana", 7)
carro_3.receba_avaliacao("Carlos", 6)


def main():
    Carro.listar_carros()

if __name__ == '__main__':
    main()