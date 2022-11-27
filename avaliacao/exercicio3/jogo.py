from singleton.dashboardSingleton import DashboardSingleton
from interfaces.i_jogo import IJogo


class Jogo(IJogo):
    def __init__(self):
        self.dashboard = DashboardSingleton()

    def add_vencedor(self, posicao, nome, pontos, jogadores):
        self.dashboard.add_vencedor(posicao, nome, pontos, jogadores)