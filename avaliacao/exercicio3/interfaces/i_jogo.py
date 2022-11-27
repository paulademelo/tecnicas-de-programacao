from abc import ABCMeta, abstractclassmethod


class IJogo(metaclass=ABCMeta):
    @staticmethod
    @abstractclassmethod
    def add_vencedor(posicao, nome, pontos, jogadores):
        "Implementar interface"
