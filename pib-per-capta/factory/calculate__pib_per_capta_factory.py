from singleton.calculate_pib_per_capta_singleton import CalculatePibPerCaptaSingleton

# Factory responsável por unir a responsabilidade de criação de novos objetos
class CalculatePibFactory:
    @classmethod
    def create_instance(self):
        return CalculatePibPerCaptaSingleton.instance__()