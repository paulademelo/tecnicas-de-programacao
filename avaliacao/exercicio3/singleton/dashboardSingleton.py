# O dashboard é o singleton deste projeto
class DashboardSingleton():
    _tabela = {}

    def __new__(cls):
        return cls

    @classmethod
    def print(cls):
        "A class level method"
        print("------------------------ GRUPO G -----------------------")
        for chave, valor in sorted(cls._tabela.items()):
            print("-- Colocação --- ----- País ---- ---- Pontos ----")
            print(f"|\t{chave}\t| \t{valor[1]}\t|\t{valor[2]}\t|")
            print("---------------------- Jogadores -----------------------")
            print(f"{valor[3]}")
            print("*********************************************************")
        print()

    @classmethod
    def add_vencedor(cls, posicao, nome, pontos, jogadores):
        cls._tabela[posicao] = posicao, nome, pontos, jogadores
